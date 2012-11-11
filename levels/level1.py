#! /usr/bin/python

import Level
from metronome import Metronome

NOTE = 1
ACTION = 2

class TimingLevel(Level.Level):
	from logicBlocks.halfNote import getStartText,getEndText,getTempo,\
					 getBackgroundInstrument,getInstrumentList,isValidState,\
					 isButtonPressValid,playBackgroundInstrument,update, handleMusicInput

	def __init__(self):
		self.beatsPerMeasure = 4
		self.numMeasures = 3
		self.bpm = 30
		self.activePlayer = 1
		self.state = NOTE
		self.fail = False
		self.notesPlayed = {
            1: [],
            2: [],
			}
		self.metronome = Metronome(self.bpm, self.beatsPerMeasure)
		
	def getEndText(self):
		print "Level 1 end text"
		
	def update(self):
		self.metronome.update()
		if(self.metronome.isAtNextBeat()):
			print "Next beat - now on beat ", self.metronome.getBeat()
			self.advanceState()
			if(not self.isValidState()):
				print "setting failure"
				self.fail = True
				
	def isValidState(self):
		print self.state
		if self.state == NOTE:
			return True
		else:
			print "in else - "
			print self.notesPlayed[self.activePlayer]
			if self.notesPlayed[self.activePlayer]:
				print "notes played"
				print self.notesPlayed[self.activePlayer]
				return True
		print "returning false"
		return False


if __name__ == '__main__':
	test = TimingLevel()
	test.getEndText()
	test.getStartText()
	test.getTempo()
