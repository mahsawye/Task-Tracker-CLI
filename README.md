# Task-Tracker-CLI
A simple task management application to organize your work and track progress. Features task creation, status tracking, updating option, and Listing tasks.

https://roadmap.sh/projects/task-tracker

Requirements:
Python 3.x
No external libraries (uses only built-in modules: json, os, sys, datetime)


How to Run:
bashpython task_cli.py <command>

* Replace task_cli.py with your actual filename if it's different.

Available Commands:

Command            Example                                                 Description  
add                pythontask_cli.py add "Buy groceries"                   Add a new task
update             python task_cli.py update 1 "Buy groceries and cook"    Update a task'sdescription
delete              python task_cli.py delete 1                            Delete a task
mark-in-progress    python task_cli.py mark-in-progress 1                  Mark a task as in-progress
mark-done           python task_cli.py mark-done 1                         Mark a task as done
list                python task_cli.py list                                List all tasks
list todo           python task_cli.py list todo                           List only todo tasks
list in-progress    python task_cli.py list in-progress                    List only in-progress tasks
list done           python task_cli.py list done                           List only done tasks


Task Properties:
Each task saved in the JSON file has:
id — unique number, auto-assigned
description — text describing the task
status — one of todo, in-progress, done
createdAt — timestamp when created
updatedAt — timestamp when last modified


Example:
bashpython task_cli.py add "Learn Python classes"
# Task added successfully (ID: 1)

python task_cli.py mark-in-progress 1
python task_cli.py list in-progress


Notes:
The JSON file is created automatically the first time you run the app.
If you give an invalid task ID or missing arguments, the app prints a clear error message instead of crashing.
