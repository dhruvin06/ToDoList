class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def print_tasks(self):
        print(self.tasks)

    def empty_tasks(self):
        self.tasks = []

    def add_task(self,task_name):
        self.tasks.append({"name": task_name , "status" : "Not Completed"})
        print(f'{task_name} is successfully added')

    def complete_task(self,task_name):
        for task in self.tasks:
            if task["name"] == task_name:
                if task["status"] == "Not Completed":
                    task["status"] = "Completed"
                    print(f'{task_name} is successfully completed')
                else:
                    print(f'The task is already completed')
                return
        print(f'The task {task_name} wasn\'t found')
                
    def view_tasks(self):
        if not self.tasks:
            print("There are not tasks")
        else:
            for task in self.tasks:
                print(f'{task["name"]} : {task["status"]}')

    def remove_task(self,task_name):
        for task in self.tasks:
            if task["name"] == task_name:
                self.tasks.remove(task)
                print(f'The task {task_name} was removed')
                return
        print(f'The task {task_name} was not found')

    
    
todolist = ToDoListManager()

todolist.empty_tasks()
todolist.print_tasks()
todolist.add_task("studying")
todolist.add_task("cooking")
todolist.complete_task("studying")
todolist.print_tasks()
todolist.complete_task("hello")
todolist.view_tasks()
todolist.remove_task("studying")
todolist.view_tasks()