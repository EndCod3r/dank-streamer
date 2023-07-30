from pynput.mouse import Controller
import time

mouse = Controller()

time.sleep(5)

time.sleep(5)
mouse.position = (2350, 1000)
time.sleep(5)
mouse.position = (2400, 1000)
time.sleep(5)
mouse.position = (2570, 1000)
print(
    "If the cursor didn't move to the positions of the buttons run GetMousePosition.py again."
)
