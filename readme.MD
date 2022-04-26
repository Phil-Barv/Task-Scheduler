# Multi-tasking Task Scheduler

<br>

This project uses heap sorting priority queues to determine the most optimal order in which to complete a set of
tasks. It includes a multi-tasking feature where you can set a particular task to be multi-taskeable. Instructions to run
the repository locally are provided below.

<br>

### Example Tasks

<br>

The following tasks are dummy tasks to show how to use the application. Insert your tasks as shown below.

```python
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
```

<br>

### Output

<br>

```txt
⏰Simple Scheduler at time 8h00 started executing task 0 that takes 10 mins
✅ Completed Task 0 - 'get up at 8:00 AM' at time 8h10

⏰Simple Scheduler at time 8h10 started executing task 1 that takes 10 mins
✅ Completed Task 1 - 'get dressed and ready' at time 8h20

⏰Simple Scheduler at time 8h20 started 🤔multi-tasking🤓 7 and 3 that take 20 mins
✅ Completed Task 7 - 'listen to music' and 3 - 'make grocery list'  at time 8h40

⏰Simple Scheduler at time 8h40 started executing task 4 that takes 15 mins
✅ Completed Task 4 - 'go to the market' at time 8h55

⏰Simple Scheduler at time 8h55 started 🤔multi-tasking🤓 2 and 5 that take 40 mins
✅ Completed Task 2 - 'eat healthy breakfast' and 5 - 'buy groceries in list'  at time 9h35

⏰Simple Scheduler at time 9h35 started executing task 6 that takes 20 mins
✅ Completed Task 6 - 'drive back home' at time 9h55

⏰Simple Scheduler at time 9h55 started executing task 8 that takes 15 mins
✅ Completed Task 8 - 'store groceries' at time 10h10

⏰Simple Scheduler at time 10h10 started executing task 9 that takes 50 mins
✅ Completed Task 9 - 'PCW' at time 11h00

⏰Simple Scheduler at time 11h00 started executing task 10 that takes 90 mins
✅ Completed Task 10 - 'class' at time 12h30

🏁 Completed all planned tasks in 4h30min
```

<br>


## Running Repo Locally

1. Clone the repo to your local machine!
2. Open your terminal and cd to the location of the cloned repo.
3. In the clone's root directory, input:

#### macOS
```python3
python3.6 run.py
```

#### Windows
```python3
python3.6 run.py
```

#### Git Bash
```python3
python3.6 run.py
```

4. Once you run the command, the app will generate the optimal schedule which will be displayed in the terminal.
5. Feel free to adapt the code for your tasks.