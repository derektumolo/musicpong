#! /usr/bin/python

from abc import ABCMeta,abstractmethod 

class Level(object):
	__metaclass__ = ABCMeta
	
	import metronome
	
	@abstractmethod
	def getStartText():
		raise NotImplementedError

	@abstractmethod
	def getEndText():
		raise NotImplementedError

	@abstractmethod
	def getTempo():
		raise NotImplementedError

	@abstractmethod
	def getBackgroundInstrument():
		raise NotImplementedError

	@abstractmethod
	def getInstrumentList():
		raise NotImplementedError

	@abstractmethod
	def isValidState(tickValue):
		raise NotImplementedError

	@abstractmethod
	def isButtonPressValid(buttonPress,tickValue):
		raise NotImplementedError

	@abstractmethod
	def playBackgroundInstrument():
		raise NotImplementedError
	
	@abstractmethod
	def update():
		raise NotImplementedError
	
