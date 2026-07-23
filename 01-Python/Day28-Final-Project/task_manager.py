"""Day 28 Final Project: Task Management CLI Application.

Features:
- Login
- Register
- Create Task
- Delete Task
- Search Task
- Due Date
- Priority
- Save JSON
- Logging
- Exception handling
- Type hints
- Dataclasses
"""

from __future__ import annotations

import json
import logging
import os
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import List, Optional


LOG_FILE = Path(__file__).with_name("task_manager.log")
DATA_FILE = Path(__file__).with_name("tasks.json")
USERS_FILE = Path(__file__).with_name("users.json")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(LOG_FILE), logging.StreamHandler()],
)


@dataclass
class Task:
    title: str
    description: str
    due_date: str
    priority: str
    completed: bool = False


@dataclass
class User:
    username: str
    password: str
    tasks: List[Task] = field(default_factory=list)


class TaskManager:
    def __init__(self) -> None:
        self.users: List[User] = []
        self.current_user: Optional[User] = None
        self.load_data()

    def load_data(self) -> None:
        try:
            if USERS_FILE.exists():
                with USERS_FILE.open("r", encoding="utf-8") as file:
                    raw_users = json.load(file)
                    self.users = [
                        User(
                            username=user["username"],
                            password=user["password"],
                            tasks=[Task(**task) for task in user.get("tasks", [])],
                        )
                        for user in raw_users
                    ]
            if DATA_FILE.exists():
                with DATA_FILE.open("r", encoding="utf-8") as file:
                    data = json.load(file)
                    if data:
                        logging.info("Loaded tasks from JSON")
        except FileNotFoundError:
            logging.warning("Data file not found; starting fresh")
        except json.JSONDecodeError as exc:
            logging.exception("Invalid JSON data: %s", exc)

    def save_data(self) -> None:
        try:
            with USERS_FILE.open("w", encoding="utf-8") as file:
                json.dump([asdict(user) for user in self.users], file, indent=2)
            with DATA_FILE.open("w", encoding="utf-8") as file:
                json.dump({"updated_at": datetime.now().isoformat()}, file, indent=2)
            logging.info("Data saved successfully")
        except OSError as exc:
            logging.exception("Could not save data: %s", exc)
            raise

    def register(self, username: str, password: str) -> None:
        if any(user.username == username for user in self.users):
            raise ValueError("Username already exists")
        new_user = User(username=username, password=password)
        self.users.append(new_user)
        self.current_user = new_user
        self.save_data()
        logging.info("User registered: %s", username)

    def login(self, username: str, password: str) -> None:
        for user in self.users:
            if user.username == username and user.password == password:
                self.current_user = user
                logging.info("User logged in: %s", username)
                return
        raise ValueError("Invalid username or password")

    def create_task(self, title: str, description: str, due_date: str, priority: str) -> None:
        if self.current_user is None:
            raise PermissionError("Please login first")
        task = Task(title=title, description=description, due_date=due_date, priority=priority)
        self.current_user.tasks.append(task)
        self.save_data()
        logging.info("Task created: %s", title)

    def delete_task(self, title: str) -> None:
        if self.current_user is None:
            raise PermissionError("Please login first")
        for task in self.current_user.tasks:
            if task.title == title:
                self.current_user.tasks.remove(task)
                self.save_data()
                logging.info("Task deleted: %s", title)
                return
        raise ValueError("Task not found")

    def search_task(self, keyword: str) -> List[Task]:
        if self.current_user is None:
            raise PermissionError("Please login first")
        result = [
            task for task in self.current_user.tasks
            if keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower()
        ]
        return result

    def show_tasks(self) -> None:
        if self.current_user is None:
            raise PermissionError("Please login first")
        if not self.current_user.tasks:
            print("No tasks yet.")
            return
        for task in self.current_user.tasks:
            print(f"- {task.title} | Priority: {task.priority} | Due: {task.due_date} | Completed: {task.completed}")


def main() -> None:
    manager = TaskManager()
    print("Task Management CLI")
    print("1. Register")
    print("2. Login")
    print("3. Create Task")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. View Tasks")
    print("7. Exit")

    while True:
        try:
            choice = input("Choose an option: ")
            if choice == "1":
                username = input("Username: ")
                password = input("Password: ")
                manager.register(username, password)
                print("Registered successfully")
            elif choice == "2":
                username = input("Username: ")
                password = input("Password: ")
                manager.login(username, password)
                print("Logged in successfully")
            elif choice == "3":
                title = input("Task title: ")
                description = input("Description: ")
                due_date = input("Due date (YYYY-MM-DD): ")
                priority = input("Priority (High/Medium/Low): ")
                manager.create_task(title, description, due_date, priority)
                print("Task created")
            elif choice == "4":
                title = input("Task title to delete: ")
                manager.delete_task(title)
                print("Task deleted")
            elif choice == "5":
                keyword = input("Search keyword: ")
                results = manager.search_task(keyword)
                for task in results:
                    print(task)
            elif choice == "6":
                manager.show_tasks()
            elif choice == "7":
                print("Goodbye")
                break
            else:
                print("Invalid option")
        except (ValueError, PermissionError) as exc:
            print(f"Error: {exc}")
            logging.exception("CLI error: %s", exc)
        except Exception as exc:
            print(f"Unexpected error: {exc}")
            logging.exception("Unexpected error: %s", exc)


if __name__ == "__main__":
    main()
