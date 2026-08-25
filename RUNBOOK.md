# Live Demo Runbook
### Muslim Tech Collaborative · Claude Code Workshop
**Demo:** Build a real course planner that shows prayer-time conflicts while you're building your schedule — not after — then sync it to a real Google Calendar with prayer time blocked around it. Built with an MCP, a Skill, and Agents.

**How to read this:** anything in a `PASTE` block is typed or pasted verbatim into Claude Code. Nothing in a PASTE block needs editing except the one marked `← EDIT`. Everything outside those blocks is for you, not the terminal.

---

## Before anything: file names

Put this file in `~/mtc-demo/assets/` with exactly this name. The prompts below refer to it by name, so if you rename it the prompts break.

```
~/mtc-demo/
└── assets/
    └── prayer-times.png     ← screenshot of your masjid's prayer times
```

Launch Claude Code from `~/mtc-demo` so drag-and-drop and file references resolve:

```
cd ~/mtc-demo
claude
```

---

## Why this order: MCP → Skill → Agents

Your deck lists the concepts as MCPs, Agents, Skills. **Run the demo as MCP → Skill → Agents.** Phase 3 reuses the skill from Phase 2, and Phase 4 reuses both, so they have to come in this order. Say it out loud — *"we'll take these in build order"* — and the deck order still stands as reference.

Repeat this line at every phase transition:

> **MCP** = Claude can reach your stuff. **Skill** = Claude knows how *you* want it done. **Agent** = Claude does it many times at once.

---

## Phase 0 — Setup (~5 min)

Put the student list on a slide and let stragglers catch up during Phase 1.

**You (verified at home, on the demo laptop and network):**
- Claude Code installed, launched from `~/mtc-demo`
- Google Calendar MCP connected — one read *and* one write tested
- A throwaway Google account or a dedicated demo calendar — **not your real calendar**
- `assets/prayer-times.png` in place

**Students:**
- Claude Code installed
- Google Calendar connected
- Any prayer times screenshot (theirs, or share yours in the chat)

> ⚠️ Calendar MCP setup is the only step with no live recovery. Test it on the actual laptop and network you'll present on.

---

## Phase 1 — MCP: Connect the calendar (~5 min)

**Teaching point:** an MCP is how Claude reaches something outside the chat.

### 1.1 — Show it's connected

**PASTE:**
```
/mcp
```

Point at `google-calendar` in the list. Say: *"That line is the whole idea. Claude can now read and write my calendar the same way it could reach GitHub, Notion, or your company's database."*

### 1.2 — Prove it reads

**PASTE:**
```
What's on my calendar this week?
```

Say: *"I didn't paste anything in. It went and looked."*

### 1.3 — Prove it writes

**PASTE:**
```
Create a new calendar called "Fall Classes" — empty for now, we'll fill it once the planner is built.
```

Approve. **Switch to the browser and refresh Google Calendar.** The calendar exists.

That browser switch is the entire phase. Do it slowly.

**Fallback:** if the write fails, you still have 1.2. Say *"writes need scopes your admin controls — here's the shape of it"* and move on. Nothing downstream depends on this succeeding yet.

---

## Phase 2 — Skill: Teach Claude your standards (~9 min)

**Teaching point:** a skill is a folder with a markdown file in it.

### 2.1 — Show the problem first

Drag `assets/prayer-times.png` in, then paste:

**PASTE:**
```
These are my masjid's prayer times. I have a Tuesday/Thursday class 11:00am-12:20pm and a Friday discussion 12:30-1:20pm. Do either conflict?
```

You'll get a reasonable answer. **That's the point.** Say:

> *"That's fine. But it's fine today. Tomorrow I paste a different format and get a different answer, and my friend asking the same thing gets something else entirely. Nothing here knows what a hard conflict means to me, or that Jummah is different, or that I want twenty-minute blocks. Let me teach it once instead of explaining every time."*

### 2.2 — Create the skill

**PASTE:**
```
Create a skill called prayer-schedule that checks a class schedule against prayer times and blocks prayer time on my calendar.

Logic I want:
- A prayer's window runs from when it starts until the next prayer starts.
- Hard conflict: a class covers an entire prayer window with no time to pray, or a Friday class overlaps Jummah (12:45-1:45pm).
- Soft conflict: a class overlaps part of a window but leaves 30+ minutes free.
- Clear: no overlap.

Output: a one-line verdict with the conflict counts, then a table of conflicts, then one concrete suggestion for each hard conflict.

For calendar writes: 20-minute blocks at the start of each prayer window, on a separate calendar named "Prayer", never my primary. Always show me the events and wait for approval before creating them.

Read prayer times exactly as given - never calculate or substitute your own. Report scheduling conflicts only, never rulings on whether a prayer is valid or whether combining is allowed.
```

Then **open the generated `SKILL.md` and scroll it slowly on screen.** This is the moment of the whole workshop.

**PASTE:**
```
cat .claude/skills/prayer-schedule/SKILL.md
```

> *"That's the entire skill. Markdown. No code, no API, no framework. If you can write down how you want something done, you can write a skill."*

(A reference `SKILL.md` ships alongside this runbook — swap it in if the live generation comes out thin.)

### 2.3 — Run it

Clear first, so the skill has to trigger on its own description rather than leftover conversation:

**PASTE:**
```
/clear
```

Drag `assets/prayer-times.png` in again, then paste the exact same question from 2.1:

**PASTE:**
```
These are my masjid's prayer times. I have a Tuesday/Thursday class 11:00am-12:20pm and a Friday discussion 12:30-1:20pm. Do either conflict?
```

Watch the skill fire. Same question as 2.1, visibly different answer — a verdict line, a table, a concrete suggestion for the Friday hard conflict. Say it out loud: *"Same input. Same question. That's the skill."*

Close the phase: *"That's the rulebook written down. Next: build the actual tool a student would use, with these exact rules baked in."*

**Fallback:** if the skill doesn't auto-trigger after `/clear`, invoke it by name:

**PASTE:**
```
Use the prayer-schedule skill to check these classes against my masjid times.
```

Then teach the lesson: triggering depends on the description field. That's a real thing students need to know, not a failure.

---

## Phase 3 — Agents: Build the planner (~8 min)

**Teaching point:** agents don't just check work you already did — they build the thing, and they can split into specialized roles and work at the same time.

### 3.1 — Frame the real problem

Say: *"The skill checks a schedule someone hands it. But where does the schedule come from? Nobody plans their quarter by screenshotting it and asking an AI to review it after the fact. Let's build the actual planner — the tool where you build your schedule and see the prayer conflicts live, while you're still deciding."*

### 3.2 — Dispatch

Drag `assets/prayer-times.png` in, then paste:

**PASTE:**
```
Build BarakahPlan, a single-file HTML course planner for Muslim students. Launch three agents in parallel:
(1) generate a realistic sample UCSD course catalog as JSON, 30+ courses spanning many departments, searchable by code or title;
(2) write the conflict-detection module — reuse the exact same rules as the prayer-schedule skill (hard conflict, soft conflict, clear; Jummah as a hard block on Fridays) — reading prayer times from this screenshot;
(3) build the planner UI: weekly Mon-Fri grid with prayer times as horizontal bands, a searchable course sidebar to add/remove classes, and conflict badges on each class block that update live as classes are added.
Then integrate all three into barakahplan.html. Plain functional styling is fine.
```

Narrate while they run: *"Three workers, three different jobs, all at once — the catalog, the rulebook, the interface. Notice agent two isn't inventing conflict logic, it's translating the skill we already wrote."*

### 3.3 — Land it

Open `barakahplan.html`. Search for a course, add it to the schedule, watch a conflict badge appear live. Add the Friday discussion — the Jummah conflict fires the instant it's on the grid, not after the fact.

> *"Same rules as the skill, same prayer times as the calendar setup — now built into the tool itself. This is the thing a student actually uses, not a report about what they already did."*

**Fallback:** if an agent hangs, say what you'd do in real work — re-dispatch that one. A pre-built `barakahplan.html` ships in this repo on the `backup` branch: `git checkout backup -- barakahplan.html`.

---

## Phase 4 — Close: sync it back (~4 min)

Recap the through-line, then run one prompt that fires all three concepts together — the calendar from Phase 1, the skill from Phase 2, the planner from Phase 3.

**PASTE:**
```
Take the classes currently in my BarakahPlan schedule and add each one as a weekly recurring event on my Fall Classes calendar, running from September 21 to December 4, 2026. Show me the list first. Then use the prayer-schedule skill to block prayer time around them for the next two weeks.
```
`← EDIT the two dates to your actual quarter`

Approve both writes. **Switch to the browser.** Classes and prayer blocks both sit on the calendar now — built in the planner, checked by the skill, synced by the MCP.

Then hand it to the room: **take a feature request from the audience and run it live.** The demo has already succeeded, so the risk is free — and an unrehearsed request landing sells this better than anything scripted.

---

## All prompts in order (quick-copy strip)

Keep this open in a second window during the demo.

```
1.1   /mcp

1.2   What's on my calendar this week?

1.3   Create a new calendar called "Fall Classes" — empty for now, we'll fill it once the planner is built.

2.1   [drag assets/prayer-times.png]
      These are my masjid's prayer times. I have a Tuesday/Thursday class 11:00am-12:20pm and a Friday discussion 12:30-1:20pm. Do either conflict?

2.2   Create a skill called prayer-schedule that checks a class schedule against prayer times and blocks prayer time on my calendar.
      [full text in Phase 2.2 above]

      cat .claude/skills/prayer-schedule/SKILL.md

2.3   /clear
      [drag assets/prayer-times.png]
      These are my masjid's prayer times. I have a Tuesday/Thursday class 11:00am-12:20pm and a Friday discussion 12:30-1:20pm. Do either conflict?

3.2   [drag assets/prayer-times.png]
      Build BarakahPlan, a single-file HTML course planner for Muslim students. Launch three agents in parallel:
      [full text in Phase 3.2 above]

4     Take the classes currently in my BarakahPlan schedule and add each one as a weekly recurring event on my Fall Classes calendar, running from September 21 to December 4, 2026. Show me the list first. Then use the prayer-schedule skill to block prayer time around them for the next two weeks.
```

---

## Timing

| Phase | Time | Running |
|---|---|---|
| 0 — Setup | 5 min | 0:05 |
| 1 — MCP | 5 min | 0:10 |
| 2 — Skill | 9 min | 0:19 |
| 3 — Agents | 8 min | 0:27 |
| 4 — Close | 4 min | 0:31 |

Phase 2 is the heart. Running long? Trim the narration in Phase 3, or drop the audience request in Phase 4. Never compress Phase 2.

---

## For students following along

Slide this at the start:

1. Claude Code installed
2. Google Calendar connected — type `/mcp` to check
3. A prayer times screenshot (theirs, or share yours in the chat)

Tell them up front: *"If you fall behind, stop typing and watch. Every prompt is in the repo — you can redo this tonight in fifteen minutes."* Then actually ship the repo with this runbook in it.

---

## Two things to say once, on stage

- The skill reports **scheduling** conflicts, not rulings. It doesn't decide whether a prayer is valid, whether combining is permitted, or which calculation method is right. If a fiqh question comes up: *"the skill uses whatever times you give it — ask your imam, then configure accordingly."*
- Prayer times drift daily. Blocks written for future weeks use today's times. Worth one line in the demo, and it models the kind of caveat good engineering includes.

---

## Pre-demo checklist

- [ ] Google Calendar MCP tested — one read, one write, on the demo laptop and network
- [ ] Demo calendar created and empty; real calendar not connected
- [ ] `assets/prayer-times.png` in place
- [ ] Dates in the Phase 4 prompt edited to your actual quarter
- [ ] Reference `SKILL.md` on hand in case live generation is thin
- [ ] Pre-built `barakahplan.html` on the `backup` branch in case Phase 3 stumbles
- [ ] Full dry run completed and timed
- [ ] Terminal ≥ 18pt, browser at 125% zoom, calendar tab open and logged in
- [ ] Quick-copy strip open in a second window
- [ ] Hotspot ready
- [ ] Repo public, QR code on the closing slide
