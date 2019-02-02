import time
import random

initial_map = [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
	[-1, 0, 0, 0, 0, 0, 0, 0, 0,-1],
	[-1, 0, 0, 0, 0, 0, 0, 0, 0,-1],
	[-1, 0, 0, 0, 0, 0, 0, 0, 0,-1],
	[-1, 0, 0, 0, 0, 0, 0, 0, 0,-1],
	[-1, 0, 0, 0, 0, 0, 0, 0, 0,-1],
	[-1, 0, 0, 0, 0, 0, 0, 0, 0,-1],
	[-1, 0, 0, 0, 0, 0, 0, 0, 0,-1],
	[-1, 0, 0, 0, 0, 0, 0, 0, 0,-1],
	[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]
new_wall_new = [(300, 0), (100, 900), (500, 0), (300, 900), (0, 400), (100, 300), (700, 0), (400, 500), (500, 900), (0, 200), (900, 0), (900, 700), (700, 900), (0, 800), (200, 600), (0, 500), (900, 900), (0, 700), (400, 200), (200, 400), (0, 300), (600, 400), (400, 800), (800, 400), (0, 900), (200, 900), (400, 300), (0, 0), (900, 200), (400, 900), (200, 300), (200, 0), (900, 100), (900, 400), (600, 900), (200, 500), (400, 0), (800, 900), (0, 100), (600, 0), (400, 600), (800, 0), (100, 0), (400, 100), (700, 400), (0, 600), (400, 700), (900, 300), (900, 600), (900, 500), (900, 800)]
from tkinter import *
root = Tk()
#create GUI
root.title("Clean Robot")
root.geometry("1000x1000")
canvas = Canvas(root, bg="old lace", height = 1000, width = 1000)

#create rubblish
rubblish = []
rubblish_image = PhotoImage(file = "rubbish.gif")

def addrubbish():
	for i in range(0,500):
		random_rubblish_x= random.randint(0,9)
		random_rubblish_y= random.randint(0,9)
		if (random_rubblish_x*100,random_rubblish_y*100) not in new_wall_new:
			canvas.create_image((random_rubblish_x*100),(random_rubblish_y*100),anchor = "nw",image = rubblish_image)
			rubblish.append([random_rubblish_x*100,random_rubblish_y*100])
			initial_map[random_rubblish_y][random_rubblish_x] = 1
			print(len(rubblish))

		return len(rubblish)
		#print(rubbish_Y)


#create wall pic
wall_image = PhotoImage(file = "wall.gif")
for x in new_wall_new:
	canvas.create_image(x,anchor = "nw",image = wall_image)
#robot clean the rubbish
def cleanrubbish():
	pass						
#create button
#button_cleanrubbish= Button(root,text="Start clean", anchor= "sw",command = cleanrubbish)
#button_cleanrubbish.pack()

#create the cross line
for x in range(0,1000,100):
	canvas.create_line(x,0,x,1000,fill="black")
for y in range(0,1000,100):
	canvas.create_line(0,y,1000,y,fill='black')

#create robot
image_file = PhotoImage(file = "robot.gif")
robot =canvas.create_image(400,400,anchor = 'nw', image=image_file)
def move_up():
	canvas.move(robot,0,-100)
	canvas.update()
	time.sleep(0.1)

def move_down():
	canvas.move(robot,0,100)
	canvas.update()
	time.sleep(0.1)

def move_left():
	canvas.move(robot,-100,0)
	canvas.update()
	time.sleep(0.1)

def move_right():
	canvas.move(robot,100,0)
	canvas.update()
	time.sleep(0.1)

# move the robot and update the location
def move(p):
	moved_map = [[p.x,p.y]]
	
	for i in range(0,20):
		clock = 1
		roll = random.randint(0,4)
		if roll == 0:
			for x,y in new_wall_new: #if the robot hit the wall
				if (x,y) == (p.x,p.y-100):
					canvas.move(robot,0,0)
					canvas.update()
					time.sleep(0.1)
					clock = 0
					break
			while clock:
				move_up()
				if [p.x,p.y] not in moved_map:
					moved_map.append([p.x,p.y])
				p.x = p.x
				p.y = p.y - 100
				Suck_dirt(p.x,p.y)
				canvas.update()

				p.total_cost += 1

				break
		if roll == 1:
			for x,y in new_wall_new:
				if (x,y) == (p.x, p.y+100):
					clock = 0
					break
			while clock:
				move_down()
				if [p.x,p.y] not in moved_map:
					moved_map.append([p.x,p.y])
				p.x = p.x
				p.y = p.y + 100
				Suck_dirt(p.x,p.y)
				canvas.update()
				p.total_cost += 1
				break
		if roll == 2:
			for x,y in new_wall_new:
				if (x,y) == (p.x-100, p.y):
					clock = 0
					break
			while clock:
				move_left()
				if [p.x,p.y] not in moved_map:
					moved_map.append([p.x,p.y])
				p.x = p.x -100
				p.y = p.y
				Suck_dirt(p.x,p.y)
				canvas.update()
				p.total_cost += 1
				break
		if roll == 3:
			for x,y in new_wall_new:
				if (x,y) == (p.x+100, p.y):
					clock = 0
					break
			while clock:
				move_right()
				if [p.x,p.y] not in moved_map:
					moved_map.append([p.x,p.y])
				p.x = p.x + 100
				p.y = p.y
				Suck_dirt(p.x,p.y)
				canvas.update()
				p.total_cost += 1
				break
	print("the len of the moved_map:",len(moved_map))
	return p.x,p.y,p.total_cost

def Suck_dirt(x,y):
	#pass
	canvas.create_rectangle(x,y,x+100,y+100,fill = "old lace")
	initial_map[int(y/100)][int(x/100)] = 0

class Agent:
	def __init__(self, parent, x, y, total_cost):
		self.parent = parent
		self.x = x
		self.y = y
		self.total_cost = total_cost
# initialize the location
p = Agent(None,400,400,0)
canvas.pack()
All_total_cost = 0
count_rubblish = 0
for i in range(0,1):
	p.total_cost = 0
	rubblish_total= addrubbish()
	(new_x,new_y,total_cost) = move(p)
	print("the total cost is ",total_cost)
	All_total_cost = total_cost + All_total_cost
	for a in initial_map:
		for x in a:
			if x == 1:
				count_rubblish += 1
	print("the total rubblish is ",rubblish_total)
	print("the rubblish remain is ",count_rubblish)
print("Done")
print(All_total_cost)

root.mainloop()