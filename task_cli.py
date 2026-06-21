import json
import os
import sys
from datetime import datetime


class TaskTracker:
    def __init__(self):
        self.file = "tasks.json"
        if os.path.exists(self.file):
            with open(self.file, "r") as tasks_file:
                self.tasks = json.load(tasks_file)
        else:
            self.tasks = []

    def save(self):
        with open(self.file, "w") as tasks_file:
            json.dump(self.tasks, tasks_file, indent=2)

    def add_task(self, description):
        task = {
            "id": len(self.tasks) + 1,
            "description": description,
            "status": "todo",
            "createdAt": datetime.now().isoformat(),
            "updatedAt": datetime.now().isoformat(),
        }
        self.tasks.append(task)
        self.save()
        print(f"Task added successfully (ID: {task['id']})")

    def delete_task(self, task_id):
        original_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        if len(self.tasks) == original_count:
            print(f"Task {task_id} not found.")
            return
        self.save()
        print(f"Task deleted successfully (ID: {task_id})")

    def update_task(self, task_id, description):
        found = False
        for task in self.tasks:
            if task["id"] == task_id:
                task["description"] = description
                task["updatedAt"] = datetime.now().isoformat()
                found = True
        if not found:
            print(f"Task {task_id} not found.")
            return
        self.save()
        print(f"Task updated successfully (ID: {task_id})")

    def mark_in_progress_task(self, task_id):
        found = False
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = "in-progress"
                task["updatedAt"] = datetime.now().isoformat()
                found = True
        if not found:
            print(f"Task {task_id} not found.")
            return
        self.save()
        print(f"Task marked successfully (ID: {task_id})")

    def mark_done_task(self, task_id):
        found = False
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = "done"
                task["updatedAt"] = datetime.now().isoformat()
                found = True
        if not found:
            print(f"Task {task_id} not found.")
            return
        self.save()
        print(f"Task marked successfully (ID: {task_id})")


    def list_tasks(self, status=None):
        if status:
            filtered = [task for task in self.tasks if task["status"] == status]
        else:
            filtered = self.tasks

        if not filtered:
            print(f"No tasks found.")
            return

        for task in filtered:
            print(f"ID: {task['id']} | {task['description']} | {task['status']} | {task['createdAt']}")


def main():
    if len(sys.argv) < 2:
        print("Please provide a command: add, update, delete, mark-in-progress, mark-done, list")
        return

    tracker = TaskTracker()
    command = sys.argv[1]

    if command == "add":
        tracker.add_task(sys.argv[2])
    elif command == "delete":
        tracker.delete_task(int(sys.argv[2]))
    elif command == "update":
        tracker.update_task(int(sys.argv[2]), sys.argv[3])
    elif command == "mark-in-progress":
        tracker.mark_in_progress_task(int(sys.argv[2]))
    elif command == "mark-done":
        tracker.mark_done_task(int(sys.argv[2]))
    elif command == "list":
        if len(sys.argv) > 2:
            tracker.list_tasks(sys.argv[2])
        else:
            tracker.list_tasks()
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
