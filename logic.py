from clicker import ClickMouse
from pynput.keyboard import Listener

def execute_clicker(delay, button, click_limit, start_key, break_key):
    """Executes the ClickMouse logic."""
    clicker = ClickMouse(delay, button, click_limit, break_key)

    def on_press(key):
        """Starts the clicking when the start key is pressed."""
        if key == start_key:
            print(f"Starting clicker with limit {click_limit} clicks.")
            clicker.click()
            print("Program completed successfully.")
            return False  # Stop the listener once the task is done

    print(f"Press '{start_key.char}' to start clicking. Press '{break_key.char}' to stop early.")
    with Listener(on_press=on_press) as listener:
        listener.join()

    return "completed"  # Return control after execution
