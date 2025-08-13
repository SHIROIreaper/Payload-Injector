# Pico W Payload Injector (Educational Project)

> **Disclaimer:**  
> This project is for **educational and authorized testing purposes only**.  
> Do **not** use it on devices, systems, or networks without explicit permission from the owner.  
> The author is **not responsible** for any misuse or illegal activities.

## Overview

The **Pico W Payload Injector** is a USB HID device built on the Raspberry Pi Pico W microcontroller.  
It emulates a USB keyboard to deliver pre-defined keystroke payloads to a target machine automatically.  

This project is intended for:
- Cybersecurity education
- Authorized penetration testing
- Demonstrating the risks of malicious USB devices (e.g., BadUSB attacks)

## Features

- **Plug-and-play** HID emulation
- **Wi-Fi control** (work in progress) for remote payload selection
- **Multiple payload storage** with quick switching
- **Custom payload scripting** using MicroPython or CircuitPython
- **Status indicators** via onboard LED

## Requirements

### Hardware
- Raspberry Pi Pico W
- Micro-USB cable (data capable)
- Host machine (Windows/Linux/macOS)

### Software
- CircuitPython or MicroPython installed on Pico W
- Python 3.x

