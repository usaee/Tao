import time

from objc_util import *

AVSpeechUtterance=ObjCClass('AVSpeechUtterance')

AVSpeechSynthesizer=ObjCClass('AVSpeechSynthesizer')

AVSpeechSynthesisVoice=ObjCClass('AVSpeechSynthesisVoice')



def speak(words):
	voices=AVSpeechSynthesisVoice.speechVoices()
	
	voice = voices[12]
	synthesize=AVSpeechSynthesizer.new()
	utterance=AVSpeechUtterance.speechUtteranceWithString_(words)
	
	utterance.rate=0.45
	utterance.voice=voice
	utterance.useCompactVoice=True
	synthesize.speakUtterance_(utterance)
	
	time.sleep(5)
