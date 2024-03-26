import turtle 
import time
#from playsound import playsound

screen_1 = turtle.Screen()
screen_1.setup(width = 1050, height = 650)
t1 = turtle.Turtle()
screen_1.addshape("startpage.gif")
t1.shape("startpage.gif")
time.sleep(2)
screen_1.addshape("page after title.gif")
t1.shape("page after title.gif")
screen_1.tracer(0)

#gamepage
screen_3 = turtle.Screen()  
screen_3.setup(width = 1050, height = 650)
t3 = turtle.Turtle()
t3.shape("blank")
sketch_3 = turtle.Turtle()
sketch_3.color("white")  
sketch_3.penup()
sketch_3.hideturtle()

#endpage
screen_4 = turtle.Screen()  
t2 = turtle.Turtle()
#t2.shape("blank")
screen_4.setup(width = 1050, height = 650)
sketch_4 = turtle.Turtle()
sketch_4.color("white")  
sketch_4.penup()
sketch_4.hideturtle()


pen = turtle.Turtle()
pen.hideturtle()

ButtonLength = 100
ButtonWidth = 50

Button_x1 = -430
Button_y1 = -230

Button_x2 = -20
Button_y2 = -230

Button_x3 = 350
Button_y3 = -230


def draw_button1(pen):
    pen.penup()
    pen.goto(Button_x1, Button_y1)
    pen.goto(Button_x1 + ButtonLength, Button_y1)
    pen.goto(Button_x1 + ButtonLength, Button_y1 + ButtonWidth)
    pen.goto(Button_x1 , Button_y1 + ButtonWidth)
    pen.goto(Button_x1, Button_y1)
    pen.goto(Button_x1 + 25, Button_y1 + 15)
draw_button1(pen)


def draw_button2(pen):
    pen.penup()
    pen.goto(Button_x2, Button_y2)
    pen.goto(Button_x2 + ButtonLength, Button_y2)
    pen.goto(Button_x2 + ButtonLength, Button_y2 + ButtonWidth)
    pen.goto(Button_x2 , Button_y2 + ButtonWidth)
    pen.goto(Button_x2, Button_y2)
    pen.goto(Button_x2 + 25, Button_y2 + 15)
draw_button2(pen)


def instructions():
    sketch_3.goto(-20,4)
    sketch_3.write("The player controls an in-game paddle by moving it vertically\n across the left or right side of the screen.\n\n\nThey can compete against another player controlling a\n second paddle on the opposite side.\n\n\nPlayers use the paddles to hit a ball back and forth.\n\n\nThe goal is for each player to reach eleven points \nbefore the opponent.\npoints are earned when one fail to return the ball to the other.\n\n\nThe player reaching the eleven points first wins the game.",align="center",font=('Arial',15,'italic'))

def draw_button3(pen):
    pen.penup()
    pen.goto(Button_x3, Button_y3)
    pen.goto(Button_x3 + ButtonLength, Button_y3)
    pen.goto(Button_x3 + ButtonLength, Button_y3 + ButtonWidth)
    pen.goto(Button_x3 , Button_y3 + ButtonWidth)
    pen.goto(Button_x3, Button_y3)
    pen.goto(Button_x3 + 15, Button_y3+ 15)
    
draw_button3(pen)



def button_click(x,y):
    if Button_x1<=x<=Button_x1+ ButtonLength:
        if Button_y1<=y<=Button_y1 + ButtonWidth:
            turtle.exitonclick()
            
    elif  Button_x2<=x<=Button_x2 + ButtonLength:
        if Button_y2<=y<=Button_y2 + ButtonWidth:
            instructions()
                    
    elif Button_x3<=x<=Button_x3 + ButtonLength:
        if Button_y3<=y<=Button_y3 + ButtonWidth:
            screen_3.addshape("game_page.gif")
            t3.shape("game_page.gif")
            lp = turtle.Turtle()
            lp.hideturtle()
            lp = screen_3.textinput("player-1", "Enter your name")
            rp = turtle.Turtle()
            rp.hideturtle()
            rp = screen_3.textinput("player-2", "Enter your name")

            # Left paddle  
            left_paddle = turtle.Turtle()
            left_paddle.speed(-10)  
            left_paddle.shape("square")  
            left_paddle.color("white")  
            left_paddle.shapesize(stretch_wid = 6, stretch_len = 0.5)  
            left_paddle.penup()
            left_paddle.goto(-450, 0)  


            # Right paddle  
            right_paddle = turtle.Turtle()  
            right_paddle.speed(-10)  
            right_paddle.shape("square")  
            right_paddle.color("white")  
            right_paddle.shapesize(stretch_wid = 6, stretch_len = 0.5)  
            right_paddle.penup()
            right_paddle.goto(450, 0)  


            # Ball of circle shape  
            hit_ball = turtle.Turtle()
            hit_ball.shape("blank")
            hit_ball.speed(10)
            hit_ball.shape("circle")  
            hit_ball.color("white")  
            hit_ball.penup()
            hit_ball.goto(0,0)  
            hit_ball.dx = 0.6
            hit_ball.dy = 0.6

            #Now, we will initialize the score  
            left_player = 0  
            right_player = 0  


            # Displaying of the score  
            sketch_3 = turtle.Turtle()
            sketch_3.speed(0)  
            sketch_3.color("white")  
            sketch_3.penup()  
            sketch_3.hideturtle()  
            sketch_3.goto(0, 260)  
            sketch_3.write("Left_player : {}    Right_player: {}".format(  
                                  lp,rp), align = "center",  
                                  font = ("Courier", 24, "normal"))


            # Implementing the functions for moving paddle vertically  
            def paddle_L_up():  
                y = left_paddle.ycor()  
                y += 20  
                left_paddle.sety(y)  


            def paddle_L_down():  
                y = left_paddle.ycor()  
                y -= 20  
                left_paddle.sety(y)  


            def paddle_R_up():  
                y = right_paddle.ycor()  
                y += 20  
                right_paddle.sety(y)  


            def paddle_R_down():  
                y = right_paddle.ycor()  
                y -= 20  
                right_paddle.sety(y)  


            # Then, binding the keys for moving the paddles up and down.   
            screen_3.listen()  
            screen_3.onkeypress(paddle_L_up, "r")  
            screen_3.onkeypress(paddle_L_down, "c")  
            screen_3.onkeypress(paddle_R_up, "Up")  
            screen_3.onkeypress(paddle_R_down, "Down")  


            while True:  
                    screen_3.update()
                    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)  
                    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)   

                    # Check all the borders  
                    if hit_ball.ycor() > 300:  
                        hit_ball.sety(300)  
                        hit_ball.dy *= -1 

                    if hit_ball.ycor() < -300:  
                        hit_ball.sety(-300)  
                        hit_ball.dy *= -1  

                    if hit_ball.xcor() > 500:  
                        hit_ball.goto(0, 0)  
                        hit_ball.dy *= -1  
                        left_player += 1  
                        sketch_3.clear()
                        sketch_3.write("{} : {}               {} : {}".format(lp,left_player,rp,right_player), align = "center",font = ("Courier", 24, "normal"))
                        
                    if hit_ball.xcor() < -500:  
                        hit_ball.goto(0, 0)  
                        hit_ball.dy *= -1  
                        right_player += 1  
                        sketch_3.clear()
                        sketch_3.write("{} : {}               {} : {}".format(lp,left_player,rp,right_player), align = "center",font = ("Courier", 24, "normal"))
                        
                    # Collision of ball and paddles  
                    if (hit_ball.xcor() > 425 and  hit_ball.xcor() < 450) and (hit_ball.ycor() < right_paddle.ycor() + 50 and hit_ball.ycor() > right_paddle.ycor() - 50):  
                                       hit_ball.setx(360)  
                                       hit_ball.dx *= -1
                    if (hit_ball.xcor() < -425 and hit_ball.xcor() > -450) and (hit_ball.ycor() < left_paddle.ycor() + 50 and hit_ball.ycor() > left_paddle.ycor() - 50):  
                                       hit_ball.setx(-360)  
                                       hit_ball.dx *= -1
                                      
                             
                    if left_player == 11:
                            if left_player == 11:
                                sketch_3.goto(0,0)
                                sketch_3.write("GAME OVER", align="center", font=("Courier", 50, "normal"))
                                time.sleep(2)
                                screen_3.clear()  # Clear the game page screen
                                # playsound("congratualations.mp3")
                                screen_4.addshape("end_Page.gif")
                                t2.shape("end_Page.gif")
                                sketch_4.goto(-15,90)
                                sketch_4.color("deeppink3")
                                sketch_4.write("{}".format(lp), align="center", font=("Comic Sans MS", 50, "bold"))
                                turtle.Screen().exitonclick()

                            elif right_player == 11:
                                sketch_3.goto(0,0)
                                sketch_3.write("GAME OVER", align="center", font=("Courier", 50, "normal"))
                                time.sleep(2)
                                screen_3.clear()  # Clear the game page screen
                                # playsound("congratualations.mp3")
                                screen_4.addshape("end_Page.gif")
                                t2.shape("end_Page.gif")
                                sketch_4.color("deeppink3")
                                sketch_4.goto(-15,90)
                                sketch_4.write("{}".format(rp), align="center", font=("Comic Sans MS", 50, "bold"))
                                turtle.Screen().exitonclick()

     
screen_1.onclick(button_click)
