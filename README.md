# Scalable IoT Project with Real-Time Visualization in Node-RED - Proyecto IoT Escalable con Visualización en Node-RED

# English:

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

# Spanish:

## Descripción
Este proyecto implementa una plataforma IoT escalable que cubre desde la **capa física** hasta la **capa de transporte de datos**, con almacenamiento en **MySQL** y visualización en tiempo real utilizando **Node-RED**. El sistema recoge datos de sensores conectados a un microcontrolador **ESP32**, los transmite mediante el protocolo **MQTT**, los almacena en una base de datos MySQL, y presenta los datos en un **Dashboard interactivo**.

## Objetivos del Proyecto
- **Implementar un sistema IoT escalable** y accesible visualmente.
- **Transmitir datos desde microcontroladores ESP32** a un servidor mediante **MQTT**.
- Crear un **Dashboard en Node-RED** para visualizar los datos de sensores en tiempo real a través de gráficos e indicadores personalizados.

## Metodología
El proyecto se dividió en varias fases:
1. **Configuración del microcontrolador ESP32** para la recolección de datos.
2. **Transmisión de datos mediante MQTT** para la eficiencia en el uso de ancho de banda.
3. **Desarrollo de Backend en Python**, que conecta MQTT con la base de datos **MySQL**.
4. **Creación del Dashboard en Node-RED**, donde se visualizan los datos en tiempo real.

## Implementación

### 1. Configuración del ESP32
El ESP32 fue configurado para leer datos de sensores conectados a sus pines, utilizando el entorno de desarrollo **Wokwi**.

### 2. Capa de Transporte de Datos con MQTT
El protocolo **MQTT** se utilizó para transmitir los datos del ESP32 al servidor. Se configuró un servidor **Mosquitto** MQTT para gestionar los mensajes entrantes.

### 3. Backend y Conexión con MySQL
Se desarrolló un backend en **Python** con la biblioteca **Paho-MQTT**, que se suscribe a los tópicos de datos del ESP32 y almacena los datos en **MySQL** sin utilizar PHPMyAdmin, maximizando la eficiencia.

### 4. Escalabilidad y Optimización
La arquitectura modular permite agregar nuevos nodos ESP32 sin afectar la estabilidad. La base de datos y el servidor **MQTT** fueron optimizados para soportar el crecimiento del sistema.

### 5. Dashboard en Node-RED
Se desarrolló un **Dashboard interactivo** en Node-RED para visualizar los datos en tiempo real. Entre sus funcionalidades destacan:
- **Gráficos en tiempo real** con **ui_chart**, **ui_gauge**, y **ui_text**.
- **Notificaciones por umbral** para alertar al usuario sobre valores críticos de temperatura y humedad.
- Panel para **selección de métricas** (en desarrollo).

## Código
### ESP32
- [Proyecto Wokwi](https://wokwi.com/projects/408634800407273473)


