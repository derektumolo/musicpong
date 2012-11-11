import sc

NOTE = 1
ACTION = 2

def getStartText(self):
	print "Start Text"
	
def getEndText(self):
	print "End Text"
	
def getTempo(self):
	print "Current tempo"

def getBackgroundInstrument(self):
  	print "Background Instrument"

def getInstrumentList(self):
	print "Instrument List"	

def isValidState(tickValue):
	print "Valid State" 

def handleMusicInput(self, player, note):
	if(isButtonPressValid(self,player,note)):
		self.notesPlayed[self.getActivePlayer()].append(note)

def isButtonPressValid(self,player, buttonPress):
	if(self.getActivePlayer() ==  player):
		if (self.getState() == NOTE and not self.notesPlayed[self.getActivePlayer()]):
			return True
		else:
			return False

def playBackgroundInstrument(self):
	print "Background instrument"
	
def update(self):
	print "Update self in halfNote"
