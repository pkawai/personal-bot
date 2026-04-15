---
name: daily-briefing
description: Use this skill when the user says "good morning", "morning update", "daily briefing", "what's today", "start my day", or asks for a summary of the day. Activate on any greeting that implies the user is starting their day.
version: 1.0.0
---

# Daily Briefing Skill

Generate a personalized morning briefing combining today's date, live forex rates, and a motivational quote — all in one concise message.

## When to Use

Activate when the user sends:
- "good morning" or "gm"
- "daily briefing" or "morning update"
- "what's today?" or "start my day"
- Any morning greeting implying they want a daily overview

## Core Workflow

1. **Get current date and time** from system context. Format as: `Monday, April 14, 2026 — 9:15 AM`

2. **Fetch live EUR/USD rate** using WebFetch:
   - URL: `https://open.er-api.com/v6/latest/USD`
   - Extract: EUR rate, MNT rate, and `time_last_update_utc`

3. **Fetch a motivational quote** using WebFetch:
   - URL: `https://zenquotes.io/api/random`
   - Extract: `q` (quote text) and `a` (author)
   - If this fails, use a hardcoded fallback: *"The secret of getting ahead is getting started." — Mark Twain*

4. **Format the full briefing:**

   ```
   Good morning! ☀️

   📅 Monday, April 14, 2026 — 9:15 AM

   💱 Forex Snapshot
   1 USD = 0.9234 EUR
   1 USD = 3,450 MNT
   (rates as of [timestamp])

   💬 Quote of the Day
   "The secret of getting ahead is getting started."
   — Mark Twain

   Have a productive day!
   ```

5. Keep the entire response under 25 lines — it's a quick morning snapshot, not a report.

## Notes

- This skill chains two external data sources (forex + quotes) — if either fails, still deliver the briefing with what's available
- If the quote API fails, use the fallback quote
- If the forex API fails, omit the forex section and note "Live rates unavailable"
- Always include a warm, encouraging closing line
- Time zone: assume Ulaanbaatar time (UTC+8) unless the user specifies otherwise
