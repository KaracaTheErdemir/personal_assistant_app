import logging
from handlers.query_handler import delete_data, insert_data, update_data, fetch_data

def new_friend(parts):
    payload = {
        "name" : parts[2],
        "full_name" : parts[3],
        "sex" : parts[4]
    }
    insert_data("friends", payload)
    return "Adding a new friend."

def new_meeting(parts):
    payload = {
        "name" : parts[2],
        "full_name" : parts[3],
        "sex" : parts[4]
    }
    insert_data("meetings", payload)
    return "Scheduling a new meeting."

def new_expense(parts):
    payload = {"type": "expense", "data": parts}
    insert_data(payload)
    return "Adding a new expense."

def new_habit(parts):
    payload = {"type": "habit", "data": parts}
    insert_data(payload)
    return "Tracking a new habit."

def new_todo(parts):
    payload = {"type": "todo", "data": parts}
    insert_data(payload)
    return "Creating a new todo."

def update_friend(parts):
    option = parts[2]
    payload = {
        "full_name": parts[3]
    }
    if option == '-p':
        payload["profession"] = parts[4]
    elif option == '-f':
        payload["friends_since"] = parts[4]
    elif option == '-b':
        payload["birth_date"] = parts[4]
    update_data("friends", payload)
    return "Updating friend."

def update_meeting(parts):
    payload = {"type": "meeting", "data": parts}
    update_data(payload)
    return "Updating meeting."

def update_expense(parts):
    payload = {"type": "expense", "data": parts}
    update_data(payload)
    return "Updating expense."

def update_habit(parts):
    payload = {"type": "habit", "data": parts}
    update_data(payload)
    return "Updating habit."

def update_todo(parts):
    payload = {"type": "todo", "data": parts}
    update_data(payload)
    return "Updating todo."

def delete_friend(parts):
    payload = {"type": "friend", "data": parts}
    # Call delete_data from query_handler with payload
    delete_data(payload)
    return "Deleting friend."

def delete_meeting(parts):
    payload = {"type": "meeting", "data": parts}
    delete_data(payload)
    return "Deleting meeting."

def delete_expense(parts):
    payload = {"type": "expense", "data": parts}
    delete_data(payload)
    return "Deleting expense."

def delete_habit(parts):
    payload = {"type": "habit", "data": parts}
    delete_data(payload)
    return "Deleting habit."

def delete_todo(parts):
    payload = {"type": "todo", "data": parts}
    delete_data(payload)
    return "Deleting todo."

def track_meeting(parts):
    payload = {"type": "meeting", "data": parts}
    update_data(payload)
    return "Tracking meeting."

def track_expense(parts):
    payload = {"type": "expense", "data": parts}
    update_data(payload)
    return "Tracking expense."

def track_habit(parts):
    payload = {"type": "habit", "data": parts}
    update_data(payload)
    return "Tracking habit."

def track_todo(parts):
    payload = {"type": "todo", "data": parts}
    update_data(payload)
    return "Tracking todo."

def list_friends(parts):
    payload = {"type": "friends", "data": parts}
    # Call fetch_data from query_handler with payload
    fetch_data(payload)
    return "Listing friends."

def list_meetings(parts):
    payload = {"type": "meetings", "data": parts}
    fetch_data(payload)
    return "Listing meetings."

def list_expenses(parts):
    payload = {"type": "expenses", "data": parts}
    fetch_data(payload)
    return "Listing expenses."

def list_habits(parts):
    payload = {"type": "habits", "data": parts}
    fetch_data(payload)
    return "Listing habits."

def list_todos(parts):
    payload = {"type": "todos", "data": parts}
    fetch_data(payload)
    return "Listing todos."

def report_friends(parts):
    payload = {"type": "friends", "data": parts}
    # Call fetch_data from query_handler with payload
    fetch_data(payload)
    return "Generating friends report."

def report_meetings(parts):
    payload = {"type": "meetings", "data": parts}
    fetch_data(payload)
    return "Generating meetings report."

def report_expenses(parts):
    payload = {"type": "expenses", "data": parts}
    fetch_data(payload)
    return "Generating expenses report."

def report_habits(parts):
    payload = {"type": "habits", "data": parts}
    fetch_data(payload)
    return "Generating habits report."

def report_todos(parts):
    payload = {"type": "todos", "data": parts}
    fetch_data(payload)
    return "Generating todos report."
