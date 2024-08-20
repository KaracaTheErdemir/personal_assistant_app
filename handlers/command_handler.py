import logging
from query_handler import write_to_db, read_from_db

# /track habit
def track_habit(message):
    habit_data = message.split()  # Assume habit data comes from user input
    result = write_to_db("habits", habit_data)
    if result:
        return "Habit tracked successfully!"
    else:
        return "Failed to track habit."

# /track list
def list_habits(message):
    habits = read_from_db("habits")
    if habits:
        return f"Your habits: {', '.join(habits)}"
    else:
        return "No habits found."

# /meeting new
def new_meeting(message):
    meeting_data = message.split()  # Assume meeting data comes from user input
    result = write_to_db("meetings", meeting_data)
    if result:
        return "Meeting scheduled successfully!"
    else:
        return "Failed to schedule meeting."

# /meeting list
def list_meetings(message):
    meetings = read_from_db("meetings")
    if meetings:
        return f"Your meetings: {', '.join(meetings)}"
    else:
        return "No meetings found."

# /objective set
def set_objective(message):
    objective_data = message.split()  # Assume objective data comes from user input
    result = write_to_db("objectives", objective_data)
    if result:
        return "Objective set successfully!"
    else:
        return "Failed to set objective."

# /objective list
def list_objectives(message):
    objectives = read_from_db("objectives")
    if objectives:
        return f"Your objectives: {', '.join(objectives)}"
    else:
        return "No objectives found."

# /friend new
def new_friend(message):
    friend_data = message.split()  # Assume friend data comes from user input
    result = write_to_db("friends", friend_data)
    if result:
        return "Friend added successfully!"
    else:
        return "Failed to add friend."

# /friend list
def list_friends(message):
    friends = read_from_db("friends")
    if friends:
        return f"Your friends: {', '.join(friends)}"
    else:
        return "No friends found."

# /expense new
def new_expense(message):
    expense_data = message.split()  # Assume expense data comes from user input
    result = write_to_db("expenses", expense_data)
    if result:
        return "Expense added successfully!"
    else:
        return "Failed to add expense."

# /expense list
def list_expenses(message):
    expenses = read_from_db("expenses")
    if expenses:
        return f"Your expenses: {', '.join(expenses)}"
    else:
        return "No expenses found."
