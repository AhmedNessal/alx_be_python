# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Match case for priority-based description
match priority:
    case "high":
        detail = f"'{task}' is a high priority task"
    case "medium":
        detail = f"'{task}' is a medium priority task"
    case "low":
        detail = f"'{task}' is a low priority task"
    case _:
        detail = f"'{task}' is a task"

# MUST print Reminder: directly in print()
if time_bound == "yes":
    print(f"Reminder: {detail} that requires immediate attention today!")
else:
    print(f"Note: {detail}. Consider completing it when you have free time.")
