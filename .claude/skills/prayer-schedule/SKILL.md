---
name: prayer-schedule
description: Check a class schedule against daily prayer times and put prayer blocks on the calendar. Use when someone shares a class schedule (screenshot, export, or Google Calendar) and wants to know where classes collide with Fajr, Dhuhr, Asr, Maghrib, Isha, or Jummah — or wants prayer time blocked off around their classes.
---

# Prayer & Class Schedule

Turn a class schedule plus a set of prayer times into a conflict report and a
set of calendar blocks.

## Inputs

Prayer times may arrive as a masjid screenshot, a pasted table, or text. Read
them as given — do not calculate or substitute your own times. If a time is
unreadable, ask rather than guess.

A class schedule may arrive as a planner screenshot, a pasted list, or events
already on the user's calendar. Each class needs: course code, days, start
time, end time. Ask for anything missing.

## Prayer windows

A prayer's window runs from its start time until the start of the next prayer.
Jummah replaces Dhuhr on Fridays and is treated as a fixed block — default
12:45–13:45 unless the user's masjid times say otherwise.

## Conflict rules

Classify every class against every prayer window:

- **Hard conflict** — the class overlaps the Jummah block, or the class covers
  a prayer's entire window so there is no time to pray in it.
- **Soft conflict** — the class overlaps part of a prayer window but leaves
  30+ minutes free inside that window, before or after class.
- **Clear** — no overlap.

Report only what the schedule shows. Do not rule on whether a prayer is valid,
whether combining is permitted, or which calculation method is correct — those
are questions for the user's imam, not this skill.

## Output format

Lead with a one-line verdict: the count of hard and soft conflicts.

Then a table, one row per conflict:

| Class | Day | Class time | Prayer | Window | Severity | Room to pray |

Then, for each hard conflict, one concrete suggestion — a different section, a
prayer before or after class, or a note that the class is simply unavoidable.

Keep it short. A schedule with no conflicts gets one line, not a table.

## Writing to the calendar

When asked to block prayer time, create one event per prayer per day using the
user's Google Calendar. Rules:

- Write to a dedicated calendar (default name: "Prayer") — never the user's
  primary calendar unless they say so.
- 20-minute blocks placed at the start of each prayer window, moved to the
  first clear 20 minutes if the window's start is inside a class.
- Skip any prayer whose entire window is covered by a hard conflict, and say
  which ones you skipped and why.
- Title format: `Fajr`, `Dhuhr`, `Asr`, `Maghrib`, `Isha`, `Jummah`.
- Confirm the date range with the user before writing anything. Show the list
  of events you are about to create and wait for a yes.

## Ramadan

If the user says they are in Ramadan, add two things to the report: classes
overlapping Maghrib (iftar), and classes starting before sunrise (suhoor
impact). Note them separately from the main conflict table.

## Accuracy notes

Prayer times shift daily. State the date range the times apply to, and say
plainly that blocks written for future weeks use the same times and will drift.
Eid dates are projections subject to moonsighting.
