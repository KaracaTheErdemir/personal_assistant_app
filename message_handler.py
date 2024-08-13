import logging

friend_list = ['Uygur', 'Yusuf', 'Ayran', 'Rabia']
def meeting_entry(message):
    if message in friend_list:
        response = f"evet bu yakın dostum {message}"
    else:
        response = f"{message} kim"
    return response

def habit_entry(message):
    pass

def objective_entry(message):
    pass

def conversation_entry(message):
    pass

def measuring_mode(message):
    pass

