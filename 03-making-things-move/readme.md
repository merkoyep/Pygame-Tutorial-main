# Making things move

Pygame doesn't have a built-in animation class or other helpers as far as I can tell. There may be an external library. We're going to get down to basic concepts here. 

## Learning Objectives

- Describe how still images animate
- Use frames to update the postion of objects 
- Create a new class from a subclass
- Use inherited properties

## Still and moving images

The game loop is called periodically roughly 30 to 60 times per second. This is how all computer applications work when you dig down to the lowest levels. We call these frames. Or frames per second FPS. 

Movies are created in the same way. We shoot a series of still images at the frame rate and display each still image back at the frame rate and your eye perceives this as motion. 

Let's try and experiment. Using the code from the previous example, create a single GameObject. Position it at the left edge of the screen. 

Update the x position of your object by adding 1 in the game loop. Each frame that passes the object should move 1 pixel to the right, draw itself and repeat the process of each loop. 

Try that on your own or follow the instructions below: 


Create a single GameObject at the left edge of the window. 

```python
# Make an instance of GameObject
apple = GameObject(0, 250, 'apple.png')
```

Inside the game loop update the position of the object each frame and render it: 

```python
apple.x += 1
apple.render(screen)
```

Test your program. 

You should see the apple move across the screen. It will probably be moving too fast, and it might speed up. 

Pygame by default tries to draw the screen as fast as the system will allow. This means that the game runs at different speeds on different systems. It also means that depending on what your computer is doing in the background the game might run faster or slower. 

This is not acceptable! We need a consistent frame rate! 

You can fix that by using Pygame's clock. The clock tells pygame when to update. 

Add the following near the top of your code: 

```python
# Get the clock
clock = pygame.time.Clock()
```

At the bottom of your game loop add the following: 

```python
# Update the window
pygame.display.flip()
# tick the clock!
clock.tick(60)
```

Here you're saying the next update should be applied in 1/30th of a second. 

The frame rate of the game should use a consistent frame rate. You shouldn't be changing this number while the game runs. You can set this to a higher number to make the game run more smoothly at the cost of processing more frames. 

To control the speed of objects on the screen you'll change the number of pixels they move each frame. 

For example, if you want the apple to move a little faster you can change its speed like this: 

```python
apple.x += 1.5 # any number here! 
```

You can control the speed of an object by how many pixels it moves in each frame. 

## Subclassing the GameObject

Currently, we have a GameObject that displays an image and can be positioned vis its x and y properties. It can also be rendered to a screen. 

Static game objects are good but games will often have objects that move. We can handle that with a class that contains the movement code. 

Imagine we need to create a fruit falling down the screen. An Apple always starts at the top of the screen and appears at a random horizontal position.

An Apple moves down the screen at a random speed. 

Import random at the top of your code: 

```python
from random import randint
```

 Add a new Apple class: 

 ```python
class Apple(GameObject):
  def __init__(self):
    x = randint(50, 400)
    super(Apple, self).__init__(x, 0, 'apple.png')
    self.dy = (randint(0, 200) / 100) + 1

  def move(self):
    self.y += self.dy
 ```

 This class extends/subclasses the GameObject. 

 It generates a random number for the x position. Then initializes its superclass. This object will always start at a random x and y of 0. It will always display the apple. 

 Apple defines a new attribute `self.dy`. This attributes sets the speed at which apples will fall down the screen. I used a random number from 1.0 to 3.0

 Last, Apple defines a new method `self.move()`. This method adds the dx to the x each frame which should move an Apple down the screen. 

 To move an Apple you need to call its move method each frame. In the game loop at the following: 

 ```python
# Draw apple
apple.move()
apple.render(screen)
 ```

 This is great so far but, what happens when an Apple goes off the bottom of the screen? It keeps going! Our code needs to handle this situation. 

 You can choose one of two routes. You can remove it and destroy the instance. Or you can recycle the instance by moving it back to the top of the screen. 

 Which route you take depends on how you want to handle things and how your game works. For now, let's choose the cycle idea. 

 The goal is to move an Apple back to the top of the screen after moving off the bottom and give it a new random x. From there it will continue down the screen until it reaches the bottom and then recycles again. 

 Add a new method to the `Apple` class and make the following changes to the class constructor: 

 ```python
class Apple(GameObject):
  def __init__(self):
    super(Apple, self).__init__(0, 0, 'apple.png')
    self.dx = 0
    self.dy = (randint(0, 200) / 100) + 1
    self.reset() # call reset here! 

  def move(self):
    self.x += self.dx
    self.y += self.dy
    # Check the y position of the apple
    if self.y > 500: 
      self.reset()

  # add a new method
  def reset(self):
    self.x = randint(50, 400)
    self.y = -64
 ```

Now we initialize our superclass with an x and y of 0. 

Next, we check the y position of the apple. If it's greater than 500 we reset the apple. 

The new reset method sets the starting parameters. This time we'll set `self.y` to `-64`. This should place the apple above the top edge of the screen. And we set `self.x` to a random value. 

Now in the game loop call Apple's move method for each frame. 

```python
# Draw apple
apple.move()
apple.render(screen)
```

## Challenges

**Challenge 1**

We need a Strawberry class. A Strawberry starts off the left edge of the screen and moves horizontally. It should start at a random y position. When it gets off the right side it starts over again from the left at a new random y. 

![challenge-1](../images/03-challenge-1.png)

Use this image for the Strawberry: 

![Strawberry](../solutions/strawberry.png)

**Challenge 2**

The Apples and Strawberries are looking good but for the next step, we need them to run in three "lanes". Look at the picture below. Imagine all of the Apples fall down the screen in a vertical lane (in green). The lanes should be evenly spaced. 

![challenge-2](../images/03-challenge-2.png)

When an Apple set's its position on the x. It should choose one of the three values: 93, 218, 343. You can use an array of these numbers or calculate them for yourself. 

How did I calculate the numbers? I took the width of the screen 500 and divided it by 2 to get the center. The images are 64 pixels wide and are positioned by the left edge. To make an image appear in the center it needs to be at x of 250 - 32 = 218. 

To find the lanes to the left and right I took divided the 250 in half to find the midpoint between the left and center and right of center. Which is 125, and 375. To put the image center at these positions subtract 25 for 93 and 343. 

