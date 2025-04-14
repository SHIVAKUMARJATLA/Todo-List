class Task:
    TODO = "To Do"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"

    def __init__(self, description, status = TODO, due_time = None, priority = None):
        self.description = description
        self.status = status
        self.due_time = due_time
        self.priority = priority
    
    def completed(self):
        self.status = Task.COMPLETED
        return "The task is completed"
    
    def update_description(self, new_description):
        self.description = new_description
        return f"Description Updated to : {self.description}."
    
    def update_due_time(self, new_due_time):
        self.due_time = new_due_time
        return f"Due Time Updated to : {self.due_time}."
    
    def update_priority(self, new_priority):
        self.priority = new_priority
        return f"Priority Updated to : {self.priority}."


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task  '{task.description}' Added to the list")
    
    def view_tasks(self):
        if not self.tasks:
            print("Your Todo List is empty")
            return 
        print("\n------To-Do-List-----")
        index = 1
        for task in self.tasks:
            print(f"{index}. Description : {task.description}, Status : {task.status}", end = "")
            if task.due_time:
                print(f", Due Time : {task.due_time}", end = "")
            if task.priority:
                print(f", Priority : {task.priority}", end = "")
            print()
            index += 1
        print("-------------------\n")
    
    def mark_completed(self, task_index):
        try:
            index = int(task_index) - 1
            if 0 <= index < len(self.tasks):
                message = self.tasks[index].completed()
                print(message)
            else:
                print("Invalid Task Index.")
        except ValueError:
            print("Invalid Input. Please enter a number for the task index.")
    
    def view_tasks_by_status(self, status):
        filtered_tasks = [t for t in self.tasks if t.status == status]
        if not filtered_tasks:
            print(f"No tasks with status '{status}'")
            return
        for i, task in enumerate(filtered_tasks, 1):
            print(f"{i}. {task.description} | Due: {task.due_time or 'N/A'} | Priority: {task.priority or 'N/A'}")


    def remove_task(self, task_index):
        try:
            index = int(task_index) - 1
            if 0 <= index < len(self.tasks):
                removed_task = self.tasks.pop(index)
                print(f"Task '{removed_task.description}' removed from the list.")
            else:
                print("Invalid Task Index")
        except ValueError:
            print("Invalid Input. Please enter a number for the task index.")

todo_list = TodoList()

while True:
    command = input("\nChoose an action (add, view, complete, remove, filter, exit): ").lower()
    if command == "add":
        description = input("Enter task description: ")
        due_time = input("Enter due time (optional): ") or None
        priority = input("Enter Priority (optional): ") or None
        new_task = Task(description, "To Do", due_time, priority)
        todo_list.add_task(new_task)
    elif command == "view":
        todo_list.view_tasks()
    elif command == "complete":
        index_str = input("Enter the index of the task to mark as completed: ")
        todo_list.mark_completed(index_str)
    elif command == "remove":
        index_str = input("Enter the index of the task to remove: ")
        todo_list.remove_task(index_str)
    elif command == "filter":
        status = input("Enter status to filter (To Do, In Progress, Completed): ")
        todo_list.view_tasks_by_status(status)
    elif command == "exit":
        print("Exiting the To-Do List Application.")
        break
    else:
        print("Invalid input. Choose from (add, view, complete, remove, exit).")