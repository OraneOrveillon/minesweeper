import pygame
import pygame_gui
from pygame_gui.elements import UIVerticalScrollBar

if __name__ == '__main__':
    pygame.init()

    pygame.display.set_caption('Quick Start')
    window_surface = pygame.display.set_mode((800, 600))

    background = pygame.Surface((800, 600))
    background.fill(pygame.Color('#FFFFFF'))

    manager = pygame_gui.UIManager((800, 600))
    clock = pygame.time.Clock()

    UIVerticalScrollBar(window_surface.get_rect(), 100).show()

    is_running = True

    while is_running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            manager.process_events(event)

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)

        pygame.display.update()
