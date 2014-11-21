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
truck5 = drawpad.create_rectangle(600,450,660,480, fill = "purple")
#top of road
truck6 = drawpad.create_rectangle(200,350,260,380, fill = "blue")
truck7 = drawpad.create_rectangle(350,350,410,380, fill = "red")
truck8 = drawpad.create_rectangle(500,350,560,380, fill = "black")
truck9 = drawpad.create_rectangle(650,350,710,380, fill = "black")
truck10= drawpad.create_rectangle(20,350,80,380, fill = "blue")
#medium row of road
car1 = drawpad.create_rectangle(40,400,80,430, fill = "red")
car2 = drawpad.create_rectangle(240,400,280,430, fill = "blue")
car3 = drawpad.create_rectangle(440,400,480,430, fill = "forestgreen")
car4 = drawpad.create_rectangle(640,400,680,430, fill = "red")
# first row of logs
Log1 = drawpad.create_rectangle(0,50,80,90, fill = "brown")
Log2 = drawpad.create_rectangle(150,50,230,90, fill = "brown")
Log3 = drawpad.create_rectangle(300,50,380,90, fill = "brown")
Log4 = drawpad.create_rectangle(450,50,530,90, fill = "brown")
Log5 = drawpad.create_rectangle(600,50,680,90, fill = "brown")
#second row of logs
Log6 = drawpad.create_rectangle(0,150,80,190, fill = "brown")
Log7 = drawpad.create_rectangle(150,150,230,190, fill = "brown")
Log8 = drawpad.create_rectangle(300,150,380,190, fill = "brown")
Log9 = drawpad.create_rectangle(450,150,530,190, fill = "brown")
Log10= drawpad.create_rectangle(600,150,680,190, fill = "brown")








player = drawpad.create_oval(350,575,375,600, fill = "lightgreen")



























































































































root.mainloop()




