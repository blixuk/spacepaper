#!/usr/bin/env python

import random
import os

width = 1920
height = 1080
starAmount = 100
starSize = 3
planetAmount = 8
planetSize = 100

colour = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

def main():
    setup()

def setup():
	os.system("clear")
	print("SpacePaper\n\n")
	print("Please enter your paramaters!\n")
	width = int(input("Width of canvas: "))
	height = int(input("Height of canvas: "))
	starAmount = int(input("Amount of Stars: "))
	starSize = int(input("Max size of Stars: "))
	planetAmount = int(input("Amount of Planets: "))
	planetSize = int(input("Max size of Planets: "))
	write(width, height, starAmount, starSize, planetAmount, planetSize)

	while True:
		os.system("clear")
		print("\nWould you like to generate with the same paramaters again?\n")
		op = input("(Y)es / (N)o or (Q)uit: ")

		if op == "y" or op == "Y" or op == "yes":
			write(width, height, starAmount, starSize, planetAmount, planetSize)
		elif op == "n" or op == "N" or op == "no":
			setup()
		elif op == "q" or op == "Q" or op == "quit":
			break
		else:
			pass

def write(width, height, starAmount, starSize, planetAmount, planetSize):
	# Create File
	c = open('wallpaper.svg', 'w+')
	c.write('')
	c.close()

	# Document
	f = open(f'wallpaper.svg', 'a+')
	f.write('<?xml version="1.2" encoding="utf-8" ?>\n')
	f.write(f'<svg version="1.2" baseProfile="tiny" height="{height}" width="{width}" xmlns="http://www.w3.org/2000/svg" xmlns:ev="http://www.w3.org/2001/xml-events" xmlns:xlink="http://www.w3.org/1999/xlink">\n')
	f.write('<defs>')
	for s in stripes(5):
		f.write(f'{s}\n')
	f.write('</defs>\n')
	f.write('<rect fill="black" height="100%" width="100%" x="0" y="0" />\n')

	for s in drawStars(starAmount, starSize):	
		f.write(f'{s}\n')
	
	for p in drawPlanet(planetAmount, planetSize):
		f.write(f'{p}\n')

	f.write('</svg>')
	f.close()

def drawPlanet(amount, size):
	planets = []
	for i in range(1, amount):
		x = random.randint(size, width - size)
		y = random.randint(size, height - size)
		r = random.randint(1, size)
		
		x2 = 0
		y2 = 0
		
		if x2 == x:
			x = x + size
		elif y2 == y:
			y = y + size
		
		if (i % 2) == 0:
			planets.append(f'<circle fill="url(#stripes{i})" cx="{x}" cy="{y}" r="{r}"/>')
		elif (i % 3) == 0:
			r = r * 2
			n = random.sample(colour, 6)
			g = random.sample(colour, 6)
			planets.append(f'<circle fill="#{n[0]}{n[1]}{n[2]}{n[3]}{n[4]}{n[5]}" cx="{x}" cy="{y}" r="{r}"/>')
			planets.append(f'<ellipse style="stroke:#{g[0]}{g[1]}{g[2]}{g[3]}{g[4]}{g[5]}; stroke-width:{r/6};" fill="none" cx="{x}" cy="{y}" rx="{r * 2}" ry="{20}"/>')
			planets.append(f'<path d="M{x-r},{y} a1,1 0 0,0 {r*2},0" fill="#{n[0]}{n[1]}{n[2]}{n[3]}{n[4]}{n[5]}" />')
		elif (i % 4) == 1:
			n = random.sample(colour, 6)
			planets.append(f'<circle fill="#{n[0]}{n[1]}{n[2]}{n[3]}{n[4]}{n[5]}" cx="{x}" cy="{y}" r="{r}" stroke-dasharray="2, 40"/>')
			planets.append(f'<circle cx="{x}" cy="{y}" r="{r * 2}" stroke="white" stroke-width="{r / 6}" stroke-dasharray="2 {r / 2}" stroke-linecap="round" fill="none"/>')
			#r = r * 2
			#n = random.sample(colour, 6)
			#g = random.sample(colour, 6)
			#planets.append(f'<circle fill="#{n[0]}{n[1]}{n[2]}{n[3]}{n[4]}{n[5]}" cx="{x}" cy="{y}" r="{r}"/>')
			#planets.append(f'<ellipse cx="{x}" cy="{y}" rx="{r * 2}" ry="{20}" stroke="#{g[0]}{g[1]}{g[2]}{g[3]}{g[4]}{g[5]}" stroke-width="{r / 5}" stroke-dasharray="2 {r / 3}" fill="none" stroke-linecap="round"/>')
			#planets.append(f'<path d="M{x-r},{y} a1,1 0 0,0 {r*2},0" fill="#{n[0]}{n[1]}{n[2]}{n[3]}{n[4]}{n[5]}" />')
		else:
			n = random.sample(colour, 6)
			planets.append(f'<circle fill="#{n[0]}{n[1]}{n[2]}{n[3]}{n[4]}{n[5]}" cx="{x}" cy="{y}" r="{r}" />')
		
		x2 = x
		y2 = y
		
	return planets

def drawStars(amount, size):
	stars = []
	for i in range(1, amount):
		x = random.randint(size, width - size)
		y = random.randint(size, height - size)
		r = random.randint(1, size)
		a = random.sample(colour, 1)
		b = random.sample(colour, 1)
		stars.append(f'<circle fill="#{a[0]}{b[0]}{a[0]}{b[0]}{a[0]}{b[0]}" cx="{x}" cy="{y}" r="{r}"/>')
	return stars

def stripes(num):
	stripes = []
	for i in range(1, num):
		n = random.sample(range(3, 10), 6)
		g = random.sample(range(3, 10), 6)
		stripes.append(f'''<pattern id="stripes{i}" viewBox="0,0,8,8" width="50" height="50" patternUnits="userSpaceOnUse">
		<polygon points="0,0 4,0 0,4" 	  fill="#{n[0]}{n[1]}{n[2]}{n[3]}{n[4]}{n[5]}"></polygon>
		<polygon points="0,8 8,0 8,4 4,8" fill="#{n[0]}{n[1]}{n[2]}{n[3]}{n[4]}{n[5]}"></polygon>
		<polygon points="0,4 0,8 8,0 4,0" fill="#{g[0]}{g[1]}{g[2]}{g[3]}{g[4]}{g[5]} "></polygon>
		<polygon points="4,8 8,8 8,4"     fill="#{g[0]}{g[1]}{g[2]}{g[3]}{g[4]}{g[5]}"></polygon>
		</pattern>''')
	return stripes

if __name__ == "__main__":
    main()
