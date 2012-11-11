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
	print note
	if(isButtonPressValid(self,player,note)):
		self.notesPlayed[self.getActivePlayer()].append(note)
		self.state = ACTION

def isButtonPressValid(self,player, buttonPress):
	print "Button Press"
	if(self.getActivePlayer() ==  player):
		if (self.getState() == NOTE and not self.notesPlayed):
			return True
		else:
			return False

def playBackgroundInstrument(self):
	print "Background Instrument"
	
def update(self):
	print "dooobeee doobee doo"
