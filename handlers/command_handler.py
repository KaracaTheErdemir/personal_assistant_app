import logging
from query_handler import write_to_db, read_from_db

def new(option):
    try:
        logging.info(f"Executing /new with option {option}")
        # Call the database function to insert data
        return insert_data(option)
    except Exception as e:
        logging.error(f"Error in new: {type(e).__name__} - {str(e)}")
        return "An error occurred while processing /new."

def track(option):
    try:
        logging.info(f"Executing /track with option {option}")
        # Call the database function to update data
        return update_data(option)
    except Exception as e:
        logging.error(f"Error in track: {type(e).__name__} - {str(e)}")
        return "An error occurred while processing /track."

def list_data(option):
    try:
        logging.info(f"Executing /list with option {option}")
        # Call the database function to fetch data
        return fetch_data(option)
    except Exception as e:
        logging.error(f"Error in list_data: {type(e).__name__} - {str(e)}")
        return "An error occurred while processing /list."

def report(option):
    try:
        logging.info(f"Executing /report with option {option}")
        # Call the database function to fetch data for reporting
        return fetch_data(option)
    except Exception as e:
        logging.error(f"Error in report: {type(e).__name__} - {str(e)}")
        return "An error occurred while processing /report."