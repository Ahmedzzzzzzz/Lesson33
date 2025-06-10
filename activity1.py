#import necessary libraries
import pygame

# initialize required modules
pygame.init()

# setup window geometry
screen = pygame.display.set_mode((400,400))

#create a loop to run till the game is quit by the user
done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        
    pygame.display.flip()