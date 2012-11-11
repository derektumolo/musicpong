#! /usr/bin/python

import Level
from metronome import Metronome

class TimingLevel(Level.Level):
	from logicBlocks.halfNote import getStartText,getEndText,getTempo,\
					 getBackgroundInstrument,getInstrumentList,isValidState,\
					 isButtonPressValid,playBackgroundInstrument,update
	

	def __init__(self):
		self.numberOfBeats = 4
		self.bpm = 60
		self.metronome = Metronome(self.bpm, self.numberOfBeats)
	def getEndText(self):
		print "Level 1 end text"
	def update(self):
		self.metronome.update()
		if(self.metronome.isAtNextBeat()):
				print "Next beat - now on beat ", self.metronome.getBeat()
	
	def isComplete(self):
		if (self.metronome.getBeat() > self.numberOfBeats):			
			return True 

	def isValidState(self):
		return True


if __name__ == '__main__':
	test = TimingLevel()
	test.getEndText()
	test.getStartText()
	test.getTempo()
