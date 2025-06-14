import pygame

pygame.init()
screen_width, screen_height = 500, 500 # Converted to lowercase

display_surface = pygame.display.set_mode((screen_width, screen_height)) # Converted to lowercase
pygame.display.set_caption('adding image and background image') # Converted string to lowercase

background_image = pygame.transform.scale(
    pygame.image.load('background.png').convert(),
    (screen_width, screen_height)) # Converted to lowercase

penguin_image = pygame.transform.scale(
    pygame.image.load('hello penguin.png').convert_alpha(), (200, 200))
penguin_rect = penguin_image.get_rect(center=(screen_width // 2, # Converted to lowercase
                                             screen_height // 2 - 30)) # Converted to lowercase

text = pygame.font.Font(None, 36).render('hello world', True, # Converted string to lowercase
                                         pygame.color('black')) # Converted to lowercase
text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 + 110)) # Converted to lowercase

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.blit(background_image, (0, 0))
        display_surface.blit(penguin_image, penguin_rect)
        display_surface.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    game_loop()
