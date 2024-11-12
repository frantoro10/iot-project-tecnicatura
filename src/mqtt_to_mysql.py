import paho.mqtt.client as mqtt
import mysql.connector
import json

#Datos de conexión a la base de datos MySQL que luego se utilizan en la función save_to_database donde se hace la conexión. Formato JSON
db_config = {
    'user': 'root',
    'password': '420926',
    'host': 'localhost', #IP donde esta alojado el servidor
    'database': 'iot_data',
}

#Función que se ejecuta cuando se conecta al broker MQTT
def on_connect(client, userdata, flags, rc):
    print(f"Conectado al broker MQTT con codigo: {rc}")
    #Suscribirnos al topico (topic) donde subi los datos en el ESP32
    client.subscribe("iot/sensors/dht22")

#Función que se ejecuta cuando se recibe un mensaje desde el broker MQTT
def on_message(client, userdata, msg):
    print(f"Mensaje recibido: {msg.payload.decode()}") #Uso de metodo decode, ya que los datos vienen en binario usando "enconde()" o b""

    #Convertir el mensaje recibido en datos de temp y humedad.
    message = msg.payload.decode() #Payload, significa recibir el mensaje principal. No los metadatos como topic, hora, etc.
    try: 
        data = message.split(",") #Separar o dividir en comas cada string
        temp = float(data[0].split(":")[1].strip().replace("°C", ""))
        hum = float(data[1].split(":")[1].strip().replace("%", ""))
        
        #Llamamos funcion para guardar los datos a la base de datos.
        save_to_database(temp,hum)
    except Exception as e:
        print(f"Error procesando el mensaje: {e}") 

#Función para guardar los datos en la base de datos, que luego se llama en la función on_message.
def save_to_database(temp,hum):
    try:
        #Conexión a base de datos
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        #Insertar los datos
        query = "INSERT INTO sensor_data (temperature, humidity) VALUES (%s, %s)"
        cursor.execute(query, (temp,hum))

        #Confirmar datos
        connection.commit()
        print(f"Datos guardados: Temperatura= {temp}, Humedad = {hum}")

    #Excepción dentro del bloque try, para capturar error.
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    #Cierre de conexión    
    finally:
        cursor.close()
        connection.close()    

#Configuración del cliente MQTT
client = mqtt.Client()

# Vincular las funciones de conexión y recepción de mensajes
client.on_connect = on_connect
client.on_message = on_message

#Conectar al broker MQTT.
client.connect("broker.hivemq.com", 1883, 60)

#Mantener la conexión y esperar los mensajes
client.loop_forever()