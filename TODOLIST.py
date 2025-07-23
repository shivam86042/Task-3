# TO-DO List Application in Python

tasks = []

# Function to display all tasks
def view_tasks():
    if not tasks:
        print("\n📋 Your to-do list is empty!\n")
    else:
        print("\n📝 Current Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()

# Function to add a new task
def add_task():
    task = input("➕ Enter the task: ")
    tasks.append(task)
    print("✅ Task added successfully!\n")

# Function to update a task
def update_task():
    view_tasks()
    try:
        task_no = int(input("✏️ Enter task number to update: "))
        if 1 <= task_no <= len(tasks):
            new_task = input("Enter the new task: ")
            tasks[task_no - 1] = new_task
            print("✅ Task updated!\n")
        else:
            print("❌ Invalid task number.\n")
    except ValueError:
        print("⚠️ Please enter a valid number.\n")

# Function to delete a task
def delete_task():
    view_tasks()
    try:
        task_no = int(input("🗑️ Enter task number to delete: "))
        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            print(f"🗑️ Task '{removed}' deleted!\n")
        else:
            print("❌ Invalid task number.\n")
    except ValueError:
        print("⚠️ Please enter a valid number.\n")

# Main function with menu
def main():
    while True:
        print("========== TO-DO LIST MENU ==========")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Select an option (1-5): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("👋 Exiting... Have a productive day!")
            break
        else:
            print("❌ Invalid choice! Please try again.\n")

# Run the program
if __name__ == "__main__":
    main()
