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
truck3 = drawpad.create_rectangle(200,350,260,380, fill = "blue")
truck4 = drawpad.create_rectangle(350,350,410,380, fill = "red")
#medium row of road
car1 = drawpad.create_rectangle(40,400,80,430, fill = "red")

# first row of logs

log4 = drawpad.create_rectangle(450,110,530,70, fill = "brown")
log5 = drawpad.create_rectangle(600,70,680,30, fill = "brown")
#second row of logs

log8 = drawpad.create_rectangle(300,150,380,190, fill = "brown")
log9 = drawpad.create_rectangle(450,150,530,190, fill = "brown")
log10= drawpad.create_rectangle(600,150,680,190, fill = "brown")
#middle row of logs

# i wanna know what love is sssssssssssssssss i want you to show meee yeahhhhehehehehe i want feel what love isssssssssssss i want you to show
player = drawpad.create_oval(350,575,375,600, fill = "lightgreen")

loglist = [log4,log5,log8,log9,log10]



collisionlist = [truck1,truck2,truck3,truck4,car1,water]
def collisionDect():
    x1,y1,x2,y2 = drawpad.coords(player)
    
    for enemy in enemyList:
        ex1,ey1,ex2,ey2 = drawpad.coords(enemy)
        if x1 > ex1 and x1 < ex2 and y1 > ey1 and yi < ey2:
         drawpad.move(player, 350 - x1, 575 - y1)   
          
          
          
    foundlog = False 
    if y1 < 800:
        for log in loglist:
            lx1,ly1,lx2,ly2 = drawpad.coords(log)
            if x1 > lx1 and x1 < lx2 and y1 > ly1 and y1 < ly2:
                drawpad.move(player,logdirection,0)
                foundlog = True 
        if foundlog == False:
            drawpad.move(player, 350 - x1, 575 - y1)































            








































      

























root.mainloop()




