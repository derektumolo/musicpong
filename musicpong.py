import pygame
import os
from levels.level1 import TimingLevel
from pygame.locals import *

NOTE = 0
ACTION = 1
		
class Game:
	def __init__(self):
		self.screen = pygame.display.set_mode((640, 480))
		pygame.display.set_caption('RockPong')

		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()
		self.background.fill((0, 0, 0))
		
		# Blit everything to the screen
		self.screen.blit(self.background, (0, 0))
		pygame.display.flip()

		# Initialise clock
		self.clock = pygame.time.Clock()
		
		self.running = True
		
		self.levels = [TimingLevel(),TimingLevel()]
		self.level = self.levels.pop()
		
		self.guideLines(10,50,1,70,4,4) #todo - move this
	
	def guideLines(self,x,y,width,height,measures,beats):
		self.beats = beats
		count = beats*measures
		self.gap = (640 - (width*(count+1)) - 20)/count
		
		for r in range(0,count+1):
			if (r%beats == 0):
				pygame.draw.rect(self.screen, (0,0,255), (x,y,width,height))
			else:
				pygame.draw.rect(self.screen, (0,255,0), (x,y,width,height/2))
			x = x + self.gap

	def handleKeyboardInput(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				self.running = False
				return
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					self.running = False
				else:
					self.level.handleMusicInput(1, event)
			
	#def handleMusicInput(self):
	#	#self.level.handleMusicInput()
	#	pass
	
	def update(self):
		self.level.update()
		
		if( self.level.isComplete() ):
			print "VICTORY"
			if (self.levels):
				self.level = self.levels.pop()
				self.level.start()
			else:
				exit()
	
def main():
	pygame.init()

	game = Game() 

	while game.running:
	# Make sure game doesn't run at more than 60 frames per second
		game.clock.tick(60)
		
		game.handleKeyboardInput()
		#game.handleMusicInput()
		
		game.update()
		
		pygame.display.update()

if __name__ == '__main__': main()

