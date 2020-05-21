# This script requires a Raspberry Pi 2, 3 or Zero. Circuit Python must
# be installed and it is strongly recommended that you use the latest
# release of Raspbian.

import time
import os
import board
import digitalio

print("press a button!")

button1 = digitalio.DigitalInOut(board.D23)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

button2 = digitalio.DigitalInOut(board.D24)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP
while True:
global playProcess
    # omxplayer -o local <file>
    # omxplayer -o hdmi <file>
    # omxplayer -o both <file>
    if not button1.value:
playProcess=subprocess.Popen(['omxplayer','/bp.mp3'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE, close_fds=True)
time.sleep(10)
playProcess.stdin.write('q')print('--- Cleared all existing mp3s. ---')

    if not button2.value:
        playProcess=subprocess.Popen(['omxplayer','/bd.mp3'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE, close_fds=True)
time.sleep(10)
playProcess.stdin.write('q')print('--- Cleared all existing mp3s. ---')

    time.sleep(.25)
