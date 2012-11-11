#! /usr/bin/python

import Level

class TimingLevel(Level.Level):
	from logicBlocks.halfNote import getStartText,getEndText,getTempo,\
					 getBackgroundInstrument,getInstrumentList,isValidState,\
					 isButtonPressValid,playBackgroundInstrument,update
	
	def __init__(self):
		pass
	def getEndText(self):
		print "Level 1 end text"


if __name__ == '__main__':
	test = TimingLevel()
	test.getEndText()
	test.getStartText()
	test.getTempo()
