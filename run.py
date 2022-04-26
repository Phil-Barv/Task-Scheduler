from scheduler import Task, TaskScheduler

#create dummy tasks
tasks = [
    Task(0, 'get up at 8:00 AM', 10, [],90, False), 
    Task(1, 'get dressed and ready', 10, [0],62, False), 
    Task(2, 'eat healthy breakfast', 40, [0,1],50, True), 
    Task(3, 'make grocery list', 20, [0],55, True), 
    Task(4, 'go to the market', 15, [3],30, False), 
    Task(5, 'buy groceries in list', 30, [4],25, True), 
    Task(6, 'drive back home', 20, [5],30, False),
    Task(7, 'listen to music', 15, [],77, True),
    Task(8, 'store groceries', 15, [5,6],15, False),
    Task(9, 'PCW', 50, [6],39, False),
    Task(10, 'class', 90, [6,9],39, False),]

#initialize instance of task scheduler
task_scheduler = TaskScheduler(tasks)

#run scheduler
task_scheduler.run_task_scheduler()