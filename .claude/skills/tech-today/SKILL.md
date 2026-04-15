---
name: tech-today
description: Use this skill when the user sends "techtoday", "tech today", "tech news", "what's happening in tech", "latest in AI", "tech digest", or asks for a summary of current technology news and trends around the world.
version: 1.0.0
---

# Tech Today Skill

Deliver a structured, up-to-date global tech news digest — covering breaking stories, AI developments, trending categories, and the most-talked-about subjects right now.

## When to Use

Activate on:
- `techtoday` or `tech today`
- "what's happening in tech?"
- "tech news", "tech digest", "tech update"
- "latest in AI", "AI news today"
- "what's trending in tech?"

## Core Workflow

### Step 1 — Run parallel searches

Search for the following **simultaneously** (run all 5 searches):

1. `latest tech news today {current year}` — general top stories
2. `artificial intelligence news today` — AI-specific developments
3. `trending technology topics this week` — what people are talking about
4. `big tech companies news today` — Apple, Google, Microsoft, Meta, OpenAI, etc.
5. `tech startups funding product launch today` — startup/product news

### Step 2 — Categorize what you find

Sort findings into these categories (skip any with no results):

| Category | What to include |
|----------|----------------|
| 🤖 **AI & Machine Learning** | Model releases, research papers, AI tools, LLM news |
| 📱 **Products & Launches** | New devices, apps, software releases |
| 💰 **Business & Funding** | Acquisitions, IPOs, funding rounds, layoffs |
| 🔬 **Science & Research** | Breakthroughs, new studies, academic findings |
| 🔒 **Security & Privacy** | Data breaches, vulnerabilities, policy changes |
| 🌍 **Industry & Policy** | Regulation, geopolitics, antitrust, government tech |

### Step 3 — Format the digest

Structure the response exactly like this:

```
📡 Tech Today — [Day, Date]

🔥 Top Story
[1-2 sentence summary of the single biggest story right now]

─────────────────────

🤖 AI & Machine Learning
• [Story headline] — [1 sentence summary]
• [Story headline] — [1 sentence summary]
• [Story headline] — [1 sentence summary]

📱 Products & Launches
• [Story headline] — [1 sentence summary]
• [Story headline] — [1 sentence summary]

💰 Business & Funding
• [Story headline] — [1 sentence summary]
• [Story headline] — [1 sentence summary]

[...other categories with content...]

─────────────────────

💬 Most Talked About
[3-5 bullet points of the biggest themes/topics people are discussing across tech right now]

🔗 Go deeper: [2-3 source links for the top story]
```

### Step 4 — Quality rules

- **Only include stories from the last 48 hours** — if a story is older, skip it
- **3 bullets per category max** — keep it scannable
- **No duplicate stories** across categories — each story appears once only
- **AI section always appears first** if it has content — it's the most relevant category
- **Top Story** must be the single most significant piece of news, not just the first result
- If a category has no fresh news, **omit it entirely** — don't pad with old stories

## Notes

- This skill is read on Telegram — keep total response under 50 lines
- Prioritize sources: TechCrunch, The Verge, Ars Technica, Wired, Reuters Tech, Bloomberg Tech
- If searches return mostly old content (>48h), note "News is quiet today — here's what's trending this week" and broaden to 7 days
- The user may also send `techtoday ai` to get only the AI section — in that case run only the AI search and return just that section
