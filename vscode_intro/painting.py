from turtle import *

d = -1
rainbow = ["red", "orange", "yellow", "green", "blue", "dark blue", "dark violet"]
while True:
    d += 1
    if d == 7:
        d = -1
    speed(100000)
    color(rainbow[d])
    right(1)
    forward(1)
    circle(100)    

# a = 0
# b = 0
# for i in range (210):
#     a += 1
#     b += 1
#     speed(500)
#     right (a)
#     color("red")
#     forward(b)

# c = 0
# for i in range (100):
#     speed(500)
#     c += 1
#     right (c)
#     circle(100)
#     end_fill()

done()