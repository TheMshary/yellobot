from clickerheroes import *
import threading, time

h = Heroes()

#	Dark Ritual thread
#	TODO:
#		1.	RESUME the ritual based on current cooldowns
class DarkRitual(threading.Thread):
	def __init__(self):
		super(DarkRitual, self).__init__()

	def run(self):
		"""
		sleep(900)
		h.keyboard.tap_key('8')
		sleep(0.25)
		h.keyboard.tap_key('9')
		sleep(900) """
		###########################################
		###### For now, it assumes skills are ready ######
		###########################################
		while True:
			h.keyboard.tap_key('8')
			sleep(0.5)
			h.keyboard.tap_key('6')
			sleep(0.5)
			h.keyboard.tap_key('9')
			sleep(900)
			h.keyboard.tap_key('8')
			sleep(0.5)
			h.keyboard.tap_key('9')
			sleep(900)


#	Clicker thread
class Clicker(threading.Thread):

	def __init__(self):
		super(Clicker, self).__init__()

	def run(self):
		clickx, clicky = h.getenemyloc()
		while True:
			#	Does 16 clicks/sec
			h.mouse.click(clickx, clicky)
			sleep(0.0625)

#	Clicker Skills Manager thread
class ClickerSkills(threading.Thread):
	def __init__(self):
		super(ClickerSkills, self).__init__()
	
	def run(self):
		clickstormcooldown = 150
		clickstormhotkey = '1'
		powersurgecooldown = 150
		powersurgehotkey = '2'
		luckystrikescooldown = 450
		luckystrikeshotkey = '3'
		metaldetectorcooldown = 450
		metaldetectorhotkey = '4'
		goldenclickscooldown = 900
		goldenclickshotkey = '5'
		superclickscooldown = 900
		superclickshotkey = '7'
		
		#	Starts a thread for each skill, and clicks it when the cooldown is popped
		clickstorm = threading.Thread(target = activateSkill, args =  (clickstormhotkey, clickstormcooldown))
		clickstorm.daemon = True
		powersurge = threading.Thread(target=activateSkill, args = (powersurgehotkey, powersurgecooldown))
		powersurge.daemon = True
		luckystrikes = threading.Thread(target=activateSkill, args = (luckystrikeshotkey, luckystrikescooldown))
		luckystrikes.daemon = True
		metaldetector = threading.Thread(target=activateSkill, args = (metaldetectorhotkey, metaldetectorcooldown))
		metaldetector.daemon = True
		goldenclicks = threading.Thread(target=activateSkill, args = (goldenclickshotkey, goldenclickscooldown))
		goldenclicks.daemon = True
		superclicks = threading.Thread(target=activateSkill, args = (superclickshotkey, superclickscooldown))
		superclicks.daemon = True
		
		clickstorm.start()
		sleep(0.5)
		powersurge.start()
		sleep(0.5)
		luckystrikes.start()
		sleep(0.5)
		metaldetector.start()
		sleep(0.5)
		goldenclicks.start()
		sleep(0.5)
		superclicks.start()
		

def activateSkill(skillHotKey, cooldown):
	while True:
		#print "in activateSkill()"
		h.keyboard.tap_key(skillHotKey)
		sleep(cooldown)

#	Heroes Manager thread
#	Assumes beginning of ascension
#class HeroesManager(threading.Thread):
#	mouseX, mouseY = (0, 0)
#	def __init__(self):
#		mouseX, mouseY = h.mouse.position()
#		self.mouse.click(self.hwinx+2, self.hwiny+2)		# Clicks the Heroes tab without moving the mouse.
#		h.mouse.move(mouseX, mouseY)
		#START MANAGING IN RUN METHOD


#	def run(self):
		# search for Terra's box
#		terrax, terray = h.findheroimg(h.terraimggold)
#		cointempx, cointempy = (terrax-360, terray+50)
#		coinx, coiny = h.findimg(h.coin, coinx, coiny, 50, 50)
#		pricex, pricey = (coinx+25, coiny)
		
		# search for coin within Terra's box
		# get price boundaries
#		h.keyboard.press_key('z')
#		while True:
			

#	Ascension Manager thread
#class AscensionManager(threading.Thread):

#	def __init__(self):
		
		
#	def run(self):
#		while True:
					#	if it takes more than 10 seconds to progress 2 zones, it's time to ascend.
#			prevzone = self.getzlvl()
#			sleep(10)
#			curzone = self.getzlvl()
#			progressed = curzone - prevzone
#			if progressed < 2:
#				self.ascend()

#	def getzlvl():


#	def ascend():
		#	scroll up to max
		#	scroll down a constant amount to get to Amenhotep (location doesn't change)



#	Ancients Manager thread
#class AncientsManager(threading.Thread):

			#	include data structures to organize the information on all summoned and unsummoned ancients
			#	and their relations to one another
			#	lvl up one, the rest line up in a sequence of priority
			#	repeat the sequence until another sequence is more effective and efficient


#	def __init__(self):
		
		
#	def run(self):
		


















