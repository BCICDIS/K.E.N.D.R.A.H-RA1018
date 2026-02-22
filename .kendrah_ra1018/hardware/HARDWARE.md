# KENDRAH — Hardware

**Module:** `.kendrah-ra1018/Hardware/`
**Domain:** Hardware Communication, Sensing, and Physical System Interaction
**Status:** Active

---

## Overview

The Hardware module defines KENDRAH's ability to communicate with, monitor, control, and interact with physical hardware components and devices. This includes the host machine's own hardware (CPU, GPU, RAM, storage, peripherals), connected external hardware (sensors, microcontrollers, IoT devices, embedded systems), and any hardware accessible via standard communication protocols.

KENDRAH bridges the gap between software intelligence and the physical world.

---

## Hardware Categories

### Host Machine Hardware
- **CPU:** Monitor clock speed, core usage, temperature, load per core, power state, thermal throttling
- **GPU:** Monitor GPU utilization, VRAM usage, temperature, driver version, CUDA availability
- **RAM:** Monitor total, used, available, swap usage; identify memory leaks in running processes
- **Storage:** Monitor read/write speeds, health (S.M.A.R.T.), capacity, IOPS
- **Network Interface:** Monitor throughput, packet loss, interface state, MAC/IP assignments
- **Power:** Monitor battery state (laptops), power draw, UPS status
- **Display:** Detect connected monitors, resolution, refresh rate, display arrangement

### Peripherals & Input Devices
- **Keyboards & Mice:** Detect, map, and automate input device interactions
- **Webcams & Microphones:** Access and stream audio/video from connected devices
- **Printers & Scanners:** Interface with printing and scanning hardware
- **USB Devices:** Detect connected USB devices, read device descriptors, communicate via USB HID or serial

### Embedded Systems & Microcontrollers
- **Arduino:** Read sensors, control actuators via serial communication (pyserial)
- **Raspberry Pi:** Direct GPIO control, I2C, SPI, UART communication
- **ESP32 / ESP8266:** WiFi-enabled IoT microcontroller communication
- **General Serial Devices:** Any device communicating over RS-232, UART, or USB-Serial

### IoT & Sensor Devices
- **Temperature & Humidity Sensors:** Read environmental data from connected sensors
- **Motion Sensors / PIR:** Detect and log motion events
- **Camera Modules:** Capture images or video from camera hardware
- **GPS Modules:** Read location data from GPS hardware
- **Accelerometers / Gyroscopes:** Read orientation and motion data (IMU)
- **Smart Home Devices:** Interface with Zigbee, Z-Wave, or Wi-Fi smart devices via hub APIs

### Industrial & Specialized Hardware
- **PLCs (Programmable Logic Controllers):** Interface via Modbus, OPC-UA, or proprietary protocols
- **CNC / Robotic Systems:** Send G-code commands, read encoder feedback
- **Laboratory Instruments:** Interface with lab equipment via GPIB, RS-232, or vendor APIs
- **Medical Devices:** Read from authorized medical monitoring hardware via defined protocols

---

## Communication Protocols

| Protocol   | Use Case                                                         |
|------------|------------------------------------------------------------------|
| **USB/HID**| Human interface devices, mass storage, custom USB devices       |
| **Serial (UART/RS-232)** | Arduino, microcontrollers, embedded systems        |
| **I2C**    | Short-distance sensor communication (temperature, IMU, etc.)    |
| **SPI**    | High-speed sensor and memory communication                      |
| **GPIO**   | Direct digital I/O on Raspberry Pi and similar boards           |
| **Bluetooth** | BLE and Classic Bluetooth devices                            |
| **Wi-Fi/HTTP** | IoT devices with network connectivity                       |
| **MQTT**   | Lightweight IoT messaging protocol                              |
| **Modbus** | Industrial equipment and PLCs                                   |
| **CAN Bus**| Automotive and industrial control systems                       |

---

## Core Capabilities

### Hardware Monitoring
- Real-time monitoring of host hardware metrics
- Alert on thresholds: CPU > 90%, temperature > 85°C, disk < 5GB free
- Log hardware events to a time-series format for trend analysis

### Hardware Control
- Write to GPIO pins (Raspberry Pi)
- Send serial commands to connected microcontrollers
- Control smart home devices via hub APIs (Home Assistant, etc.)
- Trigger hardware actuators: motors, relays, LEDs, displays

### Sensor Data Acquisition
- Poll sensors on a configurable interval
- Stream sensor data to files, databases, or dashboards
- Apply filters and transformations to raw sensor data
- Trigger alerts or actions based on sensor readings

### Hardware Diagnostics
- Run diagnostics on connected hardware
- Check for driver errors, device conflicts, or communication failures
- Generate a full hardware inventory report

---

## Tools & Libraries

```python
import psutil           # Host hardware monitoring
import GPUtil           # GPU monitoring
import serial           # Serial/UART communication (pyserial)
import smbus2           # I2C communication
import RPi.GPIO         # Raspberry Pi GPIO
import hid              # USB HID device communication
import paho.mqtt.client # MQTT IoT communication
import bleak            # Bluetooth Low Energy
import pyusb            # USB device communication
```

---

## Commands

```
/hardware status                          — Full host hardware health report
/hardware monitor [component]            — Live monitoring of a hardware component
/hardware alert --cpu [threshold]        — Set CPU usage alert threshold
/hardware alert --temp [threshold]       — Set temperature alert threshold
/hardware list-devices                   — List all detected connected devices
/hardware serial connect [port] [baud]   — Connect to a serial device
/hardware serial send [port] "[command]" — Send a command to a serial device
/hardware gpio set [pin] [HIGH|LOW]      — Set a GPIO pin (Raspberry Pi)
/hardware gpio read [pin]                — Read a GPIO pin state
/hardware sensor read [device]           — Read data from a connected sensor
/hardware diagnose                       — Run full hardware diagnostic
/hardware inventory                      — Generate hardware inventory report
```
