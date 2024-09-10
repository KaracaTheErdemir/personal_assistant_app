import logging
from handlers.query_handler import delete_data, insert_data, update_data, fetch_data

def new_friend(line):
    payload = {"type": "friend", "data": line}
    # Call insert_data from query_handler with payload
    insert_data(payload)
    return "Adding a new friend."

def new_meeting(line):
    payload = {"type": "meeting", "data": line}
    insert_data(payload)
    return "Scheduling a new meeting."

def new_expense(line):
    payload = {"type": "expense", "data": line}
    insert_data(payload)
    return "Adding a new expense."

def new_habit(line):
    payload = {"type": "habit", "data": line}
    insert_data(payload)
    return "Tracking a new habit."

def new_todo(line):
    payload = {"type": "todo", "data": line}
    insert_data(payload)
    return "Creating a new todo."

def update_friend(line):
    payload = {"type": "friend", "data": line}
    # Call update_data from query_handler with payload
    update_data(payload)
    return "Updating friend."

def update_meeting(line):
    payload = {"type": "meeting", "data": line}
    update_data(payload)
    return "Updating meeting."

def update_expense(line):
    payload = {"type": "expense", "data": line}
    update_data(payload)
    return "Updating expense."

def update_habit(line):
    payload = {"type": "habit", "data": line}
    update_data(payload)
    return "Updating habit."

def update_todo(line):
    payload = {"type": "todo", "data": line}
    update_data(payload)
    return "Updating todo."

def delete_friend(line):
    payload = {"type": "friend", "data": line}
    # Call delete_data from query_handler with payload
    delete_data(payload)
    return "Deleting friend."

def delete_meeting(line):
    payload = {"type": "meeting", "data": line}
    delete_data(payload)
    return "Deleting meeting."

def delete_expense(line):
    payload = {"type": "expense", "data": line}
    delete_data(payload)
    return "Deleting expense."

def delete_habit(line):
    payload = {"type": "habit", "data": line}
    delete_data(payload)
    return "Deleting habit."

def delete_todo(line):
    payload = {"type": "todo", "data": line}
    delete_data(payload)
    return "Deleting todo."

def track_meeting(line):
    payload = {"type": "meeting", "data": line}
    update_data(payload)
    return "Tracking meeting."

def track_expense(line):
    payload = {"type": "expense", "data": line}
    update_data(payload)
    return "Tracking expense."

def track_habit(line):
    payload = {"type": "habit", "data": line}
    update_data(payload)
    return "Tracking habit."

def track_todo(line):
    payload = {"type": "todo", "data": line}
    update_data(payload)
    return "Tracking todo."

def list_friends(line):
    payload = {"type": "friends", "data": line}
    # Call fetch_data from query_handler with payload
    fetch_data(payload)
    return "Listing friends."

def list_meetings(line):
    payload = {"type": "meetings", "data": line}
    fetch_data(payload)
    return "Listing meetings."

def list_expenses(line):
    payload = {"type": "expenses", "data": line}
    fetch_data(payload)
    return "Listing expenses."

def list_habits(line):
    payload = {"type": "habits", "data": line}
    fetch_data(payload)
    return "Listing habits."

def list_todos(line):
    payload = {"type": "todos", "data": line}
    fetch_data(payload)
    return "Listing todos."

def report_friends(line):
    payload = {"type": "friends", "data": line}
    # Call fetch_data from query_handler with payload
    fetch_data(payload)
    return "Generating friends report."

def report_meetings(line):
    payload = {"type": "meetings", "data": line}
    fetch_data(payload)
    return "Generating meetings report."

def report_expenses(line):
    payload = {"type": "expenses", "data": line}
    fetch_data(payload)
    return "Generating expenses report."

def report_habits(line):
    payload = {"type": "habits", "data": line}
    fetch_data(payload)
    return "Generating habits report."

def report_todos(line):
    payload = {"type": "todos", "data": line}
    fetch_data(payload)
    return "Generating todos report."
