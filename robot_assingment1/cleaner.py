import tkinter as tk

#from tkinter import *
win = tk.Tk()
win.title("Cleaner robot")
win.geometry('1000x1000')
canvas = tk.Canvas(win,bg='old lace',height = 1000, width=1000)
#robot move
def move():
    canvas.move(robot,0,20)
# create room line
for x in range(0,1000,100):
    canvas.create_line(x,0,x,1000,fill="black")
for y in range(0,1000,100):
    canvas.create_line(0,y,1000,y,fill="black")
#cre    
b=tk.Button(win, text="Robot move",command = move).pack()
image_file = tk.PhotoImage(file='robot.gif')
robot = canvas.create_image(0,0,anchor="nw",image = image_file)
rubbish = canvas.create_rectangle(100,100,200,200,fill = "yellow")
#frame = Frame(win, width = 1000,hegith= 1000)
def Addrubbish(event):
    print(event.x,event.y)
button = Button(win,text="Add rubbish")
button.bind('<button-1>',buttonAction)
button.pack()
canvas.pack()
win.mainloop()





    
    