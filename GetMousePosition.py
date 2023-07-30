from pynput.mouse import Controller
import time

mouse = Controller()

time.sleep(5)

for i in range(3):
    print('The current pointer position is {0}'.format(
    mouse.position))
    time.sleep(5)