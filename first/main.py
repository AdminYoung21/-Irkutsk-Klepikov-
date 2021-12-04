# подключение библиотеки
import pygame
try:
    width = int(input())
    height = int(input())
    print("1")
except ValueError as v:
    print("Неправильный формат ввода")
    exit()

SIZE = (width, height)
BACKGROUND = (0, 0, 0)


def draw(screen):
    print("1")
    screen.fill(BACKGROUND)
    pygame.draw.line(screen, (255, 255, 255), start_pos=(0, 0), end_pos=SIZE, width=5)
    pygame.draw.line(screen, (255, 255, 255), start_pos=(0, height), end_pos=(width, 0), width=5)

if __name__ == '__main__':
    # инициализация
    pygame.init()
    pygame.display.set_caption("Cross")
    screen = pygame.display.set_mode(size=SIZE)
    # цикл работы игры
    while True:
        print("1")
        if pygame.event.wait().type == pygame.QUIT:
            break
        draw(screen)
        pygame.display.flip()
    pygame.quit()