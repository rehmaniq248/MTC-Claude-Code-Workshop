# BarakahPlan Demo Kit
### Muslim Tech Collaborative · Claude Code Workshop

Everything that must exist **before** the demo starts. Everything else —
the planner itself — gets built live in Claude Code (that's the show).

```
barakahplan-demo-kit/
├── mcp-server/
│   ├── prayer_mcp.py        ← the ~40-line MCP server you show on screen
│   └── requirements.txt
├── .claude/
│   └── skills/
│       └── ui-design/
│           └── SKILL.md     ← your UI prompt kit, packaged as a skill
├── fallback/
│   └── prayer_data.json     ← wifi-failure insurance (same shape as the MCP output)
└── README.md
```

---

## One-time setup (do at home, before the dry run)

```bash
cd barakahplan-demo-kit
pip install -r mcp-server/requirements.txt

# Register the MCP server with Claude Code (project scope):
claude mcp add prayer-times -- python3 mcp-server/prayer_mcp.py

# Launch Claude Code and confirm:
claude
> /mcp        # should list: prayer-times ✔ connected
> /skills     # (or check settings) should show: ui-design
```

⚠️ The server compiles and loads, but the live Aladhan API call was **not**
tested from the sandbox it was written in — run `get_prayer_times` once at
home to confirm end-to-end, and refresh `fallback/prayer_data.json` with real
output the morning of the demo.

---

## The three stage prompts

### Phase 1 — MCP (~5 min)
Open `mcp-server/prayer_mcp.py` on screen first. Say: *"This is the entire
server. Forty lines. Claude wrote it in one prompt."* Then:

> Using the prayer-times MCP, get today's prayer times for San Diego and
> convert today's date to Hijri. Save the combined result as
> `prayer_data.json` — we'll build our planner on top of it. Also include a
> Jummah block for Fridays, 12:45–13:45.

**If the live call fails:** `cp fallback/prayer_data.json .` and say "this is
exactly what the tool returns" — keep moving.

### Phase 2 — Agents (~7 min)

> Build BarakahPlan, a single-file HTML course planner for Muslim students —
> think WebReg's course planner, not a fixed list.
> Launch three parallel agents:
> (1) generate a realistic UCSD sample course catalog as JSON, 30+ courses
> spanning many departments (CSE, MATH, ECON, HIST, LIGN, VIS, PHIL, BILD,
> CHEM, POLI, etc.) with a course code, title, days, and time each — include
> one Friday 12:30–13:20 discussion, one class overlapping Asr, one
> 19:00–20:50 evening lab, and the rest clean classes spread across the day;
> (2) write the conflict-detection module using prayer_data.json — a hard red
> flag for Friday classes overlapping the Jummah block, yellow for classes
> overlapping a prayer time but leaving room to pray in its window, and a
> Ramadan mode that flags classes overlapping Maghrib/iftar; also detect Eid
> days from the Hijri data with a "projected — subject to moonsighting" note;
> (3) build the planner UI — weekly Mon–Fri grid 8:00–22:00, prayer times as
> horizontal bands across the grid, a WebReg-style course sidebar (search by
> code or title to filter the catalog, add/remove from the schedule), and
> red/yellow/green conflict badges on each class block.
> Then integrate all three into `barakahplan.html`. Plain functional styling
> only — we'll design it in the next step. Do NOT use the ui-design skill yet.

*(The "do NOT use the skill yet" line matters — it protects your Phase 3
before/after reveal.)*

Demo on the plain version: drop the Friday class → Jummah flag fires. Toggle
Ramadan mode → evening lab flags.

### Phase 3 — Skill (~6 min)
Open `.claude/skills/ui-design/SKILL.md` and scroll it. Say: *"A skill is a
folder with a markdown file. That's it. Your best prompt, saved forever."*
Then:

> Using the ui-design skill, restyle barakahplan.html into
> barakahplan-styled.html. Keep every feature and behavior identical.

Open both side by side. Re-fire one conflict on the styled version.

---

## Rehearsal = backup generation

Run the full three-phase script at home once. The dry run **produces your
backup files**: commit the generated `barakahplan.html` and
`barakahplan-styled.html` to a `backup` branch. On stage, if Phase 2 or 3
stumbles: `git checkout backup -- barakahplan-styled.html` and say "here's
the same command, run this morning."

## Pre-demo checklist

- [ ] `claude mcp list` shows prayer-times; live tool call tested end-to-end
- [ ] `fallback/prayer_data.json` refreshed morning-of
- [ ] Dry run completed; backup branch committed
- [ ] Terminal ≥ 18pt, browser at 125% zoom
- [ ] Hotspot ready as wifi backup
- [ ] QR code to this repo on the closing slide
- [ ] Timed: full run ≤ 22 min leaving room for Q&A + one live audience feature

## Respect notes (worth saying once on stage)

- The app treats prayer times as *scheduling data*, not rulings. Calculation
  method and Asr madhab are config flags on the API — "ask your local imam,
  configure accordingly."
- Eid/Ramadan dates are projections; the UI carries a moonsighting note.
