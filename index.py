# Imports Controller and Button from pynput.mouse
from pynput.mouse import Controller, Button

# Imports time to make a sleep timer
import time

# Imports random to generate a random number
import random

# Sets mouse as a variable to Controller()
mouse = Controller()

# Gets the positions for each button
print("Hover over Run AD Button in less than 5 seconds.")
time.sleep(5)
RunADPos = mouse.position
print("Hover over Read Chat Button in less than 5 seconds.")
time.sleep(5)
ReadChatPos = mouse.position
print("Hover over Collect Donations Button in less than 5 seconds.")
time.sleep(5)
CollectDonationsPos = mouse.position
print(
    "Hover over the Dismiss Message Button in Discord by clicking one of the buttons in less than 5 seconds."
)
time.sleep(5)
DismissMessagePos = mouse.position

print("Open Discord in less than 5 seconds and start streaming.")
time.sleep(5)


# Makes a infinite loop for auto streaming.
while True:
    # Moves mouse to Dismiss messsage button and clicks it
    time.sleep(5)
    mouse.position = DismissMessagePos
    time.sleep(0.5)
    mouse.click(Button.left, 1)

    # Waits 10 minutes to move mouse to random button and click it
    time.sleep(600)
    button = random.randint(1, 3)
    if button == 1:
        mouse.position = RunADPos
        time.sleep(0.3)
        mouse.click(Button.left, 1)
    elif button == 2:
        mouse.position = ReadChatPos
        time.sleep(0.3)
        mouse.click(Button.left, 1)
    elif button == 3:
        mouse.position = CollectDonationsPos
        time.sleep(0.3)
        mouse.click(Button.left, 1)
