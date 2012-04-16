import pygame,sys
from pygame.locals import *

pygame.init()

screen=pygame.display.set_mode((640,360),0,32)
pygame.display.set_caption("Fak")
bgColor=(255,0,255)
circle_color=(255,255,255)
x=50
y=50
c=50
b=50
circle_pos=(x,y)
mainLoop=True
pygame.mixer.music.load('123.mp3')
pygame.mixer.music.play()
while mainLoop:
	for event in pygame.event.get():
		if event.type==QUIT:
			mainLoop=False
		elif event.type==KEYDOWN:
			if event.key==K_SPACE:
				circle_color=(95,100,255)
				b,c=x,y
			elif event.key==K_LEFT:
				x-=5
				circle_pos=(x,y)
			elif event.key==K_UP:
				y-=5
				circle_pos=(x,y)
			elif event.key==K_RIGHT:
				x+=5
				circle_pos=(x,y)
			elif event.key==K_DOWN:
				y+=5
				circle_pos=(x,y)
		elif event.type==KEYUP:
			if event.key==K_SPACE:
				circle_color=(255,255,255)
				circle_pos=(x,y)			

	screen.fill(bgColor)
	pygame.draw.circle(screen,circle_color,circle_pos,50,0)
	pygame.draw.lines(screen,circle_color,True,[(b,c),(circle_pos)],50)
	pygame.display.update()

pygame.quit()
