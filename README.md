KEYLOGGER PROJECT<BR>
Welcome to the Keylogger Project! This project is for educational purposes only, designed to demonstrate how keystroke logging works in a controlled, authorized environment. Unauthorized use of this code is strictly prohibited.

What Does This Project Do?
Captures and logs all key presses on your keyboard.

Saves the logged keys with timestamps to a file named keylogger_output.txt.

Displays a disclaimer when the program starts to ensure ethical use.

Provides an easy way to stop the program by pressing the Esc key.

How to Use This Project
Step 1: Requirements
Make sure you have the following installed:

Python 3.x

The required library: pynput

To install pynput, run:

bash
Copy
Edit
pip install pynput
Step 2: Run the Program
Save the code to a file, for example: keylogger.py.

Open a terminal or command prompt.

Run the script:

bash
Copy
Edit
python keylogger.py
Step 3: Stop the Program
To stop the keylogger, simply press the Esc key.

Step 4: Check the Logs
All logged key presses are saved in the file keylogger_output.txt in the same directory as the script.

Output Example
What You’ll See in the Terminal:
markdown
Copy
Edit
***************************************
*            DISCLAIMER               *
***************************************
This keylogger script is for educational purposes only.
Use it responsibly and only in authorized environments.
Unauthorized use of this script is illegal and unethical.
***************************************

Logging has been set up. Key presses will be saved to 'keylogger_output.txt'.
Keylogger is running. Press 'Esc' to stop.

Key pressed: a
Key pressed: b
Special key pressed: Key.enter
What You’ll See in keylogger_output.txt:
vbnet
Copy
Edit
2025-06-15 20:12:30 - Key pressed: a
2025-06-15 20:12:31 - Key pressed: b
2025-06-15 20:12:32 - Special key pressed: Key.enter
Features
User-Friendly Exit: Press Esc to stop the program at any time.

Comprehensive Logs: Logs both regular and special keys with timestamps.

Disclaimer: Clearly states the purpose and limitations of the script.

Important Notes
Ethics First: This script is for learning purposes only. Always get proper authorization before using it.

File Permissions: Ensure you have write permissions in the directory where you run the script.

Troubleshooting<BR>
pynput Not Installed?<BR>
Run:

bash
Copy
Edit
pip install pynput
Empty keylogger_output.txt?

Make sure you have write access to the directory.

Test the script in a simple Python environment.

Script Not Stopping?

Make sure the terminal window is active when pressing Esc.

Author<BR>
Designed by KEDARI Sneha, for educational and demonstration purposes.

Enjoy exploring the world of Python programming and ethical hacking! 🎉








