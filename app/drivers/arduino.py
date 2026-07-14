import serial
import time

PORTA = "COM5"      # vamos trocar pela sua porta
BAUDRATE = 9600

arduino = serial.Serial(PORTA, BAUDRATE)

time.sleep(2)


def enviar_comando(comando):

    arduino.write(f"{comando}\n".encode())

    print(f"📡 Comando enviado: {comando}")