#Ask the user to input a task description
task = input("Enter your task")

#Prompt for the task’s priority (high, medium, low)\
priority = input("Priority (high/medium/low):")

#Ask if the task is time-bound (yes or no)
time_bound = input("Is it time-bound? (yes/no)")

while priority not in ("high", "medium", "low"):
    print("Invalid priority. Please enter high, medium, or low.")
    priority = input("Priority (high/medium/low): ").lower()

while time_bound not in ("yes", "no"):
    print("Please answer 'yes' or 'no'.")
    time_bound = input("Is it time-bound? (yes/no): ").lower()


match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"

if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

print("Reminder:", message)
