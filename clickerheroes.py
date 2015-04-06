#!/usr/bin/env python
import pyscreenshot as ImageGrab
from pymouse import PyMouse
from pykeyboard import PyKeyboard
from time import *
from datetime import datetime
import cv2, os
from cv2 import cv
import numpy as np
import pytesseract



#	TODO: 
#		1.	FIX checkprog() so that it clicks the progression mode icon when it's in idle mode.
#		2.	Add all relevant information on skills in a data structure(s) stored in Heroes class in


class Hero:
	def __init__(self, name, price, dps):
		self.name = name
		self.img = cv2.imread('img/%s/%s.png' % (name, name))
		self.goldimg = cv2.imread('img/%s/%sgold.png' % (name, name))
		self.price = price
		self.dps = dps


# Added by: Sentient64
class Skill:
	def __init__(self, name, hotkey):
		self.name = name
		self.img = cv2.imread('DarkRitualAssets/%s.png' % (name))
		self.hotkey = hotkey
		

class Heroes:
	def __init__(self):
		self.winy = 0
		self.winx = 0
		self.hwinx = 0
		self.hwiny = 0
		self.cvmethod = cv2.TM_CCOEFF_NORMED
		self.mouse = PyMouse()
		self.keyboard = PyKeyboard()
		self.startpointer = cv2.imread('img/start.png')
		self.idleimg = cv2.imread('img/idle.png')
		self.progimg = cv2.imread('img/prog.png')
		self.heroes = []
		self.skills = []
		self.loadskills()
		self.loadheroes()
		self.getwindow()
		self.BETTY=5
		self.NATALIA=10
		self.MIDAS=15
		self.AMEN=19
		self.SHINO=23
		self.FROST=25
		self.terraimggold = cv2.imread("img/terra/terragold.png")
		self.coin = cv2.imread("img/coin.png")

	def loadskills(self):
		with open('skills.txt', 'r') as f:
			for l in f.read().split('\n'):
				if len(l) == 0:
					continue
				tok = l.split(',')
				s = Skill(tok[0], tok[1])
				self.skills.append(s)

	def loadheroes(self):
		with open('heroes.txt', 'r') as f:
			for l in f.read().split('\n'):
				if len(l) == 0:
					continue
				tok = l.split(',')
				h = Hero(tok[0], float(tok[1]), float(tok[2]))
				self.heroes.append(h)

	def getwindow(self):
		im = ImageGrab.grab().convert('RGB')
		big=np.array(im)
		big=big[:, :, ::-1].copy()
		r = cv2.matchTemplate(self.startpointer, big, self.cvmethod)
		y, x = np.unravel_index(r.argmax(), r.shape)
		self.winx = x - 14
		self.winy = y - 86
		self.hwinx = self.winx + 11
		self.hwiny = self.winy + 171
		return (self.winx, self.winy)

	def getenemyloc(self):
		im = ImageGrab.grab().convert('RGB')
		big=np.array(im)
		big=big[:, :, ::-1].copy()
		r = cv2.matchTemplate(self.startpointer, big, self.cvmethod)
		y, x = np.unravel_index(r.argmax(), r.shape)
		return (x+820, y+200)

	def findimg(self, small, x, y, w, h):
		im = ImageGrab.grab()
		big=np.array(im)
		big=big[:, :, ::-1].copy()

		while True:
			try:
				r = cv2.matchTemplate(small, big, self.cvmethod)
				break
			except:
				print "Warning: failed to grab image"
				continue
		min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(r)
		print "Found one!"
		# min_loc should be the location of the image. print it to make sure it's a tuple
		x, y = np.unravel_index(r.argmax(), r.shape)
		loc = np.where(r >= 0.95)		# Threshold = 0.95
		
			#	This if-statement is fucked up. Please fix it so that it makes sense.
		if loc.count(x) > 0 and loc.count(y) > 0:	 # loc.count(x) is how many times 'x' appears in loc
			return (x, y)
		else:
			return (x, y)
	
	# Returns it's top-left coordinates.
	def findskillimg(self, small):
		return self.findimg(small.img, self.winx+530, self.winy+30, 105, 520)
	
	def getclickerskill(self, skillname):
		for skill in self.skills:
			if skill.name == skillname:
				return self.findimg(skill.img, self.winx+530, self.winy+30, 105, 520)
	
	def findheroimg(self, small):
		return self.findimg(small, self.hwinx, self.hwiny, 535, 635)

	def findhero(self, hero):
		x, y = self.findheroimg(hero.img)
		if x == None:
			x, y = self.findheroimg(hero.goldimg)
		return (x, y)

	def selhero(self, hero):
		#Fast finding
		x, y = self.findhero(hero)
		if x == None or y == None:
			self.mouse.click(self.hwinx+2, self.hwiny+2)
			sleep(1.0)
			self.mouse.scroll(50, 0)
			sleep(1.0)
			x, y = self.findhero(hero)
			skips = 0
			while x == None:
				skips += 1
				self.mouse.scroll(-6)
				sleep(0.5)
				x, y = self.findhero(hero)
				if skips > 10:
					print "Warning: Hero not found, going back to top"
					self.selhero(hero)
					return
		if(y > 380):
			self.mouse.scroll(-3)
			sleep(0.5)
			x, y = self.findhero(hero)
		if x == None or y == None:
			#print "Warning: Strange hero error"
			self.selhero(hero)
			return
		self.mouse.move(self.hwinx+50, self.hwiny+y+50)
		sleep(0.2)

	def grabocr(self, x, y, w, h):
		im = ImageGrab.grab(bbox=(x, y, x+w, y+h))
		pix = im.load()
		for x in range(im.size[0]):
			for y in range(im.size[1]):
				if pix[x, y] != (254, 254, 254):
					pix[x, y] = 0;
		return pytesseract.image_to_string(im)

	def getmoney(self):
		raw = self.grabocr(self.winx+100, self.winy+18, 400, 42)
		try:
			val = float(raw)
			return val
		except:
			return 0

	def selmonster(self):
		self.mouse.move(self.winx+800, self.winy+350)

	def upgrade(self):
		self.mouse.click(self.winx+13, self.winy+171)
		sleep(0.2)
		self.mouse.scroll(-500)
		sleep(1.2)
		self.mouse.click(self.winx+250, self.winy+550)

	def checkprog(self):
		f = open("output.txt", "a")
		if not confirm:
			x, y = self.findimg(self.idleimg, self.winx+1090, self.winy+190, 60, 60)
			if x == None and y == None:
				return
			else:
				self.mouse.click(self.winx+1111, self.winy+211)
				f.write("Clicked on progression icon @ %s\n" % datetime.now())
		else:
			x, y = self.findimg(self.progimg, self.winx+1090, self.winy+190, 60, 60)
			if x == None and y == None:
				f.write("Not On Progression Mode\n")
				f.close()
				self.checkprog(confirm=0)
			else:
				f.write("On Progression Mode\n")
		f.close()
		sleep(0.2)

	def click(self, times = 1):
		x, y = self.mouse.position()
		for n in range(0, times):
			self.mouse.click(x, y)
			sleep(0.1)

	def ctrlclick(self, times = 1):
		self.keyboard.press_key(self.keyboard.control_key)
		sleep(0.2)
		self.click(times)
		sleep(0.1)
		self.keyboard.release_key(self.keyboard.control_key)

	def ascend(self):
		self.selhero(self.heroes[self.AMEN])
		x, y = self.mouse.position()
		self.mouse.click(x+250, y+10)
		sleep(0.5)
		self.mouse.click(self.winx+485, self.winy+425)
		sleep(0.5)
		self.mouse.click(self.winx+485, self.winy+425)
		sleep(0.5)
		self.mouse.move(self.winx+485, self.winy+425)
		sleep(0.5)
		self.mouse.click(self.winx+485, self.winy+425)
