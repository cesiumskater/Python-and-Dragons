"""
Task Manager CLI - Portfolio Project
A professional command-line task management system

Skills Demonstrated:
- File I/O with JSON
- Argument parsing (argparse)
- Data structures (lists, dictionaries)
- Error handling
- User input validation
- Professional code organization

Author: Your Name
GitHub: https://github.com/yourusername/task-manager-cli
"""

import json
import os
import argparse
from datetime import datetime
from typing import List, Dict, Optional


class TaskManager:
    """Manages tasks with persistent storage"""

    def __init__(self, filename: str = "tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self) -> List[Dict]:
        """Load tasks from JSON file"""
        if not os.path.exists(self.filename):
            return []

        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"Warning: {self.filename} is corrupted. Starting fresh.")
            return []
        except Exception as e:
            print(f"Error loading tasks: {e}")
            return []

    def save_tasks(self) -> bool:
        """Save tasks to JSON file"""
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.tasks, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving tasks: {e}")
            return False

    def add_task(self, description: str, priority: str = "medium") -> Dict:
        """Add a new task"""
        task = {
            "id": len(self.tasks) + 1,
            "description": description,
            "priority": priority.lower(),
            "completed": False,
            "created": datetime.now().isoformat(),
            "completed_at": None
        }
        self.tasks.append(task)
        self.save_tasks()
        return task

    def list_tasks(self, show_completed: bool = False, priority: Optional[str] = None) -> List[Dict]:
        """List tasks with optional filtering"""
        filtered = self.tasks

        if not show_completed:
            filtered = [t for t in filtered if not t['completed']]

        if priority:
            filtered = [t for t in filtered if t['priority'] == priority.lower()]

        return filtered

    def complete_task(self, task_id: int) -> bool:
        """Mark a task as completed"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                task['completed_at'] = datetime.now().isoformat()
                self.save_tasks()
                return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """Delete a task"""
        initial_count = len(self.tasks)
        self.tasks = [t for t in self.tasks if t['id'] != task_id]

        if len(self.tasks) < initial_count:
            self.save_tasks()
            return True
        return False

    def update_task(self, task_id: int, description: Optional[str] = None,
                    priority: Optional[str] = None) -> bool:
        """Update task description or priority"""
        for task in self.tasks:
            if task['id'] == task_id:
                if description:
                    task['description'] = description
                if priority:
                    task['priority'] = priority.lower()
                self.save_tasks()
                return True
        return False

    def get_stats(self) -> Dict:
        """Get task statistics"""
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t['completed'])
        pending = total - completed

        priority_counts = {
            'high': sum(1 for t in self.tasks if t['priority'] == 'high' and not t['completed']),
            'medium': sum(1 for t in self.tasks if t['priority'] == 'medium' and not t['completed']),
            'low': sum(1 for t in self.tasks if t['priority'] == 'low' and not t['completed'])
        }

        return {
            'total': total,
            'completed': completed,
            'pending': pending,
            'by_priority': priority_counts
        }


def display_tasks(tasks: List[Dict]):
    """Display tasks in a formatted table"""
    if not tasks:
        print("\nNo tasks found.")
        return

    print(f"\n{'ID':<5} {'Status':<10} {'Priority':<10} {'Description':<40}")
    print("-" * 70)

    for task in tasks:
        status = "✓ Done" if task['completed'] else "○ Pending"
        priority = task['priority'].capitalize()
        desc = task['description'][:37] + "..." if len(task['description']) > 40 else task['description']

        print(f"{task['id']:<5} {status:<10} {priority:<10} {desc:<40}")

    print()


def main():
    """Main CLI interface"""
    parser = argparse.ArgumentParser(
        description="Task Manager - Professional CLI task management",
        epilog="Example: python task_manager.py add 'Complete Python project'"
    )

    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('description', type=str, help='Task description')
    add_parser.add_argument('-p', '--priority', choices=['low', 'medium', 'high'],
                           default='medium', help='Task priority (default: medium)')

    # List command
    list_parser = subparsers.add_parser('list', help='List tasks')
    list_parser.add_argument('-a', '--all', action='store_true',
                            help='Show completed tasks too')
    list_parser.add_argument('-p', '--priority', choices=['low', 'medium', 'high'],
                            help='Filter by priority')

    # Complete command
    complete_parser = subparsers.add_parser('complete', help='Mark task as completed')
    complete_parser.add_argument('id', type=int, help='Task ID')

    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', type=int, help='Task ID')

    # Update command
    update_parser = subparsers.add_parser('update', help='Update a task')
    update_parser.add_argument('id', type=int, help='Task ID')
    update_parser.add_argument('-d', '--description', type=str, help='New description')
    update_parser.add_argument('-p', '--priority', choices=['low', 'medium', 'high'],
                               help='New priority')

    # Stats command
    subparsers.add_parser('stats', help='Show task statistics')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    # Initialize task manager
    manager = TaskManager()

    # Execute command
    if args.command == 'add':
        task = manager.add_task(args.description, args.priority)
        print(f"\n✓ Task added: #{task['id']} - {task['description']} [{task['priority']}]")

    elif args.command == 'list':
        tasks = manager.list_tasks(show_completed=args.all, priority=args.priority)
        display_tasks(tasks)

    elif args.command == 'complete':
        if manager.complete_task(args.id):
            print(f"\n✓ Task #{args.id} marked as completed!")
        else:
            print(f"\n✗ Task #{args.id} not found.")

    elif args.command == 'delete':
        if manager.delete_task(args.id):
            print(f"\n✓ Task #{args.id} deleted.")
        else:
            print(f"\n✗ Task #{args.id} not found.")

    elif args.command == 'update':
        if manager.update_task(args.id, args.description, args.priority):
            print(f"\n✓ Task #{args.id} updated.")
        else:
            print(f"\n✗ Task #{args.id} not found.")

    elif args.command == 'stats':
        stats = manager.get_stats()
        print(f"\n=== Task Statistics ===")
        print(f"Total tasks: {stats['total']}")
        print(f"Completed: {stats['completed']}")
        print(f"Pending: {stats['pending']}")
        print(f"\nPending by priority:")
        print(f"  High: {stats['by_priority']['high']}")
        print(f"  Medium: {stats['by_priority']['medium']}")
        print(f"  Low: {stats['by_priority']['low']}")
        print()


if __name__ == "__main__":
    main()
