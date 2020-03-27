import turtle
import requests
import csv

WIDTH = 800
HEIGHT = 800


def getInstructionsFromGoogleSheet():

	url = 'https://docs.google.com/spreadsheets/u/0/d/1i3SP5tYbVhyOoL5nSTAVh3od6LsDYnhb65QHFwSX7Ns/export?format=csv&id=1i3SP5tYbVhyOoL5nSTAVh3od6LsDYnhb65QHFwSX7Ns&gid=0'
	filename = 'bearings.csv'

	response = requests.get(url)

	open(filename, 'wb').write(response.content)

	file = open(filename)
	reader = csv.reader(file)

	headers = next(reader)
	angle = headers.index('Angle')
	distance = headers.index('Distance')

	instructions = []

	for row in reader:

		instructions.append((row[angle], row[distance]))

	return instructions



def draw(instructions):

	# Setup canvas + turtle
	screen = turtle.Screen()
	screen.title("Burt The Turtle")
	screen.setup(WIDTH, HEIGHT)
	screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
	turtle.mode('logo')
	turtle.hideturtle()
	turtle.speed(5)
	
	# Draw
	for angle, distance in instructions:

		print(f'Drawing.. Angle: {angle} | Distance: {distance}')
		turtle.setheading(float(angle))
		turtle.forward(float(distance))

	turtle.done()


instructions = getInstructionsFromGoogleSheet()
draw(instructions)





