---
name: todo-manager
description: Use this skill when the user wants to manage their todo list or tasks. Trigger on "add task", "add todo", "remind me to", "show my tasks", "list todos", "what do I need to do", "mark done", "complete task", "finished task", "delete task", or "remove task".
version: 1.0.0
---

# Todo Manager Skill

Manage a personal todo list stored persistently in `data/todos.json`. Supports adding, listing, completing, and deleting tasks.

## When to Use

Activate when the user:
- Wants to add a task ("add task X", "remind me to X", "I need to X")
- Wants to see their tasks ("show todos", "list tasks", "what do I need to do")
- Wants to mark a task done ("mark #1 done", "complete task 2", "finished X")
- Wants to delete a task ("delete task 3", "remove task X")

## Core Workflow

### Adding a task

Run via Bash:
```bash
python ".claude/skills/todo-manager/scripts/todos.py" add "TASK_TEXT"
```
Replace `TASK_TEXT` with the task extracted from the user's message.

Respond: "Added to your list: **TASK_TEXT**"

### Listing tasks

Run via Bash:
```bash
python ".claude/skills/todo-manager/scripts/todos.py" list
```

Format the output as a clean list:
```
Your tasks:

○ 1. Buy groceries (added 2026-04-13)
✓ 2. Submit assignment (added 2026-04-12)
○ 3. Review PR #5 (added 2026-04-13)
```

If no tasks exist, say: "Your task list is empty. Add something with 'add task [name]'."

### Completing a task

First, list the tasks so the user can see the numbers, OR if the user specified a number, use it directly.

Run via Bash:
```bash
python ".claude/skills/todo-manager/scripts/todos.py" done TASK_NUMBER
```

Respond: "Completed: **TASK_TEXT**"

### Deleting a task

Run via Bash:
```bash
python ".claire/skills/todo-manager/scripts/todos.py" delete TASK_NUMBER
```

Respond: "Removed from your list: **TASK_TEXT**"

## Notes

- All commands must be run from the project root directory (where `data/todos.json` lives)
- Task numbers are 1-indexed
- If the user says a task name instead of a number (e.g. "mark 'buy groceries' done"), list first to find the number, then complete it
- Completed tasks stay in the list with a ✓ — they are not auto-deleted
- If the script fails, read `data/todos.json` directly and perform the operation manually using file editing tools
