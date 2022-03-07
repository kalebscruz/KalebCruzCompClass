import math
import numpy as np
gravity = 9.8
c = 3.0e8

def problemOne(height):
    height = float(input("Enter initial height in meters:"))
    time = float(input("How long has the ball been falling in seconds:"))
    velocity =  gravity * time
    new_height = "{:.2f}".format(float(height - ( velocity *  time )))
    print("The ball is now  " + str(new_height) + " meters in the air")


def relativistic(speed,distance):
    speed = input(print("Enter the speed"))
    distance = input(print("Enter new planet x  light years away"))
    gamma = 1/(np.sqrt(1 - float(speed)**2))
    problem_cont = distance/gamma
    part_a_earth = distance/speed
    cont=0
    part_b_ship = cont/speed
    print("The time to travel to the planet is " + part_a_earth + " from earths frame of reference" )
    print("The time to travel to the planet is " + part_b_ship + " from the ships frame of reference" )

