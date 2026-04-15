#!/usr/bin/env python3
"""
Todo manager helper script for the personal bot.
Manages tasks stored in data/todos.json.

Usage:
  python todos.py list
  python todos.py add "Buy groceries"
  python todos.py done 1
  python todos.py delete 1
"""

import json
import sys
from datetime import datetime
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent.parent.parent.parent / "data" / "todos.json"


def load_todos():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE) as f:
        return json.load(f)


def save_todos(todos):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(todos, f, indent=2)


def list_todos():
    todos = load_todos()
    if not todos:
        print("No tasks yet. Add one with: python todos.py add \"task name\"")
        return
    for i, todo in enumerate(todos, 1):
        status = "✓" if todo["done"] else "○"
        print(f"{i}. [{status}] {todo['text']}  (added {todo['added']})")


def add_todo(text):
    todos = load_todos()
    todos.append({
        "text": text,
        "done": False,
        "added": datetime.now().strftime("%Y-%m-%d")
    })
    save_todos(todos)
    print(f"Added: {text}")


def mark_done(index):
    todos = load_todos()
    if index < 1 or index > len(todos):
        print(f"Error: no task #{index}")
        sys.exit(1)
    todos[index - 1]["done"] = True
    save_todos(todos)
    print(f"Completed: {todos[index - 1]['text']}")


def delete_todo(index):
    todos = load_todos()
    if index < 1 or index > len(todos):
        print(f"Error: no task #{index}")
        sys.exit(1)
    removed = todos.pop(index - 1)
    save_todos(todos)
    print(f"Deleted: {removed['text']}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    command = sys.argv[1]

    if command == "list":
        list_todos()
    elif command == "add" and len(sys.argv) >= 3:
        add_todo(" ".join(sys.argv[2:]))
    elif command == "done" and len(sys.argv) == 3:
        mark_done(int(sys.argv[2]))
    elif command == "delete" and len(sys.argv) == 3:
        delete_todo(int(sys.argv[2]))
    else:
        print(__doc__)
        sys.exit(1)
