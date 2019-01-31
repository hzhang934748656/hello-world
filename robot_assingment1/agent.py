import time
import random
'''
class Agent:
	def __init__(self, parent, x, y, dist):
        self.parent = parent
        self.x = x
        self.y = y
        self.dist = dist
class Fuct:
	def __init__(self,s_x,s_y,t_x,t_y):
		self.s_x = s_x
		self.s_y = s_y
		self.target_x = target_x
		self.target_y = target_y
		
	def Battary_check(self):
		if Battary_remain < (Battary_total/2):
			pass

	def move(self):
		roll = random(0,4)
		if roll == 0:
			move_up(current_location)
	def move_up(self,current_location):
		current_location(self.x,self.y)

	def move_down():	
	def move_left():	
	def move_right():

'''


wall = [(400, 0), (400, 100), (400, 200), (400, 300), (400, 800), (400, 700), (400, 600), (400, 500), (600, 400), (700, 400), (800, 400), (0, 300), (100, 300), (200, 300), (200, 400), (200, 500), (200, 600), (100, 600)]
wall_x = [400, 400, 400, 400, 400, 400, 400, 400, 600, 700, 800, 0, 100, 200, 200, 200, 200, 100]
wall_y = [0, 100, 200, 300, 800, 700, 600, 500, 400, 400, 400, 300, 300, 300, 400, 500, 600, 600]
from tkinter import *
root = Tk()
#create GUI
root.title("Clean Robot")
root.geometry("900x950")
canvas = Canvas(root, bg="old lace", height = 900, width = 900)

#create rubblish
rubbish_X = []
rubbish_Y = []
rubblish_image = PhotoImage(file = "rubbish.gif")

def addrubbish():
	for i in range(0,random.randint(1,4)):
		random_rubblish_x= random.randint(0,9)
		random_rubblish_y= random.randint(0,9)
		canvas.create_image((random_rubblish_x*100),(random_rubblish_y*100),anchor = "nw",image = rubblish_image)
		rubbish_X.append(random_rubblish_x*100)
		rubbish_Y.append(random_rubblish_y*100)
		#print(rubbish_X)
		#print(rubbish_Y)

addrubbish()
#create wall pic
wall_image = PhotoImage(file = "wall.gif")

for x in wall:
	canvas.create_image(x,anchor = "nw",image = wall_image)
#robot clean the rubbish
def cleanrubbish():
	pass						
#create button
#button_cleanrubbish= Button(root,text="Start clean", anchor= "sw",command = cleanrubbish)
#button_cleanrubbish.pack()
#create the cross line
for x in range(0,900,100):
	canvas.create_line(x,0,x,900,fill="black")
for y in range(0,900,100):
	canvas.create_line(0,y,900,y,fill='black')
#create robot
image_file = PhotoImage(file = "robot.gif")
robot =canvas.create_image(400,400,anchor = 'nw', image=image_file)
def move_up():
	canvas.move(robot,0,-100)
	canvas.update()
	time.sleep(1)
def move_down():
	canvas.move(robot,0,100)
	canvas.update()
	time.sleep(1)
def move_left():
	canvas.move(robot,-100,0)
	canvas.update()
	time.sleep(1)
def move_right():
	canvas.move(robot,100,0)
	canvas.update()
	time.sleep(1)
# move the robot and update the location
def move(p):
	for i in range(0,5):
		roll = random.randint(0,4)
		if roll == 0:
			for x,y in wall:
				if (x,y) == (p.x,p.y-100):
					break
				move_up()
				p.x = p.x
				p.y = p.y - 100
		if roll == 1:
			for x,y in wall:
				if (x,y) == (p.x, p.y+100):
					break
				move_down()
				p.x = p.x
				p.y = p.y + 100
		if roll == 2:
			for x,y in wall:
				if (x,y) == (p.x-100, p.y):
					break
				move_left()
				p.x = p.x -100
				p.y = p.y
		if roll == 3:
			for x,y in wall:
				if (x,y) == (p.x+100, p.y):
					break
				move_right()
				p.x = p.x + 100
				p.y = p.y
	return p.x,p.y

class Agent:
	def __init__(self, parent, x, y, dist):
		self.parent = parent
		self.x = x
		self.y = y
		self.dist = dist
# initialize the location
p = Agent(None,400,400,0)

	 



canvas.pack()
(new_x,new_y) = move(p)
print(new_x)
print(new_y)


root.mainloop()