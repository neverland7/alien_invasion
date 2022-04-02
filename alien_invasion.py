import sys
import time
import pygame
import settings

pygame.init()


'主窗口'
screen_image = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
#设置窗口大小(screen_image为窗口图像)

screen_rect = screen_image.get_rect()
#get_rect()获得图像的形状信息和位置信息

'标题栏'
pygame.display.set_caption("Alien Invasion")

'飞船'
ship_image = pygame.image.load('images\plane.bmp')
#ship_image为飞船图像
ship_rect = ship_image.get_rect()
ship_rect.midbottom=screen_rect.midbottom
#让两个图像中央对齐
moving_left = False
moving_right = False
#向左、右连续移动的开关

'子弹'
bullets = pygame.sprite.Group()     #调用sprite的group类，生成一个装sprite的空盒子（只能用来装sprite的列表）
#bullets =[]     #空列表



#time.sleep(2.6)
'主程序（死循环）'
while True:
    '捕捉所有操作'
    for event in pygame.event.get():  
#        print(event)   #在控制台打印所有捕捉到的事件
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type ==pygame.KEYDOWN:   #按下键时
            if event.key == pygame.K_q:
                sys.exit()
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True        
            if event.key == pygame.K_SPACE:
                if len(bullets)<settings.bullets_allowed:
                    new_bullet = pygame.sprite.Sprite()     #调用sprite的Sprite类，生成一个有image属性和rect属性的对象
                    new_bullet.rect = pygame.Rect(0, 0, 3, 15)
                    new_bullet.rect.midbottom = ship_rect.midtop
                    bullets.add(new_bullet)
            # if event.key == pygame.K_SPACE:
            #     if len(bullets) < 5:    #最多同时存在5个子弹
            #         new_bullet_rect = pygame.Rect(0, 0, 3, 15)
            #         new_bullet_rect.midbottom = ship_rect.midtop
            #         bullets.append(new_bullet_rect)  #把生成的子弹放入子弹列表     
        elif event.type ==pygame.KEYUP:     #松开键时
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False

    '判断是否移出窗口'                
    if moving_left and ship_rect.left >0:
        ship_rect.x -= settings.ship_speed
    if moving_right and ship_rect.right < screen_rect.right:
        ship_rect.x += settings.ship_speed


    '绘制图像'
    screen_image.fill(settings.bg_coLor1)
    screen_image.blit(ship_image, ship_rect)

    for bullet in bullets:
        pygame.draw.rect(screen_image,settings.bg_coLor2,bullet.rect)
        bullet.rect.y -= 1
        if bullet.rect.bottom <0:
           bullets.remove(bullet.rect)
#     for bullet_rect in bullets:
#         pygame.draw.rect(screen_image, settings.bg_coLor2, bullet_rect)     #(位置，颜色，物体)
#         bullet_rect.y -= 1
#         if bullet_rect.bottom <0:
#             bullets.remove(bullet_rect)
#  #       print(len(bullets))

    pygame.display.flip()   #刷新屏幕

    time.sleep(0.01)