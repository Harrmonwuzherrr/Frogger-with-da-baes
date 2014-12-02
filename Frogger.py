from Tkinter import *
root = Tk()
#Harmon and Vincent
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)
grass = drawpad.create_rectangle(0,250,800,600, fill = "green")
road = drawpad.create_rectangle(0,340,800,500, fill = "gray")
water = drawpad.create_rectangle(0,250,800,0, fill = "blue")
lillypad1 = drawpad.create_rectangle(70,0,110,30,  fill = "DarkGreen")
lillypad2 = drawpad.create_rectangle(180,0,220,30, fill = "DarkGreen")
lillypad3 = drawpad.create_rectangle(270,0,310,30, fill = "DarkGreen")
lillypad4 = drawpad.create_rectangle(390,0,430,30, fill = "DarkGreen")
lillypad5 = drawpad.create_rectangle(500,0,540,30, fill = "DarkGreen")
lillypad6 = drawpad.create_rectangle(610,0,650,30, fill = "DarkGreen")
lillypad7 = drawpad.create_rectangle(720,0,760,30, fill = "DarkGreen")
#bottom of road
truck1 = drawpad.create_rectangle(0,450,60,480, fill = "yellow")
truck2 = drawpad.create_rectangle(150,450,210,480, fill = "purple")
truck3 = drawpad.create_rectangle(300,450,360,480, fill = "yellow")
truck4 = drawpad.create_rectangle(450,450,510,480, fill = "yellow")

#medium row of road
car1 = drawpad.create_rectangle(40,400,80,430, fill = "red")

# first row of logs

Log4 = drawpad.create_rectangle(450,70,530,30, fill = "brown")
Log5 = drawpad.create_rectangle(600,70,680,30, fill = "brown")
#second row of logs

Log8 = drawpad.create_rectangle(300,150,380,190, fill = "brown")
Log9 = drawpad.create_rectangle(450,150,530,190, fill = "brown")
Log10= drawpad.create_rectangle(600,150,680,190, fill = "brown")
#middle row of logs



player = drawpad.create_oval(350,575,375,600, fill = "lightgreen")


collisionlist = [truck1,truck2,truck3,truck4,car1,Log4,Log5,Log8,Log9,Log10,lillypad1,lillypad2,lillypad3,lillypad4,lillypad5,lillypad6,lillypad7,water,player,]







          





























            








































      

























root.mainloop()




