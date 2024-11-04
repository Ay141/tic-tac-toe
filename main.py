import pygame
import random

pygame.init()


def draw_grid(scr):
    pygame.draw.line(scr, (0, 0, 0), (100, 0), (100, 300), 5)
    pygame.draw.line(scr, (0, 0, 0), (200, 0), (200, 300), 5)
    pygame.draw.line(scr, (0, 0, 0), (0, 100), (300, 100), 5)
    pygame.draw.line(scr, (0, 0, 0), (0, 200), (300, 200), 5)


# будет отрисовывать все х и 0
def draw_tic_tac_toe(scr, items):
    for i in range(3):
        for j in range(3):
            if items[i][j] == "0":
                pygame.draw.circle(scr, (255, 0, 0), (j * 100 + 50, i * 100 + 50), 45)
            elif items[i][j] == "x":
                pygame.draw.line(scr, (31, 31, 33), (j * 100 + 5, i * 100 + 5), (j * 100 + 95, i * 100 + 95), 5)
                pygame.draw.line(scr, (31, 31, 33), (j * 100 + 95, i * 100 + 5), (j * 100 + 5, i * 100 + 95), 5)


def get_win_check(fd, symbol):
    flag_win = False
    for line in fd:
        if line.count(symbol) == 3:
            flag_win = True
    for i in range(3):
        if i in range(3):
            if fd[1][i] == fd[0][i] == fd[2][i] == symbol:
                flag_win = True
        if fd[0][0] == fd[1][1] == fd[2][2] == symbol:
            flag_win = True
        if fd[0][2] == fd[1][1] == fd[2][0] == symbol:
            flag_win = True
        return flag_win


SCREEN_SIZE = (300, 300)

windown = pygame.display.set_mode(SCREEN_SIZE)
screen = pygame.Surface(SCREEN_SIZE)

pygame.display.set_caption("tic tac toe")
screen.fill((53, 87, 143))

field = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]

mainloop = True
game_over = False

while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            pos = pygame.mouse.get_pos()
            if field[pos[1] // 100][pos[0] // 100] == "":
                field[pos[1] // 100][pos[0] // 100] = "x"
                # Bot
                x, y = random.randint(0, 2), random.randint(0, 2)
                while field[x][y] != "":
                    x, y = random.randint(0, 2), random.randint(0, 2)
                field[x][y] = "0"

            # Результат проверки выигрыша "0" или "х"
            player_win = get_win_check(field, "x")
            ai_win = get_win_check(field, "0")
            if player_win or ai_win: # Проверка выигрыша каждой из сторон
                game_over = True
                if player_win:
                    pygame.display.set_caption("Вы выйграли!")
            else:
                pygame.display.set_caption("Бот выграл!")
        elif field[0].count("x") + field[0].count("0") + field[1].count("x") + \
                field[1].count("0") + field[2].count("x") + field[2].count("0") == 8:
            game_over = True
            pygame.display.set_caption("Ничья")

    draw_tic_tac_toe(screen, field)
    draw_grid(screen)
    windown.blit(screen, (0, 0))
    pygame.display.update()

