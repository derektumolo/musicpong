#! /usr/bin/python

import Level
import sc

NOTE = 1
ACTION = 2

class TimingLevel(Level.Level):

	def __init__(self):
		
		bgInstrument = ()
		instrumentList = ()
		self.numFailures = 0
		
		super(TimingLevel, self).__init__(4, 2, 30, "Starting Level 1", "Level 1 end text", bgInstrument, instrumentList)
				
	def isValidState(self):
		print self.state
		if self.state == NOTE:
			return True
		else:
			if self.notesPlayed[self.activePlayer]:
				sine = sc.Synth( "sine" )
				sine.freq = 60 + (self.activePlayer * 3) 
				sine.amp  = 0.9
				return True
		
		if (self.numFailures > 4):
			return False
		else:
			self.numFailures = self.numFailures + 1
			saw = sc.Synth( "saw" )
			saw.freq = 36 + (self.numFailures * 12) 
			sine.amp  = 0.6
			return True
	
	def isButtonPressValid(self,player, buttonPress):
		if(self.getActivePlayer() ==  player):
			if (self.getState() == NOTE and not self.notesPlayed[self.getActivePlayer()]):
				return True
			else:
				return False
