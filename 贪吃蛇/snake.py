def main():
    import pygame
    from PIL import Image,ImageDraw
    import os
    global a
    import time
    import random
    import sys
    import os
    pygame.init()
    global timer
    timer = 60
    global screen
    screen = pygame.display.set_mode([800,600])
    pygame.display.set_caption("贪吃蛇")
    global draw_string
    draw_string = ''
    a = []
    global snake
    snake=[[0,0],[0,1],[0,2]]
    food=[random.randint(0,29),random.randint(0,29)]
    for i in range(30):
        a.append([])
        for x in range(30):
            a[i].append(" ")
    def printsnake(li,t):
        c=""
        for x in li:
            for n in x:
                c += str(n)
        image_dict={"*":"","O":'蛇头.jpg','+':'蛇身.jpg',"@":'食物.jpg'," ":""}
        image_names = []
        for x in c:
            image_names.append(image_dict[x])
        # 简单的对于参数的设定和实际图片集的大小进行数量判断
        to_image = Image.open('背景.png') #创建一个新图
        # 循环遍历，把每张图片按顺序粘贴到对应位置上
        for y in range(1, 31):
            for x in range(1, 31):
                if image_names[(x-1)+(y-1)*30] == "":
                    continue
                from_image = Image.open(image_names[(x-1)+(y-1)*30]).resize(
                    (20, 20),Image.ANTIALIAS)
                to_image.paste(from_image, ((x - 1) *20, (y - 1) * 20))
        path = os.path.abspath(__file__)
        path = path.split('/')
        path[len(path) - 1] = 'a.png'
        imagepath = ''
        for e in path:
            if not path.index(e) == len(path) - 1:
                imagepath += e + '/'
            else:
                imagepath += e
        to_image.resize((800, 600),Image.ANTIALIAS).save(imagepath) # 保存新图
        pic = pygame.image.load(imagepath)
        colorkey = pic.get_at((0,0))
        pic.set_colorkey(colorkey)
        pic_rect = pic.get_rect()
        pic_rect.centerx = screen.get_rect().centerx
        pic_rect.centery = screen.get_rect().centery
        screen.fill((255,255,255))
        screen.blit(pic,pic_rect)
        font = pygame.font.Font("msyh.ttc",24)
        draw_string = "剩余时间:%s,得分:%s" % (t,len(snake) - 3)
        text = font.render(draw_string,True,(0,0,0))
        text_rect = text.get_rect()
        text_rect.centerx = screen.get_rect().centerx
        text_rect.y = 10
        screen.blit(text,text_rect)
        pygame.display.update()
    while True:
        timer -= 1
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.insert(0,[snake[0][0] - 1,snake[0][1]])
                    del snake[len(snake) - 1]
                elif event.key == pygame.K_RIGHT:
                    snake.insert(0,[snake[0][0] + 1,snake[0][1]])
                    del snake[len(snake) - 1]
                elif event.key == pygame.K_UP:
                    snake.insert(0,[snake[0][0],snake[0][1] - 1])
                    del snake[len(snake) - 1]
                elif event.key == pygame.K_DOWN:
                    snake.insert(0,[snake[0][0],snake[0][1] + 1])
                    del snake[len(snake) - 1]
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
        for i in range(30):
            for x in range(30):
                n = ' '
                if i == 29 or i == 0 or x == 29 or x == 0:
                    n = '*'
                a[i][x] = n
        a[food[1]][food[0]]='@'
        try:
            for n in snake:
                if snake.index(n) == 0:
                    a[n[1]][n[0]]='O'
                else:
                    a[n[1]][n[0]]='+'
                if n == food:
                    food=[random.randint(0,29),random.randint(0,29)]
                    snake.append(snake[len(snake) - 1])
        except IndexError:
            pygame.quit()
            break
        ot = timer
        printsnake(a,timer)
        if timer == 0:
            break
    print('游戏结束')
    os.system("puase")
    pygame.quit()
main()
