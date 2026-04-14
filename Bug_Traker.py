"""
-----------------------------------------------------------------------
ASSIGNMENT 11A REVISED: THE BUG TRACKING LOG
-----------------------------------------------------------------------
[ ] 1. Program uses a while loop to keep asking for bugs.
[ ] 2. Uses the datetime module to get a timestamp format.
[ ] 3. Stores the timestamp, file name, description, and priority in a dictionary.
[ ] 4. Uses `with open("bug_log.txt", "a")` to append to the file safely.
[ ] 5. The bug_log.txt file is formatted neatly with newlines.
-----------------------------------------------------------------------
"""

import datetime


def main():
    while True:
        user_choice = input("Enter 'log' to record a bug, or 'quit' to stop: ").lower()
        
        if user_choice == "quit":
            print("Bug log updated!")
            break
        
        elif user_choice == "log":
            # Gather inputs
            file_name = input("File name: ")
            description = input("Description of error: ")
            priority = input("Priority (High, Medium, Low): ")
            
            # Generate timestamp
            current_time = datetime.datetime.now()
            timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
            
            # Get into dictionary to store 
            bug_dict = {
                timestamp: [file_name, description, priority]
            }
            
            # Go append to file
            with open("bug_log.txt", "a") as file:
                file.write(f"""[{timestamp}]
File: {bug_dict[timestamp][0]}
Status: {bug_dict[timestamp][1]}
Priority: {bug_dict[timestamp][2]}
--------------------------------------------------
""")
        else:
            print("Invalid input. Please type 'log' or 'quit'.")


# Run program
main()