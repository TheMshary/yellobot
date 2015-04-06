#!/usr/bin/env python
from clickerheroes import *
from time import *
from datetime import timedelta
import threads

h = Heroes()

#	TODO:
#		1. If game not found, NAVIGATETOGAME()
#				It opens Google Chrome, then locates the tab, then checks if game is crashed
#				If it's not crashed, it checks the skills' cooldowns. Then proceeds from there.
#		2. Set h.skills[0] to empty so that skill hot keys are the same as their index in the array
#		


def startup():
	h.checkprog()
	sleep(0.5)
	h.selmonster()
	sleep(0.2)
	money = 0
	while money < h.heroes[1].price:
		h.click(20)
		money = h.getmoney()
	sleep(5)

def buyhero(ll):
	h.selhero(ll)
	sleep(0.2)
	h.ctrlclick()

def buybetty():
	buyhero(h.heroes[h.BETTY])
	sleep(1)
	h.upgrade()
	sleep(2)

def buymidas():
	buyhero(h.heroes[h.MIDAS])
	sleep(1)
	h.upgrade()
	sleep(2)

def earlygame(start):
	lvl = start
	money = h.getmoney()
	while money < h.heroes[h.FROST].price:		# while you can't hire/lvlup FROSTLEAF
		if money > h.heroes[lvl+1].price:
			lvl += 1
			if lvl == h.NATALIA+2:
				buybetty()
			if lvl == h.AMEN+1:
				buymidas()
		h.selhero(h.heroes[lvl])
		h.ctrlclick()
		sleep(2)
		h.checkprog()
		if lvl > 17:
			h.upgrade()
			sleep(2)
		money = h.getmoney()

def frostleaf():
	for n in range(0, 10):
		h.upgrade()
		sleep(1)
		h.selhero(h.heroes[h.FROST])
		sleep(1)
		h.ctrlclick()
		sleep(5)

def finalupgrade():
	for n in range(0, h.FROST):
		h.selhero(h.heroes[n])
		sleep(0.5)
		h.ctrlclick(10)
		sleep(0.2)
	sleep(1)
	h.upgrade()

def nextgame():
	h.selhero(h.heroes[h.AMEN])
	sleep(1)
	h.ctrlclick(2)
	sleep(0.2)
	h.ascend()


def activateSkill(skillHotKey):
	f = open("output.txt", "a")
	h.keyboard.tap_key(skillHotKey)
	f.write("Activated %s Skill @ %s\n" % (h.skills[skillHotKey-1].name, datetime.now()))
	f.close()

#def checkCooldown():
#	try:
#		x, y = h.findskillimg(h.skills[7])
		# Energize skill ready
		
#		break
#	except:
#		print "Warning: failed to grab skill image @ %s" %datetime.now()
#		continue

def countDownToStart():
	print "5..."
	sleep(1)
	print "4..."
	sleep(1)
	print "3..."
	sleep(1)
	print "2..."
	sleep(1)
	print "1..."
	sleep(1)


count = 0
#countDownToStart()
#print "HeroBot started"
#while True:
#	start = datetime.now()
#	startup()
#	sleep(1)
#	earlygame(1)
#	frostleaf()
#	finalupgrade()
#	nextgame()
#	end = datetime.now()
#	count += 1
#	print "Round time:", end-start
#	print "Ascension count:", count
#	sleep(5)



#-------Dark Ritual Runs Automated-------#



#print "Sleeping for 1 second.."
#sleep(1)
#print "Dark Ritual Runs bot started...."
#conf = 1



#while True:
			#	Dark Ritual Run:
			#		1. Energize -> The Dark Ritual -> Reload		(8-6-9)
			#		2. wait 15 minutes (960 seconds)
			#		3. Energize -> Reload								(8-9)
			#		4. wait 15 minutes (960 seconds)
			#		5. Repeat
#	h.checkprog)
#	activateSkill(8)
#	activateSkill(6)
#	activateSkill(9)
#	sleep(970)
#	activateSkill(8)
#	activateSkill(9)
#	sleep(970)
#	conf = conf + 1
			#	click
###click()
			#	search for image
###checkCooldown()
"""
EDRbot = threads.DarkRitual()
sleep(0.5)
EDRbot.start()
sleep(0.5)"""	
"""
sleep(3)

while True:
	h.keyboard.press_key(h.keyboard.control_key)
	sleep(0.25)
	h.click()
	sleep(0.25)
	h.keyboard.release_key(h.keyboard.control_key)
	print " "
	print "--------------------------"
	print "--------------------------"
	print " "
	count = 20
	while count > 0:
		print "%s seconds left" % count	
		count = count - 1
		sleep(1)


	
"""
#	ATTENTION: THREADS CANNOT WORK WITHOUT BEING SYNCRONIZED
#	initialize bot threads
clickbot = threads.Clicker()
EDRbot = threads.DarkRitual()
clickerskillsbot = threads.ClickerSkills()

#	start bot threads
sleep(1)
clickbot.start()
sleep(2)
EDRbot.start()
sleep(2)
clickerskillsbot.start()














