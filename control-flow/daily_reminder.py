# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Match case for priority-based message
match priority:
    case "high":
        base_message = f"'{task}' is a high priority task"
    case "medium":
        base_message = f"'{task}' is a medium priority task"
    case "low":
        base_message = f"'{task}' is a low priority task"
    case _:
        base_message = f"'{task}' is a task"

# Time-bound modification
if time_bound == "yes":
    final_message = f"Reminder: {base_message} that requires immediate attention today!"
else:
    final_message = f"Note: {base_message}. Consider completing it when you have free time."

print(final_message)
