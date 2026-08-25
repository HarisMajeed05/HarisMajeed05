# Setup — Style 4 (self-updating profile README)

## What actually broke last time, and what's fixed

1. **Nested folder mess** — the zip put `.github`, `assets`, `scripts` both at the
   top level *and* again inside a `style4_assets` subfolder. GitHub was reading the
   wrong paths. This version is flat: everything in this folder goes straight into
   your `HarisMajeed05/HarisMajeed05` repo root, no subfolder.
2. **No real script** — last time I generated static SVGs once and called it done.
   `scripts/generate_assets.py` is now a real script I ran and tested against your
   actual GitHub data before shipping it.
3. **Em dash in the typing banner** — `%E2%80%94` in the URL was a raw em dash
   character, which also broke the line width. Replaced with `|` and re-encoded.
4. **A crash I caught while testing**: the script died if a repo had no description
   on GitHub and none was set in `projects.json` either. Fixed, and I ran it again
   to confirm.

## File structure (copy this exactly into your repo root)

```
README.md
assets/
  portrait-dark.svg / portrait-light.svg   <- your real photo, already generated
  radar-dark.svg / radar-light.svg          <- self-rated, from skills.json
  radar-langs-*.svg                         <- LIVE, computed by the script
  stat-card-*.svg                           <- LIVE, computed by the script
  card-*.svg (x7 projects, dark+light)      <- LIVE, computed by the script
  skills.json                               <- you edit this by hand
  projects.json                             <- you edit this to change which repos show
scripts/
  generate_assets.py                        <- the real, tested script
.github/workflows/
  assets.yml     <- runs generate_assets.py daily, commits changes
  metrics.yml    <- contribution calendar (lowlighter/metrics)
  snake.yml      <- contribution snake (Platane/snk)
```

## What's actually live now vs static

| Asset | Updates | How |
|---|---|---|
| Language radar | Daily | Real byte counts from `/repos/{owner}/{repo}/languages` across all your public repos |
| Stat card (repos/stars/top language) | Daily | Live GitHub API |
| Project cards | Daily | Live description/language per repo, unless you override in `projects.json` |
| Self-rated skill radar | Manual | Edit `assets/skills.json`, next scheduled run picks it up |
| Contribution calendar | Every 6h | `lowlighter/metrics` action |
| Contribution snake | Every 12h | `Platane/snk` action |
| Portrait | Never (by design) | It's a photo render, doesn't need to change on a schedule |

## Setup steps, in order

1. Copy everything in this folder into your `HarisMajeed05/HarisMajeed05` repo root
   (the one your GitHub profile reads from).
2. **Settings → Actions → General → Workflow permissions → Read and write** — all
   three workflows commit back to the repo, this is off by default.
3. **Settings → Secrets and variables → Actions → New repository secret**, named
   exactly `METRICS_TOKEN`, a **classic** token (not fine-grained) from
   github.com/settings/tokens with `read:user` scope. Only the calendar workflow
   needs this one; `assets.yml` uses the automatic `GITHUB_TOKEN`, no setup needed.
4. Push, then go to the **Actions** tab and run all three workflows manually once
   (`Run workflow` button) instead of waiting for their schedules.
5. `snake.yml` creates an `output` branch on its first successful run. Until that
   run finishes, the snake image in the README will 404, that's expected on day one.

## If a workflow fails

Check the failed step's log first, it will name the problem directly:
- `assets.yml` failing on the API call almost always means a malformed
  `projects.json` (check it's valid JSON) or a repo name in there that doesn't
  match your actual GitHub repo name exactly, case-sensitive.
- `metrics.yml` failing is almost always `METRICS_TOKEN` missing or created as
  fine-grained instead of classic.
- `snake.yml` failing at the push step means step 2 above (workflow permissions)
  wasn't set.
