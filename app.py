#ititialise data strucutre
tasks = {}
next_id = 1
#add new task
def addTask():
    global next_id
    title = input("Add new task:").strip()
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
addTask()
#return task by ID
def task_by_id():
    if not tasks:
        print("No Tasks to Find")
    task_id_to_find = int(input("Enter task number to find:"))
    if task_id_to_find in tasks:
        print(tasks[task_id_to_find])
    else:
        print("Task not found")
task_by_id()
#mark a task complete
def mark_complete():
    if not tasks:
        print("No Tasks to Complete")
    task_id_to_complete = int(input("Enter task id to mark complete"))
    if task_id_to_complete in tasks:
        tasks[task_id_to_complete]["completed"] = True

