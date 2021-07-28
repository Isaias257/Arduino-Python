import serial
import time
import pygame

arduino = serial.Serial("COM3", baudrate=9600, timeout=1)
time.sleep(1)

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")
x = 50
y = 50
width = 40
height = 60
vel = 1

run = True
# strip the incoming data / causes errors without it
while run:
    try:
        arduinoData = arduino.readline().decode('ascii')
        arduinoData = arduinoData.strip()
        arduinoData = int(arduinoData)
    except ValueError:
        pass
    print(arduinoData)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    if arduinoData == 1:
        y -= vel

    win.fill((0, 0, 0))  # Fills the screen with black
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

