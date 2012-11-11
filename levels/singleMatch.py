#! /usr/bin/python

import Level

NOTE = 1
ACTION = 2

class SingleMatchLevel(Level.Level):

	def __init__(self):
		bgInstrument = ()
		instrumentList = ()
		
		super(SingleMatchLevel, self).__init__(4, 2, 30, "Starting Level 3", "Level 3 end text", bgInstrument, instrumentList)
				
	def isValidState(self):
		#print "other player played " + str(self.notesPlayed[self.getOtherPlayer()])
		if self.state == NOTE:
			return True
		else:
			print self.notesPlayed[self.activePlayer]
			if self.notesPlayed[self.activePlayer]:
				print self.notesPlayed[self.activePlayer]
				return True
		return False
		
	def isButtonPressValid(self,player, buttonPress):
		print "i pressed " + str(buttonPress[1]) + " and they played " + str(self.notesPlayed[self.getOtherPlayer()])
		if(self.getActivePlayer() ==  player):
			if (self.getState() == NOTE 
				and not self.notesPlayed[self.getActivePlayer()]
				and (self.notesPlayed[self.getOtherPlayer()] 
					or not buttonPress[1] == self.notesPlayed[self.getOtherPlayer()])):
				return True
			else:
				return False

if __name__ == '__main__':
	test = TimingLevel()
	test.getEndText()
	test.getStartText()
	test.getTempo()
