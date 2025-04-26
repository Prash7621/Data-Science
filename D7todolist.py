class ToDoList :
    def __init__(self):
        self.tasks = ["test" , "practice"]
        
    def show_tasks(self):
        if not self.tasks:
           print("Your to do-list is empty.")
        else:
            print("Your to-do list : ")
            for idx , task in enumerate(self.tasks , 1):
                print(f"{idx}. {task}")
    def add_task(self):
        task=input("Enter a new task : ")
        self.tasks.append(task)
        print(f"Task '{task}' added.")
    def remove_task(self):
        self.show_tasks()
        if self.tasks:
            try:
                task_num = int(input("Enter the number of the task to remove : "))
                if 1 <=task_num<=len(self.tasks):
                    removed=self.tasks.pop(task_num-1)
                    print(f"Task '{removed}' removed")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

def main():
    
    todo = ToDoList()
  
    while True:  
            print("\n Please choose an option : ")
            print("1. view task")
            print("2. add task")
            print("3. remove task")
            print("4.Exit")
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
                todo.show_tasks()
            elif choice == 2:
                todo.add_task()
            elif choice == 3:
                todo.remove_task()
            elif choice == 4:
                print("Exit")
                break
            else:
                print("Invalid choice")
   

if __name__ == "__main__":
    main()

  
  

# class ToDoList:
#     def __init__(self,tasks):
#         self.tasks = []

#     def show_tasks(self):
#         if not self.tasks:
#             print("Your to-do list is empty.")
#         else:
#             print("Your to-do list:")
#             for idx, task in enumerate(self.tasks, 1):
#                 print(f"{idx}. {task}")

#     def add_task(self):
#         task = input("Enter a new task: ")
#         self.tasks.append(task)
#         print(f"Task '{task}' added.")

#     def remove_task(self):
#         self.show_tasks()
#         if self.tasks:
#             try:
#                 task_num = int(input("Enter the number of the task to remove: "))
#                 if 1 <= task_num <= len(self.tasks):
#                     removed = self.tasks.pop(task_num - 1)
#                     print(f"Task '{removed}' removed.")
#                 else:
#                     print("Invalid task number.")
#             except ValueError:
#                 print("Please enter a valid number.")

# def main():
#     todo = ToDoList()
#     while True:
#         print("\nPlease choose an option:")
#         print("1. View Tasks")
#         print("2. Add Task")
#         print("3. Remove Task")
#         print("4. Exit")
#         choice = input("Enter your choice: ")

#         if choice == '1':
#             todo.show_tasks()
#         elif choice == '2':
#             todo.add_task()
#         elif choice == '3':
#             todo.remove_task()
#         elif choice == '4':
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()