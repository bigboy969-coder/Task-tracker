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

elif command == "update":
    task_id = int(sys.argv[2])
    new_description = sys.argv[3]
    for task in tasks:
        if task["id"]== task_id:
            task["description"] = new_description
    with open("tasks.json", "w")as f:
        json.dump(tasks,f , indent=2)
    print("Task updated")

elif command == "list":
    status_filter = None
    if len(sys.argv)>2:
        status_filter= sys.argv[2] 
    for task in tasks:
        if status_filter is None or task["status"]== status_filter:
            print(task["id"], task["description"], task["status"])                 

else:
    print("Unknown command")               

    