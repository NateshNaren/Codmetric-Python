
#Task 3 - To-Do List Manager


TASKS_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    try:
        with open(TASKS_FILE, "r") as f:
            for line in f:
                task, status = line.strip().split("|")
                tasks.append({"task": task, "completed": status == "True"})
    except FileNotFoundError:
        pass
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for t in tasks:
            f.write(f"{t['task']}|{t['completed']}\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for i, t in enumerate(tasks):
        status = "✅" if t["completed"] else "❌"
        print(f"{i+1}. {t['task']} [{status}]")

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Deleted: {removed['task']}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Enter a valid number.")

def mark_complete(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to mark complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            print(f"Marked '{tasks[index]['task']}' as completed.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. View Tasks\n2. Add Task\n3. Delete Task\n4. Mark Completed\n5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_complete(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
