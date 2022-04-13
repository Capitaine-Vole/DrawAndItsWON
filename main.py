import os
import sys
import random
import pygame
import time
from files import *

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Déssiné c'est gagné")
icon = pygame.image.load("icon.png").convert_alpha()
pygame.display.set_icon(icon)

words = ["un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix"]

def randomed(thing):
    p = random.randint(1, len(thing))
    return p

def choose(thing):
    return words[thing]

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                status = 1
        
        screen.blit(self.image, (self.rect.x, self.rect.y))

genIMG = pygame.image.load('new_word.png').convert_alpha()
genBTN = Button(220, 100, genIMG)
greyIMG = pygame.image.load('grey_bc.png').convert_alpha()
greyBTN = Button(220, 100, greyIMG)

font = pygame.font.Font('freesansbold.ttf', 32)

choosenWord = font.render(choose(randomed(words)-1), True, (0, 0, 0), (202, 228, 241))
textRect = choosenWord.get_rect()
textRect.center = (620 /2, 300)
screen.blit(choosenWord, textRect)

#files

checkFileExistance("words.txt")
writeFile("words.txt", (input("Entrez les mots que vous voulez rajouter dans le fichier et séparez les par des ';' :\n").split(";")))
print(readFile("words.txt"))
removeWords("words.txt", input("LEs mots à enlever :\n"))
print(readFile("words.txt"))


#end of files

run = True

while run == True:

    screen.fill((202, 228, 241))

    
    genBTN.draw()

    for event in pygame.event.get() :

        if event.type == pygame.QUIT :

            pygame.quit()

            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if 220 <= mouse[0] <= 420 and 100 <= mouse[1] <= 200:
                choosenWord = font.render(choose(randomed(words)-1), True, (0, 0, 0), (202, 228, 241))
                textRect = choosenWord.get_rect()
                textRect.center = (620 /2, 300)
                greyBTN.draw()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                choosenWord = font.render(choose(randomed(words)-1), True, (0, 0, 0), (202, 228, 241))
                textRect = choosenWord.get_rect()
                textRect.center = (620 /2, 300)
                greyBTN.draw()
                

        screen.blit(choosenWord, textRect)
        pygame.display.update()
