# This example drags the mouse in a square spiral shape in MS Paint (or any graphics drawing program)
import pyautogui

distance = 200
while distance > 0:
        pyautogui.drag(distance, 0, duration=0.5)   # move right
        distance -= 5
        pyautogui.drag(0, distance, duration=0.5)   # move down
        pyautogui.drag(-distance, 0, duration=0.5)  # move left
        distance -= 5
        pyautogui.drag(0, -distance, duration=0.5)  # move up