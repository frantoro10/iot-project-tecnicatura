# Proyecto IoT Escalable con Visualización en Node-RED

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


