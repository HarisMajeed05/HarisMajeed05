"""
Generates stats.svg, streak.svg, langs.svg, year.svg for the profile README,
using only the Python standard library and the GitHub GraphQL API.

Pinning rules that matter (see write-up):
  - the contribution window is pinned to whole UTC days, not "the past year
    from right now", so two runs a few minutes apart don't shift the
    week-bucketing and produce a no-op-looking diff every night.
  - repositories are filtered to privacy: PUBLIC so the workflow's
    GITHUB_TOKEN and a personal token agree on language percentages.
"""

import json
import os
import urllib.request
from datetime import datetime, timedelta, timezone

GH_LOGIN = os.environ["GH_LOGIN"]
TOKEN = os.environ["GITHUB_TOKEN"]

now = datetime.now(timezone.utc)
to_dt = now.replace(hour=23, minute=59, second=59, microsecond=0)
from_dt = (now - timedelta(days=364)).replace(hour=0, minute=0, second=0, microsecond=0)

QUERY = """
query($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    contributionsCollection(from: $from, to: $to) {
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays { date contributionCount }
        }
      }
    }
    repositories(first: 100, privacy: PUBLIC, ownerAffiliations: OWNER, isFork: false) {
      nodes {
        languages(first: 5, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name color } }
        }
      }
    }
  }
}
"""


def gh_graphql(query, variables):
    body = json.dumps({"query": query, "variables": variables}).encode()
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=body,
        headers={
            "Authorization": f"bearer {TOKEN}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def fetch():
    variables = {
        "login": GH_LOGIN,
        "from": from_dt.isoformat().replace("+00:00", "Z"),
        "to": to_dt.isoformat().replace("+00:00", "Z"),
    }
    return gh_graphql(QUERY, variables)["data"]["user"]


def longest_and_current_streak(days):
    longest = current = 0
    best_run = run = 0
    for d in days:
        if d["contributionCount"] > 0:
            run += 1
            best_run = max(best_run, run)
        else:
            run = 0
    # current streak = trailing run ending today
    for d in reversed(days):
        if d["contributionCount"] > 0:
            current += 1
        else:
            break
    return best_run, current


def draw_year_svg(days):
    ramp = " .`:-=+*cs#%@"
    cell = 11
    cols = len(days) // 7 + 1
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" font-family="monospace" font-size="{cell}">']
    for i, d in enumerate(days):
        col, row = divmod(i, 7)
        c = min(d["contributionCount"], 40)
        char = ramp[min(int(c / 40 * (len(ramp) - 1)), len(ramp) - 1)]
        x, y = col * cell, row * cell
        svg.append(f'<text x="{x}" y="{y + cell}" fill="#7C3AED">{char}</text>')
    svg.append("</svg>")
    with open("year.svg", "w") as f:
        f.write("\n".join(svg))


def draw_stats_svg(total, weeks):
    sparkline_points = []
    week_totals = [sum(d["contributionCount"] for d in w["contributionDays"]) for w in weeks]
    max_w = max(week_totals) or 1
    for i, w in enumerate(week_totals):
        x = i * (400 / len(week_totals))
        y = 60 - (w / max_w) * 50
        sparkline_points.append(f"{x:.1f},{y:.1f}")
    polyline = " ".join(sparkline_points)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="420" height="120">
  <text x="0" y="20" font-family="monospace" font-size="20" fill="#F8FAFC">{total} contributions</text>
  <polyline points="{polyline}" fill="none" stroke="#22D3EE" stroke-width="2"/>
</svg>'''
    with open("stats.svg", "w") as f:
        f.write(svg)


def draw_streak_svg(longest, current):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="300" height="100" font-family="monospace" fill="#F8FAFC">
  <text x="0" y="30" font-size="16">Current streak: {current} days</text>
  <text x="0" y="60" font-size="16">Longest streak: {longest} days</text>
</svg>'''
    with open("streak.svg", "w") as f:
        f.write(svg)


def draw_langs_svg(repos):
    totals = {}
    for r in repos:
        for edge in r["languages"]["edges"]:
            name = edge["node"]["name"]
            totals[name] = totals.get(name, 0) + edge["size"]
    total_size = sum(totals.values()) or 1
    top = sorted(totals.items(), key=lambda x: -x[1])[:6]
    rows = []
    for i, (name, size) in enumerate(top):
        pct = size / total_size * 100
        rows.append(f'<text x="0" y="{20 + i * 20}" font-family="monospace" font-size="13" fill="#F8FAFC">{name}: {pct:.1f}%</text>')
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="260" height="{20 + len(top) * 20}">{"".join(rows)}</svg>'
    with open("langs.svg", "w") as f:
        f.write(svg)


def main():
    user = fetch()
    cal = user["contributionsCollection"]["contributionCalendar"]
    days = [d for w in cal["weeks"] for d in w["contributionDays"]]
    longest, current = longest_and_current_streak(days)

    draw_year_svg(days)
    draw_stats_svg(cal["totalContributions"], cal["weeks"])
    draw_streak_svg(longest, current)
    draw_langs_svg(user["repositories"]["nodes"])


if __name__ == "__main__":
    main()
