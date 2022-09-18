#-----------------------------------
#PONG game by- Sanoj kumar pradhan
#----------------------------------

from  tkinter import*
import time
import random

main=Tk()
main1=Tk()
main1.geometry("300x300")
main1.title("Pong!")
main.title("Pong!")
main.resizable(0,0)
main.wm_attributes()
q=1
canvas = Canvas(main, width=500, height=500, bd=0, highlightthickness=0)
canvas.configure(bg="light blue")
canvas.create_line(250,0,250,500)
var1=StringVar()
var2=StringVar()
p1=Label(main,textvariable=var2,font=("Helvetica Bold",20,),fg="Blue",bg="light blue")
p2=Label(main,textvariable=var1,font=("Helvetica Bold",20),fg="Red",bg="light blue")
canvas.create_window(200,10,window=p1)
canvas.create_window(300,10,window=p2)

canvas.pack()
main.update()

class Ball:
    global q
    def __init__(self,canvas,paddle1,paddle2,color):
        self.canvas=canvas
        self.paddle1=paddle1
        self.paddle2=paddle2
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,250,250)
        self.x=-q
        self.y=q
        self.canvas_width=self.canvas.winfo_width()
        self.canvas_height=self.canvas.winfo_height()
        self.s=0
        self.s1=0

    def hit_paddle1(self, pos):
        paddle_pos = self.canvas.coords(self.paddle1.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                return True
            return False

    def hit_paddle2(self, pos):
        paddle_pos = self.canvas.coords(self.paddle2.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                return True
            return False


    def draw(self):
        global var1
        global q
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x=q
            self.s=self.s+1
            var1.set(str(self.s))
        if pos[1]<=0:
            self.y=q
        if pos[2]>=self.canvas_width:
            self.x=-q
            self.s1=self.s1+1
            var2.set(str(self.s1))
        if pos[3]>=self.canvas_height:
            self.y=-q
        if self.hit_paddle1(pos)==True:
            self.x=q
        if self.hit_paddle2(pos)==True:
            self.x=-q



class Paddle1:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=self.canvas.create_rectangle(0,100,10,200,fill=color)
        self.canvas_height=self.canvas.winfo_height()
        self.y=0
        self.canvas.bind_all("<KeyPress-w>", self.move_up)
        self.canvas.bind_all("<KeyPress-s>", self.move_down)

    def draw(self):
        self.canvas.move(self.id,0,self.y)
        paddle1_pos=self.canvas.coords(self.id)
        if paddle1_pos[1]<=0:
            self.y=0
        if paddle1_pos[3]>=self.canvas_height:
            self.y=0
    def move_up(self,evt):
        self.y=-3
    def move_down(self,evt):
        self.y=3



class Paddle2:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=self.canvas.create_rectangle(490,100,500,200,fill=color)
        self.canvas_height = self.canvas.winfo_height()
        self.y = 0
        self.canvas.bind_all("<KeyPress-Up>", self.move_up)
        self.canvas.bind_all("<KeyPress-Down>", self.move_down)
    def draw(self):
        self.canvas.move(self.id,0,self.y)
        paddle1_pos=self.canvas.coords(self.id)
        if paddle1_pos[1]<=0:
            self.y=0
        if paddle1_pos[3]>=self.canvas_height:
            self.y=0
    def move_up(self,evt):
        self.y=-3
    def move_down(self,evt):
        self.y=3



paddle1=Paddle1(canvas,"Blue")
paddle2=Paddle2(canvas,"Red")
ball=Ball(canvas,paddle1,paddle2,'Violet')


def Easy(event):
    global q
    q=3
    easybut = Button(main1, text="Easy")
    easybut.place(x=40, y=210)

    main1.destroy()
    while True:
        ball.draw()
        paddle1.draw()
        paddle2.draw()
        main.update_idletasks()
        time.sleep(0.01)
        main.update()

def Hard(event):
    global q
    q=5
    hardbut = Button(main1, text="Hard")
    hardbut.place(x=200, y=210)

    main1.destroy()
    while True:
        ball.draw()
        paddle1.draw()
        paddle2.draw()
        main.update_idletasks()
        time.sleep(0.01)
        main.update()
def instruction(event):

    blabel = Label(main1, text="Blue Paddle""\n Direction" "\n W-Up" "\n S-Down", fg="Blue",
                            font=("Helvetica", 10))
    rlabel = Label(main1, text="Red Paddle""\n Direction" "\n Up arrow-Up" "\n Down arrow-Down", fg="Red",
                            font=("Helvetica", 10))


    blabel.place(x=30, y=240)
    rlabel.place(x=200, y=240)



inst=Button(main1,text="INSTRUCTION",font=("Helvetica",10))
inst.bind("<Button-1>",instruction)
inst.pack(side=BOTTOM)
pong=Label(main1,text="PONG",font=("Futura 60 underline"),fg="Red")
pong.place(x=62,y=0)
label=Label(main1,text="By-" "\n Sanoj kumar pradhan" ,font=("Helvetica",20))
label1=Label(main1,text="Select Level" ,font=("Helvetica Bold",20),fg="Black")
label1.place(x=92,y=180)
label.place(x=50,y=80)
easybut=Button(main1,text="Easy")
easybut.place(x=40,y=210)
easybut.bind("<Button-1>",Easy)
hardbut=Button(main1,text="Hard")
hardbut.place(x=200,y=210)
hardbut.bind("<Button-1>",Hard)



main1.mainloop()
main.mainloop()

