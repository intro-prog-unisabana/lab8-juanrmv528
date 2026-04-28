"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md

import sys
from todo_manager import read_todo_file, write_todo_file
 
try:
    if len(sys.argv) < 2:
        raise IndexError("Insufficient arguments provided!")
 
    file_path = sys.argv[1]
 

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

    tasks = read_todo_file(file_path)
 
    if len(sys.argv) < 3:
        sys.exit(0)
 

    args = sys.argv[2:]  
    i = 0
    modified = False
 
    while i < len(args):
        command = args[i]
    
    if command == "view":
            print("Tasks:")
            for task in tasks:
                print(task)
            i += 1
 
    elif command == "add":
            if i + 1 >= len(args):
                raise IndexError('Task description required for "add".')
            task_desc = args[i + 1]
            tasks.append(task_desc)
            print(f'Task "{task_desc}" added.')
            modified = True
            i += 2