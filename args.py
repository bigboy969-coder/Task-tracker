import sys

command = sys.argv[1]

if command == "add":
    print("You want to add:", sys.argv[2])
elif command == "list":
    print("You want to list tasks")
else:
    print("Unknown command")        