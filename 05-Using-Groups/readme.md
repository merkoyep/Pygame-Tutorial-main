# Using Groups

Pygame has some special features that work with Sprites. Often games use groups of elements. These groups often interact. 

Sprites in a group might collide, pick up, or be absorbed by Sprites in another group. This translates to writing code that looks at each member of a group and calls methods on each member or runs each member through a method. 

You could write code that works with a collection of Sprites but this so common Pygame gives us a Class for that purpose. 

## Learing Objectives 

- Use Pygame's groups
- Use polymorphism to handle groups of similar objects
- Use cartesian coordinates

## Make a new Group

Pygame supplies a Group class in `pygame.sprite.Group`. `Group` is a class that manages a collection of Sprites. Since `GameObject` is a `Sprite` (it extends/subclasses `Sprite`) and `Apple`, `Strawberry`, and `Player` all extend/subclass `GameObject` they are all Sprites!

Make a new instance of `pygame.sprite.Group()`

```python
# Make a group
all_sprites = pygame.sprite.Group()
```

Then add all of your "Sprites" to the `all_sprites` group. Be sure to do this outside the game loop since it only needs to happen once time. 

```python
# Add sprites to group
all_sprites.add(player)
all_sprites.add(apple)
all_sprites.add(strawberry)
```

Now we can use the group to move and render all of the Sprites. Notice that all Sprites implement a `move()` method and a `render()` method. They implement these in the same way. This is polymorphism. It allows our Sprite collection to treat all entities the same way.

In the game loop **remove the code that currently moves and renders player and apple.** Replace it with the code below.

```python
# Clear screen
screen.fill((255, 255, 255))
# Move and render Sprites
for entity in all_sprites:
	entity.move()
	entity.render(screen)
# Update the window
pygame.display.flip()
```

With this system in place, you can have as many "Sprites" as you like in the `all_sprites` Group and they would all move and render every frame. 

Think about how each class implements move and render. Since these are all implemented the same way the process here is easier. That's polymorphism working for us!

- https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group

## Keeping everything in its lane

If you haven't done it already this section will revise the existing classes to keep all of the sprites in their lanes. 

If you did solve this in the earlier stretch challenge you can compare your solution against the solution here. 

Since the game window is a square the lane positions are the same vertically and horizontally. 

The window is 500 by 500. The center is 250. The Sprites are 64 by 64. Since the sprites are positioned by their top and left edges we need to offset them by half their width and height of the sprite (64 / 2 = 32). 

![center offset](../images/05-center-offset.png)

The two lanes on either side of the center can be calculated in any way you like. I took half the distance and subtracted 32. This was 

![center offset 2](../images/05-center-offset-2.png)

So the numbers are 93, 218, and 343. You could write an algorithm to calculate these... but we'll just use them as is here. 

We'll use a List to store the values. We will need to choose a random value from the list so import `random.choice` at the top of your script:

```python
from random import randint, choice
```

Define a variable at the top of your script: 

```python
lanes = [93, 218, 343]
```

### Keep the Apple in its lane

Next modify your `Apple` class. Change the `reset()` method: 

```python
def reset(self):
	self.x = choice(lanes)
	self.y = -64
```

Here the Apple chooses a random value from the `lanes` List when it needs an x position. 

If you haven't made the `Strawberry` class. This class is the same as the `Apple` except it moves horizontally instead of vertically.

`Strawberry` should choose a random value from lanes for its y position when it resets and its x should -64! 

### Keep the Player in its lane

The player can change lanes. So it should keep track of its vertical and horizontal lane index. 

Add two new attributes to the player. 

```python
class Player(GameObject):
	def __init__(self):
		super(Player, self).__init__(0, 0, 'player.png')
		self.dx = 0
		self.dy = 0
		self.pos_x = 1 # new attribute
		self.pos_y = 1 # new attribute
		self.reset()
```

Update the Player's `reset()` method so it places the player in the center lanes. 

```python
def reset(self):
	self.x = lanes[self.pos_x]
	self.y = lanes[self.pos_y]
	self.dx = self.x
	self.dy = self.y
```

Notice! that `self.pos_x` is the index of the horizontal position in the lanes List! `self.pos_y` is the index of the vertical position in the lanes List. 

The Player can change lanes but should also stick to the available lanes. When we want the player to change lanes we set `self.dx` or `self.dy`. A new method would help keep this process DRY. Add this new method to `Player`: 

```python
def update_dx_dy(self):
	self.dx = lanes[self.pos_x]
	self.dy = lanes[self.pos_y]
```

Your methods don't have to be long and complicated to be useful! Short methods are good when they handle a single task!

Now update the `left()`, `right()`, `up()`, and `down()` methods: 

```python
def left(self):
	if self.pos_x > 0:
		self.pos_x -= 1
		self.update_dx_dy()

def right(self):
	if self.pos_x < len(lanes) - 1:
		self.pos_x += 1
		self.update_dx_dy()

def up(self):
	if self.pos_y > 0:
		self.pos_y -= 1
		self.update_dx_dy()

def down(self):
	if self.pos_y < len(lanes) - 1:
		self.pos_y += 1
		self.update_dx_dy()
```

Notice each of these increments or decrements `self.pos_x` or `self.pos_y`. Each check to make sure the value is not outside the range of the `lanes` List. After updating a value they all call `self.update_dx_dy()`. 

### Test the Game

At this stage, you should give your game a thorough test. Play with it for a while to make sure that things are working correctly in all circumstances. 

- Check the player 
 - the player should be able to move to all of the available lanes horizontal and vertical
 - the player should not move outside of the available lanes
- Check the fruit. To do this you'll have to watch patiently as the fruit move and recycle. 
 - Make sure Apple eventually uses all of the available lanes
 - Make sure the Strawberry uses all of the available lanes
 - The Apple and Strawberry should move off the Screen and start from off the opposite side. 

## Challenges

**Challenge 1**

The fruit is looking pretty good but everything has a very down and to the right thing going on. It would be nice if there was some up-and-to-the-right stuff. 

Modify the `Apple` class so that each time an `Apple` resets it chooses a direction up or down. If it chooses up it moves up from the bottom of the screen off the top edge. 

Modify the `Strawberry` so that it chooses to move from right to left or left to right each time it resets.

**Challenge 2** 

Make a Bomb class. A Bomb is a GameObject. It moves like Apple and Strawberry. A Bomb chooses to either move up, down, left, or right. Each time it resets it chooses a different direction. 

Make an instance of Bomb and add it to the `all_sprites` group.
 