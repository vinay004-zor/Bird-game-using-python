from ursina import *
import random as r

app = Ursina()

# Create the sky
Sky()

# Load the bird animation
bird = Animation('assets/img',  # Use forward slashes for paths
                 collider='box',  # Corrected the typo here
                 scale=(2, 2, 2),
                 y=5)

# Set the camera to orthographic view
camera.orthographic = True
camera.fov = 20

sky=Animation('assets/img2',
                      y=5)

pipes = []

# Function to update the game state
def update():
    bird.y = bird.y - 4 * time.dt
    for p in pipes:
        p.x = p.x - 2 * time.dt
    touch = bird.intersects()
    if touch.hit or bird.y < -10:
        quit()

# Function to handle input
def input(key):
    if key == 'space':
        bird.y = bird.y + 3

# Create the initial pipe entity
pipe = Entity(model='quad',
              color=color.gray,
              texture='white_cube',
              position=(20, 10),
              scale=(3, 15, 1),
              collider='box')

# Function to create new pipes
def newPipe():
    y = r.randint(4, 12)
    new1 = duplicate(pipe, y=y)
    new2 = duplicate(pipe, y=y-22)
    pipes.extend((new1, new2))
    invoke(newPipe, delay=5)

# Invoke the first pipe creation
newPipe()

# Run the application
app.run()

