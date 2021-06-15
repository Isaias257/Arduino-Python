import serial



arduino = serial.Serial('COM3', baudrate= 9600, timeout = 1)

while True:
    arduinoData = arduino.readline().decode('ascii')

