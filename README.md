# Scalable IoT Project with Real-Time Visualization in Node-RED - Proyecto IoT Escalable con Visualización en Node-RED

## Description
This project implements a **scalable IoT platform** covering everything from the **physical layer** to the **data transport layer**, with **MySQL** storage and real-time visualization using **Node-RED**. The system collects data from sensors connected to an **ESP32 microcontroller**, transmits it using the **MQTT** protocol, stores it in a MySQL database, and displays it through an **interactive dashboard**.

## Project Objectives
- **Implement a scalable IoT system** with accessible visual representation.
- **Transmit data from ESP32 microcontrollers** to a server via **MQTT**.
- Create a **Node-RED dashboard** to visualize sensor data in real time using custom charts and indicators.

## Methodology
The project was divided into several phases:
1. **ESP32 microcontroller setup** for data collection.
2. **Data transmission using MQTT** for bandwidth-efficient communication.
3. **Backend development in Python**, connecting MQTT to a **MySQL** database.
4. **Dashboard creation in Node-RED**, to display the data in real time.

## Implementation

### 1. ESP32 Setup
The ESP32 was configured to read sensor data through its pins using the **Wokwi** development environment.

### 2. Data Transport Layer with MQTT
The **MQTT** protocol was used to send the data from the ESP32 to the server. A **Mosquitto** MQTT broker was set up to handle incoming messages.

### 3. Backend and MySQL Connection
A backend was developed in **Python** using the **Paho-MQTT** library. It subscribes to ESP32 data topics and stores the data in **MySQL** without using PHPMyAdmin, maximizing performance.

### 4. Scalability and Optimization
The modular architecture allows new ESP32 nodes to be added without impacting stability. The **database** and **MQTT server** were optimized to support system growth.

### 5. Node-RED Dashboard
An **interactive dashboard** was built in Node-RED to display real-time data. Its features include:
- **Real-time charts** using **ui_chart**, **ui_gauge**, and **ui_text**.
- **Threshold-based alerts** to notify users of critical temperature and humidity values.
- A panel for **metric selection** (currently in development).

## Code
### ESP32
- [Wokwi Project](https://wokwi.com/projects/408634800407273473)




