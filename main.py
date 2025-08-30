# main.py

# Simple To-Do List (Console-based)

tasks = []  # Empty list to store tasks

def show_tasks():
    if not tasks:
        print("\nNo tasks yet! ✅")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def delete_task():
    show_tasks()
    if tasks:
        try:
            task_num = int(input("\nEnter the task number to delete: "))
            removed = tasks.pop(task_num - 1)
            print(f"Task '{removed}' deleted!")
        except (ValueError, IndexError):
            print("Invalid choice ❌")

def main():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Thanks for your time , Goodbye 👋")
            break
        else:
            print("Invalid option ❌")

if __name__ == "__main__":
    main()
