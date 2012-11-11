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
		
		self.metronome = Metronome(60, 4, self.screen)
	
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
				if event.key == K_TAB:
					self.notePlayed = True;
					self.previousNote = "note"
			
	def handleMusicInput(self):
		if (self.ActivePlayer == source):	
			if (self.state == NOTE):			
				self.notePlayed = True;
				if (self.playedGoodNote()):
					#play success msg
					pass
				if (firstTurn):
					self.firstTurn = False
					pass
				else: 
					#play bad note
					pass
			else: 
				self.action = action
	
	def playedGoodNote(self):
		
		pass
	
	def clockTick(self):
		self.tick = self.tick+1
		self.metronome.circle(self.tick, self.gap)
		#print self.metronome.doABeat(self.tick)
		if (self.metronome.doABeat(self.tick) == True):
			self.stateChange()
	
	def playedCorrect():
		passx
	
	def stateChange(self):
		#print "statechanging"
		if self.state == NOTE:
			if (self.playedCorrect()):
				self.state = ACTION
			elif (self.firstTurn == False) :
				print "Yo, play something noob."
				self.state = LOSE
		else:
			if (self.activePlayer == 1):
				self.activePlayer = 2
			else:
				self.activePlayer = 1
			print "new turn"
			self.state = NOTE
			self.notePlayed = False
			
class Metronome:
	def __init__(self, bpm, timeSig, screen):
		self.beat = 1
		self.ticksPerBeat = bpm
		self.timeSig = timeSig
		self.screen = screen
	
	def circle(self,tick,gap):
		x = tick*gap*self.ticksPerBeat/60/60
		pygame.draw.circle(self.screen, (255,0,0), (x + 10,70),5)
	
	def doABeat(self, tick):
		if (tick > self.ticksPerBeat * self.beat):
			self.beat = self.beat + 1
			if (self.beat%self.timeSig == 1):
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
		
		pygame.display.update()


		

if __name__ == '__main__': main()

