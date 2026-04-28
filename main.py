"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md

import sys
from todo_manager import read_todo_file, write_todo_file
 
try:
    # Verify at least one argument (file path) was provided
    if len(sys.argv) < 2:
        raise IndexError("Insufficient arguments provided!")
 
    file_path = sys.argv[1]
 
    # Handle --help flag
    if file_path == "--help":
        print("""Usage: python main.py <file_path> <command> [arguments]...
 
Commands:
  add "task"    - Add a task to the list.
  remove "task" - Remove a task from the list.
  view          - Display all tasks.
 
Examples:
  python main.py tasks.txt add "Buy groceries"
  python main.py tasks.txt remove "Do laundry"
  python main.py tasks.txt view
  python main.py tasks.txt add "Call mom" remove "Take out trash" view""")
        sys.exit(0)