#! /usr/bin/python

import Level

class TimingLevel(Level.Level):
	from logicBlocks.halfNote import getStartText,getEndText,getTempo,\
					 getBackgroundInstrument,getInstrumentList,isValidState,\
					 isButtonPressValid,playBackgroundInstrument,update
	

	def __init__(self):
		self.numberOfBeats = 4
		self.currentBeat = 1
	def getEndText(self):
		print "Level 1 end text"
	def update(self):
		metronome.upate()
		if(metronome.isAtNextBeat()):
				currentBeat = currentBeat + 1
				print "Next beat - now on beat ", currentBeat
	
	def isComplete(self):
		if (currentBeat > numberOfBeats):			
			return True 

	def isValidState(self):
		return True


if __name__ == '__main__':
	test = TimingLevel()
	test.getEndText()
	test.getStartText()
	test.getTempo()
