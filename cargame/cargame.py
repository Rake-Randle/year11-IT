import pygame
from pygame.locals import *
import random

size = width, height = (800, 800)
road_w = int(width/1.6)
roadmark_w = int(width/80)
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4
speed = 1

pygame.init()
running = True
# Window size
screen = pygame.display.set_mode((size))
# Setting title
pygame.display.set_caption("Jake's car game")
# Color 
screen.fill((80, 220, 70))
# Draw Graphics
# road
pygame.draw.rect(
    screen,
    (50, 50, 50),
    (width/2-road_w/2, 0, road_w, height)
)
# yellow line
pygame.draw.rect(
    screen, 
    (255, 240, 60),
    (width/2-roadmark_w/2, 0, roadmark_w, height)
)
# white line left
pygame.draw.rect(
    screen, 
    (255, 255, 255),
    (width/2-road_w/2 + roadmark_w*2, 0, roadmark_w, height)
)
# white line right
pygame.draw.rect(
    screen, 
    (255, 255, 255),
    (width/2+road_w/2 - roadmark_w*3, 0, roadmark_w, height)
)

# Apply chanags
pygame.display.update()

# load images
# player car
car = pygame.image.load("img/car.png")
car_loc = car.get_rect()
car_loc.center = left_lane, height*0.8

# Enemy car
car2 = pygame.image.load("img/otherCar.png")
car_2loc = car.get_rect()
car_2loc.center = right_lane, height*0.2

counter = 0
# game loop
while running:
    counter += 1
    if counter == 4096:
        speed += 0.25
        counter = 0
        print("Level up", speed)
    # animate enemy car
    car_2loc[1] += speed
    if car_2loc[1] > height:
        if random.randint(0,1) == 0:
            car_2loc.center = left_lane, -200
        else:
            car_2loc.center = right_lane, -200
    # end gane
    if car_loc[0] == car_2loc[0] and car_2loc[1] > car_loc[1] - 250:
        print("GAME OVER! YOU LOST!")
        break
    
    # event listeners
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_w/2), 0])
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w/2), 0])
    
    # Draw Graphics
    # road
    pygame.draw.rect(
        screen,
        (50, 50, 50),
        (width/2-road_w/2, 0, road_w, height)
    )
    # yellow line
    pygame.draw.rect(
        screen, 
        (255, 240, 60),
        (width/2-roadmark_w/2, 0, roadmark_w, height)
    )
    # white line left
    pygame.draw.rect(
        screen, 
        (255, 255, 255),
        (width/2-road_w/2 + roadmark_w*2, 0, roadmark_w, height)
    )
    # white line right
    pygame.draw.rect(
        screen, 
        (255, 255, 255),
        (width/2+road_w/2 - roadmark_w*3, 0, roadmark_w, height)
    )
    screen.blit(car, car_loc)
    screen.blit(car2, car_2loc)
    pygame.display.update()

pygame.quit() 
