#Probably not a single one of the planets move accordingly. I really have no idea. A total mess it is
import random
import math
import time
from tkinter import *

global earthl
global earths

timing = 3 #edit this variable to change the orbit speed
earths = 3 #size of the earth, affects all other planets sizes as well
earthl = 21 #lenght from the sun to the earth, affects all other planets lenghts as well

width,height = 1900,1000
root = Tk()
root.geometry("1900x1000")
c = Canvas(root, width=width, height=height, bg="#00000a")

def oval(x1,y1,size,color):
	o = c.create_oval(x1-size/2,y1-size/2,x1+size/2,y1+size/2,width=0,fill=color)
	return (x1,y1)

def timer(clock,start,timing,reset):
	if clock%round(timing) == 0:
		start += 1
		if start > round(reset)-1:
			start = 0
	return start

def orbit(x1,y1,time,lenght,size,color="blue",speed=1):

	deg = 360/(360*speed)
	hyp = lenght
	orbits = []
	if True:
		sin = math.sin(math.radians(time*deg-90))
		cath = hyp*sin
		aath = math.sqrt(hyp**2-cath**2)

		if time < round(360/deg/2)+1:
			x2,y2 = x1-aath,y1+cath
			orbits.append((x2,y2))
		else:
			x2,y2 = x1+aath,y1+cath
			orbits.append((x2,y2))
	for orbit in orbits:
		oval(orbit[0],orbit[1],size,color=color)

clock = 0
earthtimer = 0
earthtimer2 = 0
marstimer = 0
global planet
global planetlist

planetlist = {"Mercury": 0,
			  "Venus" : 1,
			  "Earth" : 2,
			  "Mars" : 3,
			  "Ceres" : 4,
			  "Jupiter" : 5,
			  "Saturn" : 6,
			  "Uranus" : 7,
			  "Neptune" : 8}

planets = [[0.39,0.24,0.37,0,"#bfb8b8"],[0.72,0.6,0.92,0,"#ad7976"],[1,1,1,0,"#27688f"],[1.52,1.88,0.52,0,"#aa8f4a"],[2.77,4.6,0.15,0,"#8a8481"],[5.2,11.86,10.77,0,"#a36f44"],[9.54,29.46,9.23,0,"#c8a772"],[19.19,84.01,3.92,0,"#364fc0"],[30.06,164.82,3.84,0,"#3954cb"]]

def planet(x,y,pname,timing,clock):
	planet = planets[planetlist[pname]]
	planet[3] = timer(clock,planet[3], timing*planet[1], 360*planet[1])
	orbit(x, y, planet[3],int(earthl*planet[0]), int(earths*planet[2]),color=planet[4],speed=planet[1])
stars = []
for n in range(1000):
	stars.append((random.randint(0,width),random.randint(0,height),1,"#ffffff"))

while True:

	c.delete("all")
	sun = oval(width/1.5,height/1.4,size=6,color="#ffaa44")
	mercury = planet(sun[0], sun[1],pname="Mercury",timing=timing,clock=clock)
	venus = planet(sun[0], sun[1],pname="Venus",timing=timing,clock=clock)
	earth = planet(sun[0], sun[1],pname="Earth",timing=timing,clock=clock)
	mars = planet(sun[0], sun[1],pname="Mars",timing=timing,clock=clock)
	ceres = planet(sun[0], sun[1],pname="Ceres",timing=timing,clock=clock)
	jupiter = planet(sun[0], sun[1],pname="Jupiter",timing=timing,clock=clock)
	saturn = planet(sun[0], sun[1],pname="Saturn",timing=timing,clock=clock)
	uranus = planet(sun[0], sun[1],pname="Uranus",timing=timing,clock=clock)
	neptune = planet(sun[0], sun[1],pname="Neptune",timing=timing,clock=clock)

	

	clock += 1
	c.pack()
	root.update()








"""
															created by jax0033@protonmail.com
"""