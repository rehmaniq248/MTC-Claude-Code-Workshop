# Live Demo Runbook
### Muslim Tech Collaborative · Claude Code Workshop
**Demo:** Take a tentative class schedule, find where it collides with prayer times, and put prayer blocks on a real Google Calendar — using an MCP, a Skill, and Agents.

**How to read this:** anything in a `PASTE` block is typed or pasted verbatim into Claude Code. Nothing in a PASTE block needs editing except the two marked `← EDIT`. Everything outside those blocks is for you, not the terminal.

---

## Before anything: file names

Put these four files in `~/mtc-demo/` and use exactly these names. Every prompt below refers to them by name, so if you rename them the prompts break.

```
~/mtc-demo/
├── prayer-times.png     ← screenshot of your masjid's monthly times
├── schedule-a.png       ← candidate schedule 1 from the course planner
├── schedule-b.png       ← candidate schedule 2
└── schedule-c.png       ← candidate schedule 3
```

Launch Claude Code from that folder so drag-and-drop and file references resolve:

```
cd ~/mtc-demo
claude
```

---

## Why this order: MCP → Skill → Agents

Your deck lists the concepts as MCPs, Agents, Skills. **Run the demo as MCP → Skill → Agents.** Phase 3 reuses the skill from Phase 2, so agents have to come last. Say it out loud — *"we'll take these in build order"* — and the deck order still stands as reference.

Repeat this line at every phase transition:

> **MCP** = Claude can reach your stuff. **Skill** = Claude knows how *you* want it done. **Agent** = Claude does it many times at once.

---

## Phase 0 — Setup (~5 min)

Put the student list on a slide and let stragglers catch up during Phase 1.

**You (verified at home, on the demo laptop and network):**
- Claude Code installed, launched from `~/mtc-demo`
- Google Calendar MCP connected — one read *and* one write tested
- A throwaway Google account or a dedicated demo calendar — **not your real calendar**
- All four files above, named exactly

**Students:**
- Claude Code installed
- Google Calendar connected
- Any class schedule, real or invented

> ⚠️ Calendar MCP setup is the only step with no live recovery. Test it on the actual laptop and network you'll present on.

---

## Phase 1 — MCP: Connect the calendar (~6 min)

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

Drag `schedule-a.png` into the terminal window first, then paste:

**PASTE:**
```
This is my tentative class schedule from my course planner. Read the classes off it and create a new calendar called "Fall Classes", then add each class as a weekly recurring event running from September 21 to December 4, 2026. Show me the full list of events before you create anything.
```
`← EDIT the two dates to your actual quarter`

Approve when it shows the list. **Switch to the browser and refresh Google Calendar.** The classes are there.

That browser switch is the entire phase. Do it slowly.

**Fallback:** if the write fails, you still have 1.2. Say *"writes need scopes your admin controls — here's the shape of it"* and move on. Nothing downstream depends on this succeeding.

---

## Phase 2 — Skill: Teach Claude your standards (~9 min)

**Teaching point:** a skill is a folder with a markdown file in it.

### 2.1 — Show the problem first

Drag `prayer-times.png` in, then paste:

**PASTE:**
```
These are my masjid's prayer times. Do any of my classes conflict with them?
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

Drag `prayer-times.png` in again, then paste:

**PASTE:**
```
These are my masjid's prayer times. Check them against my Fall Classes calendar.
```

Watch the skill fire. Same question as 2.1, visibly different answer. Say it out loud: *"Same input. Same question. That's the skill."*

### 2.4 — Write it back

**PASTE:**
```
Block prayer time around my classes for the next two weeks.
```

Approve the list. **Switch to the browser again.** Prayer blocks now sit between the classes.

Close the phase: *"MCP got Claude to my calendar. The skill taught it my rules. Neither is impressive alone — together it's a tool I'd use every quarter."*

**Fallback:** if the skill doesn't auto-trigger after `/clear`, invoke it by name:

**PASTE:**
```
Use the prayer-schedule skill to check my masjid times against my Fall Classes calendar.
```

Then teach the lesson: triggering depends on the description field. That's a real thing students need to know, not a failure.

---

## Phase 3 — Agents: Do it many times at once (~6 min)

**Teaching point:** you stop doing the work and start assigning it.

### 3.1 — Frame the real problem

Say: *"Here's what actually happens during enrollment. You don't have one schedule. You have three, you're deciding between them, and WebReg is about to eat two of them."*

### 3.2 — Dispatch

Drag in all three: `schedule-a.png`, `schedule-b.png`, `schedule-c.png`, plus `prayer-times.png`. Then paste:

**PASTE:**
```
I'm deciding between these three possible schedules. Launch three agents in parallel, one per schedule. Each agent should use the prayer-schedule skill to check its schedule against my masjid's prayer times and report the conflicts it finds. When all three finish, compare them and tell me which schedule is the most prayer-friendly and why.
```

Narrate while they run: *"Three workers, three separate contexts, all at once. Serially that's three conversations and ten minutes. Here it's one instruction."*

### 3.3 — Land it

When the comparison returns: *"Notice every agent used the skill. Skills and agents compose — I wrote my rules down once and three workers all followed them. That's the architecture."*

**Fallback:** if an agent hangs, say what you'd do in real work — re-dispatch that one — and compare the two that finished. Partial results still teach it.

---

## Phase 4 — Close (~3 min)

Recap the through-line, then run one prompt that fires all three concepts at once:

**PASTE:**
```
Add a Jummah event every Friday from 12:45 to 1:45pm for the rest of the quarter, and tell me which of my classes I'd need to move.
```

Then hand it to the room: **take a feature request from the audience and run it live.** The demo has already succeeded, so the risk is free — and an unrehearsed request landing sells this better than anything scripted.

---

## All prompts in order (quick-copy strip)

Keep this open in a second window during the demo.

```
1.1   /mcp

1.2   What's on my calendar this week?

1.3   [drag schedule-a.png]
      This is my tentative class schedule from my course planner. Read the classes off it and create a new calendar called "Fall Classes", then add each class as a weekly recurring event running from September 21 to December 4, 2026. Show me the full list of events before you create anything.

2.1   [drag prayer-times.png]
      These are my masjid's prayer times. Do any of my classes conflict with them?

2.2   Create a skill called prayer-schedule that checks a class schedule against prayer times and blocks prayer time on my calendar.
      [full text in Phase 2.2 above]

      cat .claude/skills/prayer-schedule/SKILL.md

2.3   /clear
      [drag prayer-times.png]
      These are my masjid's prayer times. Check them against my Fall Classes calendar.

2.4   Block prayer time around my classes for the next two weeks.

3.2   [drag schedule-a.png, schedule-b.png, schedule-c.png, prayer-times.png]
      I'm deciding between these three possible schedules. Launch three agents in parallel, one per schedule. Each agent should use the prayer-schedule skill to check its schedule against my masjid's prayer times and report the conflicts it finds. When all three finish, compare them and tell me which schedule is the most prayer-friendly and why.

4     Add a Jummah event every Friday from 12:45 to 1:45pm for the rest of the quarter, and tell me which of my classes I'd need to move.
```

---

## Timing

| Phase | Time | Running |
|---|---|---|
| 0 — Setup | 5 min | 0:05 |
| 1 — MCP | 6 min | 0:11 |
| 2 — Skill | 9 min | 0:20 |
| 3 — Agents | 6 min | 0:26 |
| 4 — Close | 3 min | 0:29 |

Phase 2 is the heart. Running long? Cut Phase 3 to one agent, or drop the audience request. Never compress Phase 2.

---

## For students following along

Slide this at the start:

1. Claude Code installed
2. Google Calendar connected — type `/mcp` to check
3. A prayer times screenshot (theirs, or share yours in the chat)
4. Any class schedule, real or invented

Tell them up front: *"If you fall behind, stop typing and watch. Every prompt is in the repo — you can redo this tonight in fifteen minutes."* Then actually ship the repo with this runbook in it.

---

## Two things to say once, on stage

- The skill reports **scheduling** conflicts, not rulings. It doesn't decide whether a prayer is valid, whether combining is permitted, or which calculation method is right. If a fiqh question comes up: *"the skill uses whatever times you give it — ask your imam, then configure accordingly."*
- Prayer times drift daily. Blocks written for future weeks use today's times. Worth one line in the demo, and it models the kind of caveat good engineering includes.

---

## Pre-demo checklist

- [ ] Google Calendar MCP tested — one read, one write, on the demo laptop and network
- [ ] Demo calendar created and empty; real calendar not connected
- [ ] All four files in `~/mtc-demo/` with exact names
- [ ] Dates in prompt 1.3 edited to your actual quarter
- [ ] Reference `SKILL.md` on hand in case live generation is thin
- [ ] Full dry run completed and timed
- [ ] Terminal ≥ 18pt, browser at 125% zoom, calendar tab open and logged in
- [ ] Quick-copy strip open in a second window
- [ ] Hotspot ready
- [ ] Repo public, QR code on the closing slide
