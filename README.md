# 🚀 Scalable IoT Project with Real-Time Visualization in Node-RED  
### 🛰️ End-to-End IoT System with MQTT, MySQL & Live Dashboards

---

## 📌 Description

This project implements a **scalable IoT platform** covering everything from the **physical layer** to the **data transport layer**, featuring **MySQL** storage and real-time visualization using **Node-RED**.

Sensor data is collected via an **ESP32 microcontroller**, transmitted using the **MQTT** protocol, stored in a **MySQL** database, and displayed through an **interactive dashboard** built with Node-RED.

---

## 🎯 Project Objectives

- 🛠️ Build a **modular and scalable IoT system**.
- 📡 **Transmit sensor data** from ESP32 to the backend via **MQTT**.
- 📊 **Visualize real-time data** using a **custom Node-RED dashboard**.

---

## 🔍 Methodology

The project was developed through the following phases:

1. **ESP32 microcontroller setup** for sensor data acquisition.
2. **MQTT-based data transmission** for efficient messaging.
3. **Backend in Python**, connecting MQTT to **MySQL**.
4. **Node-RED dashboard** creation for real-time data visualization.

---

## ⚙️ Implementation

### 🧩 1. ESP32 Setup
- The **ESP32** was configured to read sensor data via GPIO pins using the **Wokwi** online simulator.

### 🔗 2. Data Transport Layer with MQTT
- The **MQTT protocol** was used to send sensor data to the server.
- A **Mosquitto MQTT broker** was implemented to manage message handling and topic subscriptions.

### 🐍 3. Backend in Python + MySQL Integration
- A backend script was written in **Python** using the **Paho-MQTT** library.
- The backend subscribes to ESP32 topics and writes the incoming data directly to **MySQL**, without the use of PHPMyAdmin for improved performance.

### 📈 4. Scalability & Optimization
- The system is **modular and easily extendable**: new ESP32 nodes can be added without affecting system stability.
- **MQTT broker** and **database performance** were tuned to support scaling.

### 🖥️ 5. Node-RED Dashboard
An interactive dashboard was built using **Node-RED**, with the following features:

- 📉 **Real-time charts** using `ui_chart`, `ui_gauge`, and `ui_text`.
- 🚨 **Threshold-based alerts** for temperature and humidity anomalies.
- 📋 A **metric selection panel** *(currently under development)*.

---

## 🧪 Code & Simulation

### 🔌 ESP32 (Wokwi Simulation)
- [Wokwi Project Link](https://wokwi.com/projects/408634800407273473)

---




