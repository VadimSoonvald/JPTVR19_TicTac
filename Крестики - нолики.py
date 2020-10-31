import pygame
pygame.init()

white     = (255, 255, 255)   #белый
black     = (0,0,0) #черный
red       = (255,0,0) #красный
size = [600, 800] #размер игрового поля
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Крестики-нолики")
screen.fill(white)

mas = ['None',1,2,3,4,5,6,7,8,9]
print(mas)

step = 0

def wins():
    if (mas[1] == mas [2] and mas[2] == mas [3]):
        pygame.draw.line(screen,red,(0,100),(600,100),7)
        pygame.display.flip()
        return True
    if (mas[4] == mas [5] and mas[5] == mas [6]):
        pygame.draw.line(screen,red,(0,300),(600,300),7)
        pygame.display.flip()
        return True
    if (mas[7] == mas [8] and mas[8] == mas [9]):
        pygame.draw.line(screen,red,(0,500),(600,500),7)
        pygame.display.flip()
        return True
    if (mas[1] == mas [4] and mas[4] == mas [7]):
        pygame.draw.line(screen,red,(100,0),(100,600),7)
        pygame.display.flip()
        return True
    if (mas[2] == mas [5] and mas[5] == mas [8]):
        pygame.draw.line(screen,red,(300,0),(300,600),7)
        pygame.display.flip()
        return True
    if (mas[3] == mas [6] and mas[6] == mas [9]):
        pygame.draw.line(screen,red,(500,0),(500,600),7)
        pygame.display.flip()
        return True
    if (mas[1] == mas [5] and mas[5] == mas [9]):
        pygame.draw.line(screen,red,(0,0),(800,800),7)
        pygame.display.flip()
        return True
    if (mas[3] == mas [5] and mas[5] == mas [7]):
        pygame.draw.line(screen,red,(0,600),(600,0),7)
        pygame.display.flip()
        return True

#Рисование сетки
    
pygame.draw.line(screen,black,(0,0),(600,0),7)
pygame.draw.line(screen,black,(600,0),(600,600),7)
pygame.draw.line(screen,black,(0,0),(0,600),7)

pygame.draw.line(screen,black,(0,200),(600,200),7)
pygame.draw.line(screen,black,(0,400),(600,400),7)
pygame.draw.line(screen,black,(0,600),(600,600),7)

pygame.draw.line(screen,black,(200,0),(200,600),7)
pygame.draw.line(screen,black,(400,0),(400,600),7)

#Открытие картинок
x2 = pygame.image.load("x1.png")
x2 = pygame.transform.scale(x2,(200,200))

o = pygame.image.load("o1.png")
o = pygame.transform.scale(o,(200,200))

pygame.display.flip() #обновление экрана

#основной код
done = False
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if wins():
                break
            elif step == 9:
                print('Ничья')
                text_1 = pygame.font.Font(None, 50)
                text_2 = text_1.render("Draw!", 1, [255, 0, 0])
                screen.blit(text_2, [205, 750])
                pygame.display.flip()
                break
            else:
                x, y = event.pos
            
            if (x > 0 and y > 0 and x < 200 and y < 200):
                kv = 1
                px = 0
                py = 0
                print(x,y,kv)
                
                if mas[1] == 1:
                    step = step + 1
                    print(step)
                    if step % 2 == 1:
                        mas[1] = "X"
                        screen.blit(x2,(px,py))
                    else:
                        mas[1] = "O"
                        screen.blit(o,(px,py))
                pygame.display.flip()
            
            if (x > 200 and y > 0 and x < 400 and y < 200):
                kv = 2
                px = 200
                py = 0
                print(x,y,kv)
                
                if mas[2] == 2:
                    step = step + 1
                    print(step)
                    if step % 2 == 1:
                        mas[2] = "X"
                        screen.blit(x2,(px,py))
                    else:
                        mas[2] = "O"
                        screen.blit(o,(px,py))
                pygame.display.flip()
                print(x,y,"kv = ",kv)
            if (x > 400 and y > 0 and x < 600 and y < 200):
                kv = 3
                px = 400
                py = 0
                print(x,y,kv)
                
                if mas[3] == 3:
                    step = step + 1
                    print(step)
                    if step % 2 == 1:
                        mas[3] = "X"
                        screen.blit(x2,(px,py))
                    else:
                        mas[3] = "O"
                        screen.blit(o,(px,py))
                pygame.display.flip()
                print(x,y,"kv = ",kv)
            if (x > 0 and y > 200 and x < 200 and y < 400):
                kv = 4
                px = 0
                py = 200
                print(x,y,kv)
                
                if mas[4] == 4:
                    step = step + 1
                    print(step)
                    if step % 2 == 1:
                        mas[4] = "X"
                        screen.blit(x2,(px,py))
                    else:
                        mas[4] = "O"
                        screen.blit(o,(px,py))
                pygame.display.flip()
                print(x,y,"kv = ",kv)
            if (x > 200 and y > 200 and x < 400 and y < 400):
                kv = 5
                px = 200
                py = 200
                print(x,y,kv)
                
                if mas[5] == 5:
                    step = step + 1
                    print(step)
                    if step % 2 == 1:
                        mas[5] = "X"
                        screen.blit(x2,(px,py))
                    else:
                        mas[5] = "O"
                        screen.blit(o,(px,py))
                pygame.display.flip()
                print(x,y,"kv = ",kv)
            if (x > 400 and y > 200 and x < 600 and y < 400):
                kv = 6
                px = 400
                py = 200
                print(x,y,kv)
                
                if mas[6] == 6:
                    step = step + 1
                    print(step)
                    if step % 2 == 1:
                        mas[6] = "X"
                        screen.blit(x2,(px,py))
                    else:
                        mas[6] = "O"
                        screen.blit(o,(px,py))
                pygame.display.flip()
                print(x,y,"kv = ",kv)
            if (x > 0 and y > 400 and x < 200 and y < 600):
                kv = 7
                px = 0
                py = 400
                print(x,y,kv)
                
                if mas[7] == 7:
                    step = step + 1
                    print(step)
                    if step % 2 == 1:
                        mas[7] = "X"
                        screen.blit(x2,(px,py))
                    else:
                        mas[7] = "O"
                        screen.blit(o,(px,py))
                pygame.display.flip()
                print(x,y,"kv = ",kv)
            if (x > 200 and y > 400 and x < 400 and y < 600):
                kv = 8
                px = 200
                py = 400
                print(x,y,kv)
                
                if mas[8] == 8:
                    step = step + 1
                    print(step)
                    if step % 2 == 1:
                        mas[8] = "X"
                        screen.blit(x2,(px,py))
                    else:
                        mas[8] = "O"
                        screen.blit(o,(px,py))
                    print(mas)
                pygame.display.flip()
                print(x,y,"kv = ",kv)
            if (x > 400 and y > 400 and x < 600 and y < 600):
                kv = 9
                px = 400
                py = 400
                print(x,y,kv)
                
                if mas[9] == 9:
                    step = step + 1
                    print(step)
                    if step % 2 == 1:
                        mas[9] = "X"
                        screen.blit(x2,(px,py))
                    else:
                        mas[9] = "O"
                        screen.blit(o,(px,py))
                    print(mas)
                pygame.display.flip()
                print(x,y,"kv = ",kv)
        if step >= 5:
            if wins() == True:
                if step % 2 == 1:
                    text = pygame.font.Font(None, 50)
                    text_1 = text.render("Winner - X", 1, [255, 0, 0])
                    screen.blit(text_1, [205, 750])

                else:
                    text = pygame.font.Font(None, 50)
                    text_1 = text.render("Winner - О", 1, [255, 0, 0])
                    screen.blit(text_1, [205, 750])
                
pygame.quit()