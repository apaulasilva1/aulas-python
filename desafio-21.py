import pygame
pygame.init()
pygame.mixer.music.load('mymusic.mp3')
pygame.mixer.music.play()
pygame.event.wait()