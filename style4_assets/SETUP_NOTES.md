# Setup notes — Style 4 (profile-readme.guide format)

## What's in this folder

```
README_style4_profile_guide.md   <- rename to README.md in your profile repo
assets/                          <- all generated SVGs, dark + light pairs
.github/workflows/
  metrics.yml                    <- contribution calendar, auto-refreshes every 6h
  snake.yml                      <- contribution snake, auto-refreshes every 12h
```

## What auto-updates vs what's a one-time snapshot

**Auto-updating (real, working GitHub Actions):**
- `metrics.yml` uses `lowlighter/metrics`, a widely used, actively maintained Action.
  Runs in GitHub's own CI, not on someone's personal server, so it doesn't carry the
  same "free hosting went down" risk as the vercel.app badge widgets from your other
  READMEs.
- `snake.yml` uses `Platane/snk`, same deal, real GitHub Action, self-hosted output.

**Static snapshot (generated once, by me, right now):**
- `portrait-dark.svg` / `portrait-light.svg` — dot-matrix portrait from your photo
- `radar-dark.svg` / `radar-light.svg` — self-rated skill radar (values I set based
  on your resume, edit these if you disagree with yourself)
- `radar-langs-dark.svg` / `radar-langs-light.svg` — language radar. **This one is a
  placeholder estimate**, not pulled from your live GitHub API, since that requires a
  running script with a token. The percentages are based on languages visible in your
  resume, not actual byte counts from your repos.
- `stat-card-*.svg` and the four `card-*.svg` project cards — same story, generated
  once from your resume content, not wired to live data.

## Two setup steps required either way

1. **Settings → Actions → General → Workflow permissions → Read and write** — both
   workflows commit files back to your repo, this is off by default.
2. **Settings → Secrets and variables → Actions → New repository secret**, named
   exactly `METRICS_TOKEN`, a **classic** personal access token (not fine-grained)
   from github.com/settings/tokens with `read:user` scope. The metrics workflow reads
   profile-level data the default token can't see.

## If you want the radar/cards to actually auto-update

That requires real Python scripts (`radar.py`, `cards.py`) that call the GitHub API
and a third workflow to run them on a schedule, the kind of thing the original guide
describes. I generated the *output* of what those scripts would produce, but not the
scripts themselves, that's a heavier build. Say the word and I'll write them.
