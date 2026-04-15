# Personal Bot — Project 2

**Course:** AI-First Agentic Development — AUM  
**Path:** A (Claude Channels + Telegram)  
**Platform:** Telegram  

A personal assistant bot powered by Claude Code skills, accessible via Telegram. Send a message and Claude handles it using custom-built skills — no traditional bot server required.

---

## How It Works

```
You send a message on Telegram
        ↓
Claude Channels routes it to Claude Code (running locally)
        ↓
Claude matches the message to a skill
        ↓
Skill executes (web fetch, file read/write, search)
        ↓
Response sent back to you on Telegram
```

---

## Skills

### 1. Forex Rates
Look up live foreign exchange rates with no API key needed.

| Trigger | Example |
|---------|---------|
| Exchange rate queries | "what's EUR/USD?" |
| Currency conversion | "USD to MNT rate" |
| General rates | "show forex rates" |

**Example response:**
```
Exchange Rates (base: USD)
Updated: Mon, 14 Apr 2026 08:00:01 UTC

EUR  0.9234
MNT  3,450.00
GBP  0.7891
JPY  149.32
CNY  7.24
```

---

### 2. Todo Manager
Manage a personal task list stored persistently in `data/todos.json`.

| Trigger | Example |
|---------|---------|
| Add a task | "add task review PR #5" |
| List tasks | "show my todos" |
| Complete a task | "mark task 1 done" |
| Delete a task | "delete task 2" |

**Example response:**
```
Your tasks:

○ 1. Review PR #5 (added 2026-04-13)
○ 2. Finish capstone EDA (added 2026-04-13)
✓ 3. Submit project proposal (added 2026-04-10)
```

---

### 3. Web Search
Search the web for any topic and get a concise summary with sources.

| Trigger | Example |
|---------|---------|
| Search | "search for XGBoost hyperparameters" |
| Look up | "look up Railway.app pricing" |
| Research | "research Mongolian fintech startups" |

**Example response:**
```
🔍 Search: XGBoost hyperparameters

**Summary**
XGBoost key hyperparameters include learning_rate, max_depth, n_estimators...

**Key Points**
• learning_rate (0.01–0.3): controls step size
• max_depth (3–10): tree complexity
• subsample (0.5–1.0): row sampling per tree

**Sources**
• XGBoost Documentation (xgboost.readthedocs.io)
• Towards Data Science — XGBoost Guide
```

---

### 5. Tech Today *(stretch)*
Get a structured global tech news digest — latest stories, AI developments, trending categories, and most-talked subjects right now.

| Trigger | Example |
|---------|---------|
| Keyword | `techtoday` |
| Natural phrase | "what's happening in tech?" |
| AI-only variant | `techtoday ai` |

**Example response:**
```
📡 Tech Today — Tuesday, April 15, 2026

🔥 Top Story
OpenAI announces GPT-5 with real-time voice and vision capabilities,
available to all ChatGPT users starting today.

─────────────────────

🤖 AI & Machine Learning
• GPT-5 launches globally — major leap in reasoning and multimodal tasks
• Google DeepMind releases AlphaFold 3 update with drug discovery focus
• Mistral open-sources new 70B model outperforming Llama 3

📱 Products & Launches
• Apple releases iOS 19.4 with satellite messaging improvements
• Notion launches AI database with auto-tagging and summarization

💰 Business & Funding
• Perplexity AI raises $250M at $3B valuation
• Intel announces 2,000 layoffs amid fab restructuring

─────────────────────

💬 Most Talked About
• AI agents replacing SaaS workflows
• Open-source vs closed model debate heating up
• EU AI Act enforcement deadline approaching

🔗 Go deeper: TechCrunch · The Verge · Ars Technica
```

---

### 4. Daily Briefing *(stretch)*
Start your day with a combined morning brief — date, forex snapshot, and a motivational quote.

| Trigger | Example |
|---------|---------|
| Morning greeting | "good morning" |
| Daily update | "daily briefing" |
| Start of day | "what's today?" |

**Example response:**
```
Good morning! ☀️

📅 Monday, April 14, 2026 — 9:15 AM

💱 Forex Snapshot
1 USD = 0.9234 EUR
1 USD = 3,450 MNT

💬 Quote of the Day
"The secret of getting ahead is getting started."
— Mark Twain

Have a productive day!
```

---

## Setup Instructions

### Prerequisites
- [Claude Code](https://claude.ai/download) installed and authenticated
- A Telegram account

### Step 1: Create your Telegram bot
1. Open Telegram and message [@BotFather](https://t.me/botfather)
2. Send `/newbot` and follow the prompts
3. Copy the **bot token** BotFather gives you

### Step 2: Clone this repo
```bash
git clone https://github.com/pkawai/personal-bot.git
cd personal-bot
```

### Step 3: Install the Telegram plugin
Open a Claude Code session and run:
```
/plugin install telegram@claude-plugins-official
/reload-plugins
```

### Step 4: Configure the bot token
```
/telegram:configure YOUR_BOT_TOKEN_HERE
```

### Step 5: Start Claude with the Telegram channel
```bash
claude --channels plugin:telegram@claude-plugins-official
```

Or use the alias (add to `~/.zshrc`):
```bash
alias mybot="cd /path/to/personal-bot && claude --channels plugin:telegram@claude-plugins-official"
```

### Step 6: Pair your Telegram account
1. DM your bot on Telegram — it replies with a 6-character code
2. In your Claude Code session:
```
/telegram:access pair <code>
```

### Step 7: Test the skills
Send these messages to your bot:
- `what's EUR/USD?` → live exchange rates
- `add task test the bot` → task added to your list
- `search for Claude Code channels` → web summary
- `good morning` → daily briefing
- `techtoday` → global tech news digest

---

## Project Structure

```
personal-bot/
├── .claude/
│   └── skills/
│       ├── forex-rates/
│       │   └── SKILL.md          # Exchange rate lookup skill
│       ├── todo-manager/
│       │   ├── SKILL.md          # Task management skill
│       │   └── scripts/
│       │       └── todos.py      # Python helper for todo CRUD
│       ├── web-search/
│       │   └── SKILL.md          # Web research skill
│       ├── daily-briefing/
│       │   └── SKILL.md          # Morning briefing skill (stretch)
│       └── tech-today/
│           └── SKILL.md          # Global tech news digest (stretch)
├── data/
│   └── todos.json                # Persistent task storage
├── .gitignore
└── README.md
```

---

## Git Workflow

This project uses feature branches and git worktrees for parallel skill development.

```bash
# Worktrees used during development
git worktree add ../personal-bot-todo feature/todo-manager-skill
git worktree add ../personal-bot-search feature/web-search-skill
```

Each skill was developed on its own branch with a corresponding GitHub issue:
- `feature/forex-rates-skill` → Issue #1
- `feature/todo-manager-skill` → Issue #2
- `feature/web-search-skill` → Issue #3
- `feature/daily-briefing-skill` → Issue #4
- `feature/tech-today-skill` → Issue #9
