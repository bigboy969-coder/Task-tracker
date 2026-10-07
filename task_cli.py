import json
import os
import sys
import datetime

with open("tasks.json", "r")as f:
    tasks = json.load(f)

command = sys.argv[1]

if command == "add":
    new_id = 1 
    if len(tasks) > 0:
        new_id = tasks[-1]["id"]+1
    tasks.append({"id": new_id, "description":sys.argv[2], "status":"todo"})  
    with open("tasks.json", "w")as f:
        json.dump(tasks, f, indent=2)
    print("Task added")

elif command == "list":
    for task in tasks:
        print(task["id"], task["description"], task["status"]) 

elif command == "mark-done":
    task_id = int(sys.argv[2])
    for task in tasks:
        if task["id"]== task_id:
            task["status"] = "done"
    with open("tasks.json", "w") as f:
        json.dump(tasks, f ,indent=2)
    print("Marked done")

elif command == "mark-in-progress":
    task_id =int(sys.argv[2])
    for task in tasks:
        if task["id"] == task_id:
            task["status"]= "in-progress"
    with open("tasks.json", "w")as f:
        json.dump(tasks,f , indent=2)
    print("Marked in-progress") 

elif command == "delete":
    task_id = int(sys.argv[2])
    for task in tasks:
        if task["id"]== task_id:
            tasks.remove(task)
            break
    with open("tasks.json", "w")as f:
        json.dump(tasks, f, indent=2)
    print("Task deleted")    

else:
    print("Unknown command")               

    