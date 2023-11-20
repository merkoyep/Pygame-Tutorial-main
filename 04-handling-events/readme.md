# Handling Events

Events represent things that happen in your program. Often, events come from outside the code you write from the system or the API you are using. You'll use events to handle things like keyboard input or mouse clicks. 

## Learning Objectives 

- Use Pygame's events
- Handle events when they occur
- Idenitify the type of an event
- Create an easing function

## Handling events

You used events to check if the game has quit. This lets you know when the game window is closed.

Pygame places all of the events that have occurred since the last clock tick in a list and you can check these events and decide how you want to handle them. 

An event is an object with a type. You'll handle the list of events by iterating over the list of events and checking the type. 

Take a look at the game loop from the previous examples. 

```python
# Create the game loop
running = True
while running:
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Clear screen
  screen.fill((255, 255, 255))
  ...
```

Here we loop over each `event` in `pygame.event.get()`. Then check if the `event.type` is equal to `pygame.QUIT` if so we stop the game loop. 

## Handling Keyboard events

For the next stage, let's look at handling keyboard events. Lots of games use the keyboard. Our game will use the keyboard to move a game object around the screen. 

Take a look at the game loop. Currently, it handles the `pygame.QUIT` event. Add the code below to handle some keyboard events. 

```python
while running:
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    # Check for event type KEYBOARD
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
      elif event.key == pygame.K_LEFT:
        print('LEFT')
      elif event.key == pygame.K_RIGHT:
        print('RIGHT')
      elif event.key == pygame.K_UP:
        print('UP')
      elif event.key == pygame.K_DOWN:
        print('DOWN')
  
  # Clear screen
  screen.fill((255, 255, 255))
  ...
```

When we get a KEYDOWN event it means the user has pressed a key since the last clock tick. If the event type is a key event it will also have a key attribute that will be one of pygames K_ event constants: `K_LEFT`, `K_RIGHT`, `K_UP`, and `K_DOWN`. 

Here we check for these and print the name of the ket. Test this and check the console as you press the arrow keys. 

With this in place, we need to create a player object that can be controlled. 

## Creating the player

Player is an object that will subclass GameObject. 

A player will move up, down, left, or right. The arrow keys will control it. 

We will use this image for the player. You should save this image into the folder where you are working.

![player](../solutions/player.png)

Create a new Player class. This will extend/subclass the GameObject. It will display the player.png above. 

```python
class Player(GameObject):
  def __init__(self):
    super(Player, self).__init__(0, 0, 'player.png')
    self.dx = 0
    self.dy = 0
    self.reset()

  def left(self):
    pass

  def right(self):
    pass

  def up(self):
    pass

  def down(self):
    pass

  def move(self):
    pass

  def reset(self):
    self.x = 250 - 32
    self.y = 250 - 32
```

A `Player` instance will inherit the `x` and `y` attributes and the `render` method. 

`Player` adds the `dx` and `dy` attributes. 

`Player` implements the `reset()` method which will move it to the center of the screen. This is the player's starting position. 

`Player` implements the `move()` method. This method updates the player's position in each frame. 

Last, `Player` implements the `left()`, `right()`, `up()`, and `down()` methods. These methods will be used to move the player when a key is pressed. 

How does the player move? I'd like the Player to move smoothly from position to position. For this, we will use an easing function. The idea is to make the player start fast and slow down as it reaches its target position. Like a car coming to a stop sign. 

For this, we will use the `dx` and `dy` attributes differently than they were used in the Apple class. for Player, the `dx` and `dy` represent the position the player is moving to. 

Edit the `move()` method:

```python
def move(self):
 self.x -= (self.x - self.dx) * 0.25
 self.y -= (self.y - self.dy) * 0.25
```

The formula here calculates the distance to move as: 

```
(x - dx) * 0.25
```

How does that work? Substitute some real numbers. Remember dx is where we want to go and x is our current position. 

```python
# (x - dx) * 0.25
# x = 500
x -= (500 - 250) * 0.25 
# x = 437.5
x -= (437.5 - 250) * 0.25 
# x = 390.625
x -= (390.625 - 250) * 0.25
# x = 355.46875
x -= (355.46875 - 250) * 0.25
# x = 329.1015625
x -= (329.1015625 - 250) * 0.25
...
```

Notice the pattern of the numbers. x is moving towards dx. Sooner or later dx will be 250. 

Another way to think about this equation is this. 

```
(x - dx) * 0.25
```

The first part of the equation, (x - dx), calculates the distance between the two positions. 

```
distance * 0.25
```

The second part calculates how far we want to move this frame. In this case, we want to go 25% of the distance. 

```
x -= distanceToMove
```

In the last step we adjust our x value by the distance we want to move. In other words, we move that amount closer to dx. 

Think about it like this. The formula moves the x values 25% of the way to the dx value. If we repeat this each frame the object will get closer and closer but for each frame, the 25% amount will get smaller so the object slows down until reaches the dx values. 

Mathematically we should never reach the target! This is Zeno's Arrow paradox. While the arrow might never reach the target on the computer numbers have a limit to the decimal precision and get rounded off! 

- https://demonstrations.wolfram.com/ZenosArrowParadoxAndAnInfiniteSeries/

Notice we used the same formula for the x and the y.

Create an instance of the player.

```python
# make an instance of Player
player = Player()
```

Move and render your player in the game loop. You can place this below the Apple. 

```python
while running:
  ...
  # Draw apple
  apple.move()
  apple.render(screen)

  # Draw player 
  player.move()
  player.render(screen)

  # Update the window
  pygame.display.flip()
  ...

```

The player should move to its dx value which is 0. 

If we call `player.move()` each frame the player object will move to its `self.dx` and `self.dy`.

The next step is to get the player to move by a keypress. Implement the `Player` `left`, `right`, `up`, and `down` methods. 

```python
def left(self):
  self.dx -= 100

def right(self):
  self.dx += 100

def up(self):
  self.dy -= 100

def down(self):
  self.dy += 100
```

Calling `player.left()` should make the player move to the left, and the same for `player.right()` etc. 

Add a call to each of these methods in the event handling script in the game loop. 

```python
while running:
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
      elif event.key == pygame.K_LEFT:
        player.left()
      elif event.key == pygame.K_RIGHT:
        player.right()
      elif event.key == pygame.K_UP:
        player.up()
      elif event.key == pygame.K_DOWN:
        player.down()

  ...
```

Test that out and solve any issues. 

## Challenges

**Challenge 1**

Currently, the player can move off the edge of the screen. The goal of this challenge is to prevent that! 

Remember dx and dy are the values that determine where the player will move to. You need to make sure these are never less than 0 or greater than 500. 

For extra style points consider the size of the player when it reaches the edges. 

**Challenge 2**

Imagine for the game the player can only move to one of the intersections of those lanes that the apples and strawberries move along. 

The player should move from one lane to the next with a single keypress.

![Challenge 2](../images/04-challenge-2.png)