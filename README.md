# Claude Code Workshop — Prayer & Class Schedule Demo
### Muslim Tech Collaborative · UC San Diego

A hands-on demo of three Claude Code concepts, built around one real problem: your class schedule collides with prayer times, and you want it on your calendar.

> **MCP** = Claude can reach your stuff. **Skill** = Claude knows how *you* want it done. **Agent** = Claude does it many times at once.

## What's here

```
.claude/skills/prayer-schedule/SKILL.md   the skill we build during the workshop
RUNBOOK.md                                every prompt, in order
assets/                                   drop your screenshots here
```

## Redo it yourself (~15 minutes)

1. Install Claude Code and connect Google Calendar. Check with `/mcp`.
2. Clone this repo and `cd` into it.
3. Drop into `assets/`: a screenshot of your masjid's prayer times, and one to three class schedules from your course planner. Use the names listed in `assets/README.md`.
4. Open `RUNBOOK.md` and run the prompts in order.

The skill in `.claude/skills/` is the finished version. If you want the full experience, delete it and build it yourself at Phase 2 — that's the part worth doing by hand.

## Notes

This checks **scheduling** conflicts, not rulings. It uses whatever prayer times you give it and doesn't decide whether a prayer is valid or whether combining is permitted — ask your imam, then configure accordingly.

Prayer times shift daily. Calendar blocks written for future weeks use today's times and will drift.
