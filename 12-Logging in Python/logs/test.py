# test.py
import os
import logging

# Change the working directory to the directory of this script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import custom_logger  # Ensure this line is executed to configure logging

def add(a, b):
    logging.debug("The addition operation is taking place")
    return a + b

logging.debug("The addition function is called")
add(10, 15)
