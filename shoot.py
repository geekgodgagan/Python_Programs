from random import randint
apple = Actor("apple")
# draw an apple on the screen

def draw():
    screen.clear()
    apple.draw()

#placing the apple
def place_apple():
    apple.x = randint(10,800)
    apple.y = randint(10,600)

#dealing with clicks
def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good shot!")
        place_apple()
    else:
        print("You missed!")
        quit()
# calling function
place_apple()
