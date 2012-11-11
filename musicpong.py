import pygame
import pygame.midi
import os
import sc
from levels.level1 import TimingLevel
from pygame.locals import *

class Game:
	
	def __init__(self):
		self.s_keyDown=144
		self.s_velocityValue=127.0
    		self.keyboards = (pygame.midi.Input(3),pygame.midi.Input(5))
    		self.clock = pygame.time.Clock()
    		self.running = True
		
		self.levels = [TimingLevel(),TimingLevel()]
		self.level = self.levels.pop()
		self.level.getStartText()
	
		
	def update(self):
		
		# get events
		event_get = pygame.fastevent.get
		events = event_get()
	
		# process midi keyboard events
		for keyboard in self.keyboards:
			if keyboard.poll():
				midi_events = keyboard.read(10)
				print self.getPlayer(keyboard)," ",midi_events[0][0]
				self.level.handleMusicInput(self.getPlayer(keyboard),midi_events[0][0])
		
		# process computer keyboard events
		for event in events:
		    if event.type == KEYDOWN:
			if event.key in [K_1,K_q,K_a,K_z]:
				self.level.handleKeyboardInput(1,event.key)	
			if event.key in [K_HOME,K_PAGEUP,K_PAGEDOWN,K_END]:
				self.level.handleKeyboardInput(2,event.key)	
		
		# process level updates
		self.level.update()
		
		if( self.level.isComplete() ):
			self.level.getEndText()
			if (self.levels):
				self.level = self.levels.pop()
				self.level.getStartText()
			else:
				print "All levels completed successfully!"
				exit()
	
	def getPlayer(self,keyboardID):
		if(keyboardID == self.keyboards[0]):
				return 1
		else:
				return 2
	
def main():
	
	pygame.init()
	pygame.fastevent.init()
	pygame.midi.init()

	game = Game() 

	while game.running:
		
		game.clock.tick(60)
		game.update()

if __name__ == '__main__': main()

