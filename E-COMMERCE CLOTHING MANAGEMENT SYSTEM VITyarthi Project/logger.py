
# logger.py
# This file handles simple logging for the Zara Inventory app.
# It just writes messages to a text file called activity_log.txt
# I made this very simple, no fancy logging library used.

import datetime

LOG_FILE = "activity_log.txt"


def write_log(message):
    # get current time
    now = datetime.datetime.now()
    time_string = now.strftime("%Y-%m-%d %H:%M:%S")

    # make the full log line
    log_line = "[" + time_string + "] " + message

    # open file in append mode so old logs dont get deleted
    file = open(LOG_FILE, "a")
    file.write(log_line + "\n")
    file.close()

    # also print it so we can see it while running the app
    print("LOG:", log_line)


def log_info(message):
    write_log("INFO - " + message)


def log_error(message):
    write_log("ERROR - " + message)


def log_success(message):
    write_log("SUCCESS - " + message)
