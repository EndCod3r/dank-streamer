from pynput.mouse import Controller, Button
import time
import random

# Sets mouse as a variable to Controller()
mouse = Controller()

RunADPos = 2350
ReadChatPos = 2440
CollectDonationsPos = 2570

# Makes a infinite loop for auto streaming.
while True:
    # Moves mouse to Dismiss messsage button and clicks it
    time.sleep(5)
    mouse.position = (2475, 1025)
    time.sleep(0.5)
    mouse.click(Button.left, 1)

    # Waits 10 minutes to move mouse to random button and click it
    time.sleep(600)
    button = random.randint(1, 3)
    if button == 1:
        mouse.position = (RunADPos, 1000)
        time.sleep(0.3)
        mouse.click(Button.left, 1)
    elif button == 2:
        mouse.position = (ReadChatPos, 1000)
        time.sleep(0.3)
        mouse.click(Button.left, 1)
    elif button == 3:
        mouse.position = (CollectDonationsPos, 1000)
        time.sleep(0.3)
        mouse.click(Button.left, 1)
