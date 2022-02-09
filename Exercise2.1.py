import math
from urllib.request import ProxyBasicAuthHandler
gravity = 9.8
c = 3.0e8

def problemOne(height):
    height = float(input("Enter initial height in meters:"))
    time = float(input("How long has the ball been falling in seconds:"))
    velocity =  gravity * time
    new_height = "{:.2f}".format(float(height - ( velocity *  time )))
    print("The ball is now  " + str(new_height) + " meters in the air")

def probelemTwo(height):
    height = float(input("Enter initial height in meters:"))
    time = math.sqrt(2 * height / gravity )
    print("{:.2f}".format(time))

probelemTwo()

##A spaceship travels from Earth in a straight line 
# at relativistic speed v to another planet x light 
# years away. Write a program to ask the user for 
# the value of x and the speed v as a fraction of 
# the speed of light c, then print out the time in 
# years that the spaceship takes to reach its
#  destination (a) in the rest frame of an observer 
# on Earth and (b) as perceived by a passenger on 
# board the ship.t Use your program to calculate the
#  answers for a planet 10 light years away with v = 0.99c.

def relativistic():
    v = input(print("Enter the speed"))
    x = input(print("Enter x"))
    


