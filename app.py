class Sol:
    def __init__(self):
        self.menu = """
===============================
       DEVOPS TASK TRACKER
===============================

        1. Add Task
        2. List Tasks
        3. Complete Task
        4. Delete Task
        5. Exit
"""
obj=Sol()
print(obj.menu)

class exe():
    def __init__(self):
        self.li={}

    def value(self,enter):
        if enter==1:
            print("1.new task")
            print("2.edit task")
            f=(int(input("enter:")))
            if f==1:
                a=input("Enter your task:")
                self.li[a]="pending"
                print("Task added successfully!")
                
            else:
                r=input("enter task to edit:")
                if r in self.li:
                    print("Task Found you can edit only(inprogress,comleted)")
                    s=input("enter status:")
                    self.li[r]=s
                    print("Task status changed")
                else:
                    print("Task not found in list add the task first")

        elif enter==2:
            if len(self.li)>0:
                print(self.li)
            else:
                print( "List is empty no task found")

        elif enter==3:
            e=input("enter task name to mark completed :")
            if len(self.li)>0:
                if e in self.li:
                    self.li[e]="Completed"
                print(self.li)

            else:
                print("list is empty")
            

        elif enter==4:
            d=input("enter task to Delete:")
            if d in self.li:
                self.li.pop(d,None)
                print(self.li)
            else:
                print("Task not found")

        elif enter>5 or enter<=0:  
            print("Enter only task number from 1-5 not above that.")

enter=(int(input("Enter the Task number :")))
tracker=exe()
tracker.value(enter)
while True:
    print(obj.menu)

    enter = int(input("Enter the Task number: "))

    if enter==5:
        break

    tracker.value(enter)
    

              
