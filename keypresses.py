import pygame

def detectKeyPresses(event_get, running):
    for event in event_get:
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    keys = pygame.key.get_pressed()  # checking pressed keys