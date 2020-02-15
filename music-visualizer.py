import numpy as np
import sounddevice as sd
import pygame

# sounddevice variabels.
fs=44000
duration = 0.25 # seconds

pygame.init()


# Set up the drawing window
screenWitdh=800
screenHight=500
screen = pygame.display.set_mode([screenWitdh, screenHight])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with black
    screen.fill((0, 0, 0))

    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()

    N = len(myrecording)
    X = np.fft.rfft(myrecording)
    mul=11**5

    # calculating energi for the signal
    h1=mul*(np.real((1/1795)*np.sum((X[0*1795:1*1795]**2))))
    h2=mul*(np.real((1/1795)*np.sum((X[1*1795:2*1795]**2))))
    h3=mul*(np.real((1/1795)*np.sum((X[2*1795:3*1795]**2))))
    h4=mul*(np.real((1/1795)*np.sum((X[3*1795:4*1795]**2))))
    h5=mul*(np.real((1/1795)*np.sum((X[4*1795:5*1795]**2))))
    h6=mul*(np.real((1/1795)*np.sum((X[5*1795:6*1795]**2))))
    h7=mul*(np.real((1/1795)*np.sum((X[6*1795:7*1795]**2))))

    # Draws the bars.
    pygame.draw.rect(screen, (255,255,255),(20,screenHight,100,-h1))
    pygame.draw.rect(screen, (255,255,255),(130,screenHight,100,-h2))
    pygame.draw.rect(screen, (255,255,255),(240,screenHight,100,-h3))
    pygame.draw.rect(screen, (255,255,255),(350,screenHight,100,-h4))
    pygame.draw.rect(screen, (255,255,255),(460,screenHight,100,-h5))
    pygame.draw.rect(screen, (255,255,255),(570,screenHight,100,-h6))
    pygame.draw.rect(screen, (255,255,255),(680,screenHight,100,-h7))
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
