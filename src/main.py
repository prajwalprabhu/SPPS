
import pygame
uwon = 0
cwon = 0
comp = "none"


def message(text, pos, color, size):
    font = pygame.font.SysFont(None, size)
    img = font.render(text, True, color)
    screen.blit(img, pos)


def win():
    global cwon
    global uwon
    global comp
    win = pygame.image.load("img/win.jpg")
    won = True
    while won:
        screen.blit(win, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                won = False
                pygame.quit()
                quit()
        pygame.draw.rect(screen, Red, (200, 200, 100, 50))
        message("Retry", (210, 210), size=40, color=Blue)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 200 < mouse[0] < 300 and 200 < mouse[1] < 250:
            if click[0]:
                cwon = 0
                uwon = 0
                comp = "none"
                main()

        pygame.display.flip()


def lose():
    global cwon, uwon, comp
    lose = pygame.image.load("img/lose.webp")
    lost = True
    while lost:
        screen.blit(lose, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lost = False
                pygame.quit()
                quit()
        pygame.draw.rect(screen, Red, (200, 200, 100, 50))
        message("Retry", (210, 210), size=40, color=Blue)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 200 < mouse[0] < 300 and 200 < mouse[1] < 250:
            if click[0]:
                cwon = 0
                uwon = 0
                comp = "none"
                main()

        pygame.display.flip()


def select(user):
    global uwon
    global cwon
    global comp
    from random import randrange
    from time import sleep
    options = ["Stone", "Paper", "Pencil", "Sissor"]
    select = options[randrange(0, 4)]

    comp = select
# pygame.draw.rect(screen,Red,(200,200,100,50))
# message("{}".format(select),(210,210),Red,40)
# pygame.display.flip()

    if select == "Stone":
        if options[user] == "Paper":
            uwon += 1
        if options[user] == "Sissor" or options[user] == "Pencil":
            cwon += 1

    elif select == "Paper":
        if options[user] == "Stone":
            cwon += 1
        elif options[user] == "Pencil" or options[user] == "Sissor":
            uwon += 1
    elif select == "Pencil":
        if options[user] == "Stone" or options[user] == "Sissor":
            uwon += 1
        elif options[user] == "Paper":
            cwon += 1
    elif select == "Sissor":
        if options[user] == "Stone":
            uwon += 1
        elif options[user] == "Pencil" or options[user] == "Paper":
            cwon += 1
    if uwon == 5:
        win()
        uwon = 0
        cwon = 0
    if cwon == 5:
        lose()


Red = (255, 0, 0)
l_blue = (0, 0, 150)
Blue = (0, 0, 255)
Green = (0, 255, 0)

pygame.init()
screen = pygame.display.set_mode((500, 500))


def main():

    running = True
    back = pygame.image.load(r"img/back.jpg")
    while running:
        screen.blit(back, (0, 0))
        pygame.draw.rect(screen, Red, (350, 300, 100, 50))
        message("Stone", (370, 310), Blue, 40)
        pygame.draw.rect(screen, Blue, (200, 300, 100, 50))
        message("Paper", (220, 310), Red, 40)
        pygame.draw.rect(screen, Green, (50, 300, 100, 50))
        message("Pencil", (60, 310), Blue, 40)
        pygame.draw.rect(screen, Green, (200, 400, 100, 50))
        message("Scissor", (200, 410), Red, 40)
        message("Computer's chioce:", (0, 120), Red, 40)
        pygame.draw.rect(screen, Red, (200, 150, 100, 50))
        message("{}".format(comp), (210, 160), Blue, 40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            # print(mouse)
        # options=["Stone","Paper","Pencil","Sissor"]

            if 350 < mouse[0] < 450 and 300 < mouse[1] < 350:
                if click[0]:
                    select(0)

            if 200 < mouse[0] < 300 and 300 < mouse[1] < 350:
                if click[0]:
                    select(1)
            if 50 < mouse[0] < 150 and 300 < mouse[1] < 350:
                if click[0]:
                    select(2)
            if 200 < mouse[0] < 300 and 400 < mouse[1] < 450:
                if click[0]:
                    select(3)
        message("User={}".format(uwon), (0, 0), Blue, 60)
        message("Computer={}".format(cwon), (0, 70), Red, 60)
        message("Your Choice :", (0, 250), Blue, 40)
        pygame.display.flip()


main()
