import time
wall = [[400, 0], [400, 100], [400, 200], [400, 300], [400, 800], [400, 700], [400, 600], [400, 500], [600, 400], [700, 400], [800, 400], [0, 300], [100, 300], [200, 300], [200, 400], [200, 500], [200, 600], [100, 600]]

class class_Node:
    def __init__(self, parent, x, y, dist):
        self.parent = parent
        self.x = x
        self.y = y
        self.dist = dist
        
class A_Star:
    def __init__(self, s_x, s_y, e_x, e_y, w=801, h=801):
        self.s_x = s_x
        self.s_y = s_y
        self.e_x = e_x
        self.e_y = e_y
        
        self.width = w
        self.height = h
        
        self.open = []
        self.close = []
        self.path = []
        
    def find_path(self):
        #create Node
        p = class_Node(None, self.s_x, self.s_y, 0.0)
        while True:
            #extend the next step
            self.extend_round(p)
            #if the openlist is empty
            if not self.open:
                return
            #get the lowest F
            idx, p = self.get_best()
            #get the path then return
            if p.x == self.e_x and p.y == self.e_y:
                self.make_path(p)
                return
            #add this node to closelist
            self.close.append(p)
            # delete this node from openlist
            del self.open[idx]
            
    def make_path(self,p):
        # track their parent, untill parent == None
        while p:
            self.path.append((p.x, p.y))
            p = p.parent
        
    def get_best(self):
        best = None
        bv = 1000000
        bi = -1
        for idx, i in enumerate(self.open):
            value = self.get_dist(i)#get F
            if value < bv:#compare the F
                best = i
                bv = value
                bi = idx
        return bi, best
        
    def get_dist(self, i):
        # F = G + H
        # G is the path cost robot already take, H is the estimate cost to the endpoint
        return i.dist + abs(self.e_x-i.x)+ abs(self.e_y-i.y)
        # use Manhattan distance
        
    def extend_round(self, p):
        xs = (-100, 0,   100,-100,100,-100,  0,100)
        ys = (-100,-100,-100,   0,  0, 100,100,100)
        for x, y in zip(xs, ys):
            new_x, new_y = x + p.x, y + p.y
            #if the place is wall or out of the map
            if not self.valid_check(new_x, new_y):
                continue
            #update the node
            node = class_Node(p, new_x, new_y, p.dist+ 1)
            #if the node in closelist, ignore
            if self.node_in_close(node):
                continue
            i = self.node_in_open(node)
            if i != -1:
                #node in openlist
                if self.open[i].dist > node.dist:
                    #if the current node is better than old node, replace it
                    self.open[i].parent = p
                    self.open[i].dist = node.dist
                continue
            #if the node is new, add to openlist
            self.open.append(node)

    def node_in_close(self, node):
        for i in self.close:
            if node.x == i.x and node.y == i.y:
                return True
        return False
        
    def node_in_open(self, node):
        for i, n in enumerate(self.open):
            if node.x == n.x and node.y == n.y:
                return i
        return -1
        
    def valid_check(self, x, y):
    	#if the new_node is out of the map
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        for a in wall:
        	if [x,y] == a:
        		return False
        return True

#########################################################
#########################################################
#########################################################
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
def addrubbish(event):
	canvas.create_image((int(event.x/100)*100),(int(event.y/100)*100),anchor = "nw",image = rubblish_image)
	rubbish_X.append(int((event.x/100))*100)
	rubbish_Y.append(int((event.y/100))*100)	
canvas.bind("<Button-1>", addrubbish)

#create wall pic
wall_image = PhotoImage(file = "wall.gif")

for x in wall:
	canvas.create_image(x,anchor = "nw",image = wall_image)
#robot clean the rubbish
def cleanrubbish():
	start_point_x = 0
	start_point_y = 0
	for ind in range(0,len(rubbish_X)):
		robot_clean = A_Star(start_point_x,start_point_y,rubbish_X[ind],rubbish_Y[ind])
		robot_clean.find_path()
		robot_clean.path.reverse()
		#print(robot_clean.path)
		zero_x = 0
		zero_y = 0
		for x, y in robot_clean.path:
			canvas.create_image(x,y,anchor = 'nw', image=image_file)
			canvas.update()
			canvas.create_rectangle(zero_x,zero_y,zero_x+100,zero_y+100,fill = "old lace")
			canvas.update()
			zero_x = x
			zero_y = y
			time.sleep(1)
		start_point_x = rubbish_X[ind]
		start_point_y = rubbish_Y[ind]							
#create button
button_cleanrubbish= Button(root,text="Start clean", anchor= "sw",command = cleanrubbish)
button_cleanrubbish.pack()
#create the cross line
for x in range(0,900,100):
	canvas.create_line(x,0,x,900,fill="black")
for y in range(0,900,100):
	canvas.create_line(0,y,900,y,fill='black')
#create robot
image_file = PhotoImage(file = "robot.gif")
robot =canvas.create_image(0,0,anchor = 'nw', image=image_file)
canvas.pack()
root.mainloop()