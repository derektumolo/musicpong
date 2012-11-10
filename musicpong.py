import pygame
import os
from pygame.locals import *

class Measure(pygame.sprite.Sprite):
	def __init__(self, x=0, y=0, w=150, h=100):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.surface.Surface((w, h))
		self.image.fill((54, 47, 200))

		self.owner = []
		self.x = x
		self.y = y
		self.rect = pygame.Rect(x,y,x+w,y+h)
		self.rect2 = pygame.Rect(x-3,y-3,x+w+3,y+h+3)

	def move(self,x,y):
		self.rect2 = pygame.Rect(x-3, y-3, x+w+3,y+h+3) #prob inefficient
		self.rect = pygame.Rect(x,y,x+w,y+h)
		self.x = x
		self.y = y

	def draw(self, surface):
		surface.blit(self.image, self.rect)

NOTE = 0
ACTION = 1

		
class Game:
	def __init__(self):
		self.screen = pygame.display.set_mode((640, 480))
		pygame.display.set_caption('Apocalypse')

		# Fill background (probably deprecated?)
		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()
		self.background.fill((0, 0, 0))
		
		#gamechrome = chrome.Chrome()

		# Blit everything to the screen
		self.screen.blit(self.background, (0, 0))
		pygame.display.flip()

		# Initialise clock
		self.clock = pygame.time.Clock()
		
		self.running = True
		self.tick = 0
		
		self.state = NOTE
		self.activePlayer = 1
		
		self.notePlayed = False
		
		self.metronome = Metronome(60, 4)
	
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
					elif event.type == MOUSEBUTTONDOWN:
						x = event.pos[0]/32	
						y = event.pos[1]/32
						if event.button == 1:
							# detect collision with a unit, and select it, first deselecting the current
							player.highlight.move(x,y)
							#print player.highlight.rect
							#newselect = pygame.sprite.spritecollide(player.highlight, ug, False)
							#print newselect
							if newselect != []:
								# we have clicked on a unit.  
								if newselect[0] == player.selection:
									# if we click on it again, we deselect
									player.selection.deselect()
									player.selection = []
								else:
									# drop the current one, and select a new one.
									player.select(newselect[0])
									#player.selection.highlight = player.highlight
							elif player.selection:
								player.selection.move(x, y)

	def clockTick(self):
		self.tick = self.tick+1
		self.metronome.circle(self.gap)
		if (self.metronome.doABeat(self.tick)):
			self.stateChange()
	
	def stateChange(self):
		if self.state == NOTE:
			if (self.notePlayed):
				self.state = ACTION
			else :
				print "Yo, play something you noob."
		else:
			if (self.activePlayer == 1):
				self.activePlayer = 2
			else:
				self.activePlayer = 1
			print "new turn"
			self.state = NOTE
			self.notePlayed = False
			
			
class Metronome:
	def __init__(self, bpm, timeSig):
		self.beat = 1
		self.ticksPerBeat = bpm
		self.timeSig = timeSig
	
	def circle(gap):
		
		pygame.draw.circle(self.screen, (255,0,0), (self.tick + 10,70),5)
	
	def doABeat(self, tick):
		if (tick > self.ticksPerBeat * self.beat):
			self.beat = self.beat + 1
			if (self.beat%self.timeSig == 1):
				self.beat = 1
				return True
		return False
	
def main():
	pygame.init()

	game = Game() 

	while game.running:
	# Make sure game doesn't run at more than 60 frames per second
		game.clock.tick(60)
		
		gameObjects = (Measure(0,0), Measure(160,100))

		game.guideLines(10,50,1,70,4,4)
		
		# no events are used, but the remnant pong behavior is still there for ref.
		game.handleKeyboardInput()
		#game.handleMusicInput()
		
		game.clockTick()
		
		#for o in gameObjects:
			#game.screen.blit(o.image, o.rect, o.rect)
		#unitsprites.update()

		#unitsprites.draw(screen)

		#gamechrome.draw(game.screen, player)

		pygame.display.update()


		

if __name__ == '__main__': main()

