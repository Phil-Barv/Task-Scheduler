from heapsort import MaxHeapq
class Task:
    """
    - id: Task Id   
    - description: Short description of the task   
    - duration: Duration in minutes 
    - dependencies: Number of tasks it has dependency on
    - priority: Priority level of a task (ranging from 0 to 100)
    - multi_tasking: Bool status of whether task can be multi-tasked or not
    - status: Current status of the task:       
    """
    #Initializes an instance of Task
    def __init__(self,task_id,description,duration,dependencies,priority,multi_tasking, status="N"):
        self.id= task_id
        self.description=description
        self.duration=duration
        self.dependencies=dependencies  
        self.priority = priority
        self.multi_tasking = multi_tasking
        self.status=status

    def __repr__(self):
        return f"{self.description} - id: {self.id}\n \tDuration:{self.duration}\n\tDepends on: {self.dependencies}\n\tStatus: {self.status}\n\tPriority: {self.priority}\n\tMulti-Tasking: {self.multi_tasking}"

    def __lt__(self, other):
        return self.priority < other.priority

class TaskScheduler:
    """
    A Simple Daily Task Scheduler Using Priority Queues With Multi-Tasking Feature
    """
    NOT_STARTED ='N'
    IN_PRIORITY_QUEUE = 'I'
    COMPLETED = 'C'

    def __init__(self, tasks):
        self.tasks = tasks
        self.priority_queue = MaxHeapq()    

    def print_self(self):
        print('Input List of Tasks')
        for t in self.tasks:
            print(t)            

    def remove_dependency(self, task_id):
        """
        Input: list of tasks and task_id of the task just completed
        Output: lists of tasks with t_id removed
        """
        for t in self.tasks:
            if t.id != task_id and task_id in t.dependencies:
                t.dependencies.remove(task_id)           

    def get_tasks_ready(self):
        """ 
        Implements step 1 of the scheduler
        Input: list of tasks
        Output: list of tasks that are ready to execute (i.e. tasks with no pendending task dependencies)
        """
        for task in self.tasks:
            #If task has no dependencies and is not yet in queue
            if task.status == self.NOT_STARTED and not task.dependencies:
                #Change status of the task
                task.status = self.IN_PRIORITY_QUEUE 
                #Push task into the priority queue
                self.priority_queue.heappush(task)

    def check_unscheduled_tasks(self):
        """
        Input: list of tasks 
        Output: boolean (checks the status of all tasks and returns True if at least one task has status = 'N'
        """
        for task in self.tasks:
            if task.status == self.NOT_STARTED:
                return True
        return False   

    def format_time(self, time):
        return f"{time//60}h{time%60:02d}"

    def run_task_scheduler(self, starting_time = 480):
        current_time = starting_time
        while self.check_unscheduled_tasks() or self.priority_queue.heap_size != 0:
            #Extract tasks ready to execute (those without dependencies) and push them into the priority queue
            self.get_tasks_ready()
            
            #set task to value on top of the priority queue 
            task = self.priority_queue.heappop()
            
            #set up task1 
            if self.priority_queue.heap_size != 0:
                task1 = self.priority_queue.heappop()  
                
            #handle multitasking: check for TT and execute if they're not the same item
            if task1.multi_tasking == True and task.multi_tasking == True and task1.id != task.id:
                mx_time = max([task.duration,task1.duration])
                print(f"⏰Simple Scheduler at time {self.format_time(current_time)} started 🤔multi-tasking🤓 {task.id} and {task1.id} that take {mx_time} mins")
                current_time += mx_time            
                print(f"✅ Completed Task {task.id} - '{task.description}' and {task1.id} - '{task1.description}'  at time {self.format_time(current_time)}\n") 
                #Remove task from the dependency list
                self.remove_dependency(task.id)
                task.status = self.COMPLETED

                #Remove task1 from the dependency list
                self.remove_dependency(task1.id)
                task1.status = self.COMPLETED

            #handle F for task1 is either not completed or in queue  
            if task1.multi_tasking == False and task1.status != self.COMPLETED:
                print(f"⏰Simple Scheduler at time {self.format_time(current_time)} started executing task {task1.id} that takes {task1.duration} mins")
                current_time += task1.duration            
                print(f"✅ Completed Task {task1.id} - '{task1.description}' at time {self.format_time(current_time)}\n") 
                #Remove task1 from the dependency list
                self.remove_dependency(task1.id)
                task1.status = self.COMPLETED
        
            #handle F for task is either not completed or in queue
            if task.multi_tasking == False and task.status != self.COMPLETED:
                print(f"⏰Simple Scheduler at time {self.format_time(current_time)} started executing task {task.id} that takes {task.duration} mins")
                current_time += task.duration            
                print(f"✅ Completed Task {task.id} - '{task.description}' at time {self.format_time(current_time)}\n") 
                #Remove task from the dependency list
                self.remove_dependency(task.id)
                task.status = self.COMPLETED
                
            #handles T for task1 that is either not completed or in queue
            if task1.multi_tasking == True and task1.status != self.COMPLETED:
                self.priority_queue.heappush(task1)
            
            #handles T for task that is either not completed or in queue
            if task.multi_tasking == True and task.status != self.COMPLETED:
                self.priority_queue.heappush(task)
                
                
        total_time = current_time - starting_time             
        print(f"🏁 Completed all planned tasks in {total_time//60}h{total_time%60:02d}min")
