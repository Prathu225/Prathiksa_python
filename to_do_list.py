class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Done" if self.completed else " Not Done"
        return f"{self.description} - {status}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Task added: {description}")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            print(f"Task '{self.tasks[index].description}' marked as completed.")
        else:
            print("Invalid task number.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("\nYour To-Do List:")
            for i, task in enumerate(self.tasks):
                print(f"{i}. {task}")


def main():
    todo_list = ToDoList()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            desc = input("Enter task description: ")
            todo_list.add_task(desc)
        elif choice == "2":
            todo_list.view_tasks()
            index = int(input("Enter task number to mark completed: "))
            todo_list.mark_task_completed(index)
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
