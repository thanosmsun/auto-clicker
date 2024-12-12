import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

class ClickMouse:
    def __init__(self, delay, button, click_limit, break_key):
        self.delay = delay
        self.button = button
        self.click_limit = click_limit
        self.click_count = 0
        self.mouse = Controller()
        self.break_key = break_key
        self.stop_flag = False  # Flag to indicate if the process should stop

    def click(self):
        #Performs the clicking operation.
        def on_press(key):
            if key == self.break_key:
                print("Break key pressed. Stopping early.")
                self.stop_flag = True
                return False  # Stop the listener

        with Listener(on_press=on_press) as listener:
            while self.click_count < self.click_limit and not self.stop_flag:
                self.mouse.click(self.button)
                self.click_count += 1
                time.sleep(self.delay)
            listener.stop()

        if self.stop_flag:
            print("Clicking stopped early by the user.")
        else:
            print(f"Click limit of {self.click_limit} reached.")
