import json

with open("tasks.json", "r")as f:
    tasks = json.load(f) 

new_id = 1
if len(tasks) > 0:
    new_id = tasks[-1]["id"] + 1

tasks.append({"id": new_id, "description": "Call mom", "status": "todo"})

with open("tasks.json", "w")as f:
    json.dump(tasks, f, indent=2)

print("Task added successfully!")