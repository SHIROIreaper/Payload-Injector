import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# Initialize keyboard
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

# Wait a moment after plugging in to let the OS recognize the device
time.sleep(3)

url = "https://vyshnav-portfolio.web.app"

# --- Windows attempt ---
kbd.send(Keycode.WINDOWS, Keycode.R)  # Open Run dialog
time.sleep(0.5)
layout.write("chrome " + url)
kbd.send(Keycode.ENTER)
time.sleep(2)

# --- Linux attempt ---
kbd.send(Keycode.CONTROL, Keycode.ALT, Keycode.T)  # Open terminal
time.sleep(1)
layout.write("firefox " + url)
kbd.send(Keycode.ENTER)
