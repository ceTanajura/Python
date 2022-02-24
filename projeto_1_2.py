import pygame
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#Pino de controle da bomba
GPIO.setup(21, GPIO.OUT)

def init():
    pygame.init()
    win = pygame.display.set_mode((100,100))

def getKey(KeyName):
    ans = False
    for eve in pygame.event.get():pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame,'K_{}'.format(KeyName))
    if keyInput [myKey]:
        ans = True
    pygame.display.update()
    return ans

def main():
    if getKey('a'):
        print('Key a was pressed')
        GPIO.output(21,1)
    if getKey('b'):
        print('Key b was pressed')
        GPIO.output(21,0)
       
if __name__ == '__main__':
    init()
    while True:
        main()