#! /usr/bin/python

import Level

NOTE = 1
ACTION = 2

class DoubleMatchLevel(Level.Level):

	def __init__(self):
		bgInstrument = ()
		instrumentList = ()
		
		super(DoubleMatchLevel, self).__init__(4, 2, 30, "Starting Match 2", "Level 3 end text", bgInstrument, instrumentList)
				
	def isValidState(self):
		print self.state
		if self.state == NOTE:
			return True
		else:
			print self.notesPlayed[self.activePlayer]
			if self.notesPlayed[self.activePlayer]:
				print self.notesPlayed[self.activePlayer]
				return True
		return False
		
	def isButtonPressValid(self,player, buttonPress):
		if(self.getActivePlayer() ==  player):
			if (self.getState() == NOTE 
				and not self.notesPlayed[self.getActivePlayer()] 
				and buttonPress == self.notesPlayed[self.getOtherPlayer()]):
				return True
			else:
				return False

if __name__ == '__main__':
	test = TimingLevel()
	test.getEndText()
	test.getStartText()
	test.getTempo()
