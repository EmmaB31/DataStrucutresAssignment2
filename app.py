#ititialise data strucutre
tasks = {}
next_id = 1

#add new task
def add_task():
    global next_id
    title = input("Add new task:").strip().lower()
    if not title:
        print("Title Required")
    while True:
        try:
            priority = int(input("Set priority value:"))
            break
        except ValueError:
            print("Invalid input")
    task = {
        "id": next_id,
        "title": title,
        "priority": priority,
        "completed": False
    }
    tasks[next_id] = task
    print("Success:", task["title"], "successfully added")
    next_id += 1

#return task by ID
def task_by_id():
    if not tasks:
        print("No Tasks to Find")
    task_id_to_find = int(input("Enter task number to find:"))
    if task_id_to_find in tasks:
        print(tasks[task_id_to_find])
    else:
        print("Task not found")

#search tasks by title
def search_by_title():
    if not tasks:
        print("No Tasks to Complete")
    title_to_find = input("Enter title to find:").strip().lower()

    matched_task = {
        k: v for k, v in tasks.items()
        if v.get("title") == title_to_find
    }
    if not matched_task:
        print("No matching entry")
    else:
        print(matched_task)

#mark a task complete
def mark_complete():
    if not tasks:
        print("No Tasks to Complete")
    task_id_to_complete = int(input("Enter task id to mark complete:"))
    if task_id_to_complete in tasks:
        tasks[task_id_to_complete]["completed"] = True
        print("Task Complete")
    else:
        print("Task not found")

#find highest priority task
def highest_priority():
    if not tasks:
        print("No tasks found")
        return

    highest_priority_task = None

    for task in tasks:
        if task["completed"]:
            continue  # skip completed tasks
        if highest_priority_task is None or task["priority"] > highest_priority_task["priority"]:
            highest_priority_task = task
    print(
        f'Highest priority task:\n'
        f'ID: {highest_priority_task["id"]} '
        f'Title: {highest_priority_task["title"]} '
        f'Priority: {highest_priority_task["priority"]}'
    )
#update task title and priority
def update_task():
    if not tasks:
        print("No tasks to update")
    task_to_update = int(input("Enter task number to update:"))
    new_title = input("Enter new title")
    new_priority = int(input("Enter new priority:"))
    tasks[task_to_update].update({"title": new_title, "priority": new_priority})
    print("Task updated. New task details:", tasks[task_to_update])


# User interface
def main_menu():
        print("Task Tracker")
        print("1. Add task")
        print("2. Find task by ID")
        print("3. Find task by Title")
        print("4. Mark Complete Task")
        print("5. Highest Priority Task")
        print("6. Update Task")
        print("7. Exit")

while True:
        main_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            task_by_id()
        elif choice == "3":
            search_by_title()
        elif choice == "4":
            mark_complete()
        elif choice == "5":
            highest_priority()
        elif choice == "6":
            update_task()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


