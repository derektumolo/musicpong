NOTE = 1
ACTION = 2

def isButtonPressValid(self,player, buttonPress):
	if(self.getActivePlayer() ==  player):
		if (self.getState() == NOTE and not self.notesPlayed[self.getActivePlayer()]):
			return True
		else:
			return False

def playBackgroundInstrument(self):
	print "Background Instrument"