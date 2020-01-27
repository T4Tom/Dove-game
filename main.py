import pygame, random, time
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

passed = 0

font = pygame.font.SysFont(None, 100)
text = font.render('YOU HIT A BIRD!', True, (255, 0, 0))
textRect = text.get_rect()
textRect.center = (400, 300)

font2 = pygame.font.SysFont(None, 55)


doveImg = pygame.image.load('dove.png')
doveImg = pygame.transform.scale(doveImg, (100, 70))

pigeonImg = pygame.image.load('pigeon.png')
pigeonImg = pygame.transform.scale(pigeonImg, (100, 70))
pigeonImg2 = pygame.image.load('pigeon.png')
pigeonImg2 = pygame.transform.scale(pigeonImg2, (100, 70))
random1 = random.randint(1, 530)
random3 = random.randint(1, 530)

backgroundImg = pygame.image.load('background.jpg')
backgroundImg = pygame.transform.scale(backgroundImg, (800, 600))



def crash():
  screen.blit(text, textRect)
  pygame.display.flip()
  time.sleep(5)
  game_loop()


def game_loop():

  dovex = 60
  dovey = 300
  passed = 0

  pigeonx = 900
  pigeony = random1
  pigeonx2 = 900
  pigeony2 = random3


  done = False
  while not done:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
      if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and dovey > 0:
      dovey -= 5
    if pressed[pygame.K_DOWN] and dovey < 530:
      dovey += 5
    if pressed[pygame.K_RIGHT] and dovex < 700:
      dovex += 5
    if pressed[pygame.K_LEFT] and dovex > 0:
      dovex -= 5
    

    text2 = font2.render('Passed: {0}'.format(passed), True, (0, 0, 0))
    textRect2 = text2.get_rect()
    textRect2.center = (100, 50)


    pigeonx -= 5
    if pigeonx <= -170:
      pigeonx = 700
      passed += 1
      random2 = random.randint(1, 530)
      pigeony = random2

    pigeonx2 -= 3
    if pigeonx2 <= -200:
      pigeonx2 = 700
      passed += 1
      random4 = random.randint(1, 530)
      pigeony = random4




    screen.blit(backgroundImg, (0, 0))

    screen.blit(doveImg, (dovex, dovey))
    screen.blit(pigeonImg, (pigeonx, pigeony))
    screen.blit(pigeonImg2, (pigeonx2, pigeony2))
    screen.blit(text2, textRect2)
    
    if dovey + 70 >= pigeony and dovex + 100 >= pigeonx and dovex < pigeonx + 100 and dovey < pigeony + 70:
      crash()

    if dovey + 70 >= pigeony2 and dovex + 100 >= pigeonx2 and dovex < pigeonx2 + 100 and dovey < pigeony2 + 70:
      crash()

    pygame.display.flip()
    clock.tick(70)

game_loop()