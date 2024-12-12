import tkinter as tk
from tkinter import messagebox
from pynput.mouse import Button
from pynput.keyboard import KeyCode
from logic import execute_clicker
import sys

class AutoClickerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Auto Clicker Configuration")
        self.root.geometry("400x400")  # Adjusted for additional space

        # Input fields with default values
        tk.Label(self.root, text="Delay (seconds):", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
        self.delay_entry = tk.Entry(self.root, font=("Arial", 12))
        self.delay_entry.insert(0, "0.1")  # Default value
        self.delay_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Button (left/right):", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10)
        self.button_var = tk.StringVar(value="left")
        tk.OptionMenu(self.root, self.button_var, "left", "right").grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Click Limit (integer):", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10)
        self.click_limit_entry = tk.Entry(self.root, font=("Arial", 12))
        self.click_limit_entry.insert(0, "100")  # Default value
        self.click_limit_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Start Key:", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=10)
        self.start_key_entry = tk.Entry(self.root, font=("Arial", 12))
        self.start_key_entry.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Break Key:", font=("Arial", 12)).grid(row=4, column=0, padx=10, pady=10)
        self.break_key_entry = tk.Entry(self.root, font=("Arial", 12))
        self.break_key_entry.grid(row=4, column=1, padx=10, pady=10)

        # Submit button with validation
        tk.Button(self.root, text="Submit", font=("Arial", 14), command=self.on_submit).grid(row=5, column=0, pady=20)

        # Close button to exit program
        tk.Button(self.root, text="Close", font=("Arial", 14), command=self.close_program).grid(row=5, column=1, pady=20)

    def on_submit(self):
        try:
            # Check if all fields are filled
            if not (self.delay_entry.get() and self.click_limit_entry.get() and 
                    self.start_key_entry.get() and self.break_key_entry.get()):
                raise ValueError("All fields must be filled.")

            # Gather user inputs
            delay = float(self.delay_entry.get())
            button_input = self.button_var.get().lower()
            button = Button.left if button_input == "left" else Button.right
            click_limit = int(self.click_limit_entry.get())
            start_key = KeyCode(char=self.start_key_entry.get().strip())
            break_key = KeyCode(char=self.break_key_entry.get().strip())

            # Close the GUI window
            self.root.destroy()

            # Call the execution logic
            result = execute_clicker(delay, button, click_limit, start_key, break_key)
            print(result)  # Print the result returned by the logic
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
            return  # Do not close the GUI if there is an error

    def close_program(self):
        """Terminates the program immediately."""
        self.root.destroy()
        sys.exit()  # Exits the Python process

    def run(self):
        self.root.mainloop()
