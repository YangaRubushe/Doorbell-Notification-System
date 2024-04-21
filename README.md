# Doorbell Notification System

## Overview

The Doorbell Notification System is a software solution designed to provide real-time notifications when a physical button, acting as a doorbell, is pressed. This system operates on a Raspberry Pi platform and utilizes Python scripts to detect button presses and send notifications to client devices. It enhances convenience for residential or commercial premises by allowing users to receive immediate alerts when someone rings the doorbell.

## Key Components

1. **Raspberry Pi**: Acts as the central control unit, detecting button presses and sending notifications.
2. **Button Sensor**: A physical button installed as a doorbell, triggering notifications when pressed.
3. **Python Scripts**: The system consists of server and client scripts enabling communication and notification delivery between the Raspberry Pi and external devices.

## Example of Operation

### Server Operation:

1. The server script runs on the Raspberry Pi, initializing GPIO pins to interface with the button sensor.
2. It establishes a socket server to listen for incoming connections from client devices.
3. Continuously, the server monitors the state of the button sensor, detecting button presses to trigger notification events.
4. Upon detecting a button press, the server sends a notification to all connected client devices, indicating that the doorbell has been rung.

### Client Operation:

1. The client script operates on external devices, such as smartphones or laptops, connecting to the server hosted on the Raspberry Pi.
2. It listens for incoming notifications from the server and displays them to the user in real-time.
3. Upon receiving a notification, the client provides visual or audible feedback to alert the user that the doorbell has been rung.

## Usage

To deploy the Doorbell Notification System:
- Execute the server script on the Raspberry Pi.
- Clients can interact with the system by executing the client script on their respective devices, connecting to the server to receive doorbell notifications.
- Users can press the button sensor installed as the doorbell to trigger real-time notifications on connected client devices.

## Safety Considerations

- Ensure proper installation and secure mounting of the button sensor to prevent damage or malfunction.
- Exercise caution when relying on the system for doorbell notifications, ensuring awareness of visitors at the door.

## Real-world Use Cases

Aside from doorbell notifications, the system can be adapted for various applications including:
- Home automation
- Industrial automation
- Gaming
- Data logging
- Medical equipment
- Educational projects
- Retail
- Transportation

## Documentation Purpose

This document provides detailed documentation covering the Doorbell Notification System’s planning, design, implementation, and any other relevant information. It includes instructions on hardware setup, software installation, code snippets.

For detailed instructions on setting up Raspberry Pi:
- Visit the official Raspberry Pi website: [Raspberry Pi](https://www.raspberrypi.org/)
- Follow the installation guide for your specific Raspberry Pi model: [Raspberry Pi Installation Guide](https://www.raspberrypi.org/documentation/installation/)
- Ensure to install the required operating system, such as Raspbian or Raspberry Pi OS, following the provided instructions.

Once you have set up your Raspberry Pi, proceed with the installation and configuration of the Doorbell Notification System as outlined in this documentation.


## Authors

- Yanga Rubushe
- Sibusiso Goodwell Skhosana
- Azwile Magwaza
- Liyema Heleba
- Siyasanga Mzimasi
- Sinoxolo Lomani
- Renate Mofu
- Zuhayr Adams
- Funanani Tracy Mugagadeli
- Loyiso Arnold Mlangeni