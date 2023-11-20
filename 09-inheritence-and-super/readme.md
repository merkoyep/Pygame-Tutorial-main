# Inheritence and Super

This inheritance stuff is great but maybe it's not that great if you're not using all of the features. 

We have to make some changes to get the most out of it. This might seem a little painful at this point. But it's par for the course in the life of a software developer. Over time we take shortcuts to get things done on time and along the way we incur Technical debt. Which we need to pay off by refactoring previously written code. 

## Inheritance Review

Pygame provides the `Sprite` class. It lives at `pygame.sprite.Sprite`. It has methods and properties that allow us to add the sprite to groups, remove it from the screen, and check for collisions with other sprites. 

It didn't have methods to move and draw an image. So you made a new class, a few new classes in fact that could do these things but were also `Sprite`s. In this way the new classes could be added to groups, removed from the screen, and checked for collisions with other `Sprite`s. 

You did this through inheritance!

`Sprite`
- Methods
  - `self.kill()` - removes a sprite

We need an object to draw things on the screen. 

`GameObject` - extends `Sprite`
- Attributes
  - `self.surf` - holds the image to draw
  - `self.x` - location on the x axis
  - `self.y` - location on the y axis
  - `self.rect` - defines the area of the GameObject

- Methods
  - `self.render(screen)` - draws our surf on a screen

 We need some objects with specialized behaviors. 

 Apples move across the screen horizontally. 

`Apple`
- Attributes
  - `self.dx` - speed on the x axis
  - `self.dy` - speed on the y axis
- Methods
  - `self.move()` - moves the Apple
  - `self.reset()` - resets the Apple

The `GameObject` is a `Sprite` that renders a picture. The `Apple` is a `GameObject` that draws an image of an apple and moves.

The `Strawberry` class is similar to the `Apple`. With the difference that it draws a strawberry and it moves in a different direction. 

The `Bomb` class is similar to `Apple` also. 

All three classes `Apple`, `Bomb`, and `Strawberry` share the attributes `dx`, `dy`, and the `move()` method. They differ in how they implement `move()`. 

For example `Apple`:

```python
def move(self):
  self.x += self.dx
  self.y += self.dy
  # Apple checks the y
  if self.y > 500: 
    self.reset()
```

`Strawberry`

```python
def move(self):
  self.x += self.dx
  self.y += self.dy
  # strawberry checks the x
  if self.x > 500: 
    self.reset()
```

`Bomb`

```python
def move(self):
  self.x += self.dx
  self.y += self.dy
  # bomb checks both the x and y
  if self.x > 500 or self.x < -64 or self.y > 500 or self.y < -64:
    self.reset()
```

We can refactor this and move the `move` method into our superclass. The dx and dy attributes can also be moved into the `GameObject` class! 

**Challenge**

Try that on your own. Move the `dx` and `dy` attributes into the `GameObject` class. Give them a default value of `0` in the `GameObject` `__init__`. They should still be set in the `Apple`, `Strawberry`, and `Bomb` classes in the same way they were. 

## Using super

The `move()` method is almost the same for each class: `Apple`, `Strawberry`, `Bomb`. The difference is in when/why they call `reset()`.

I feel all `GameObjects` will want to move. So we can put the move method there or at least this much of it: 

```python
class GameObject(pygame.sprite.Sprite):
 ...

  def move(self):
    self.x += self.dx # Same as Apple
    self.y += self.dy # same

 ...
```

The `Apple` class looks almost the same:

```python
class Apple(GameObject):
 ...

  def move(self):
    self.x += self.dx # these lines are the same!
    self.y += self.dy # same
    if self.y > 500:
      self.reset()

 ...
```

**Important!** When `Apple` implements `move()` it is overriding the implementation in `GameObject`. When you call `apple.move()` only the code in the `Apple` class is being executed. 

You can also call the method in your superclass using: `super()`. That would be good here! 

Change `Apple` like this: 

```python
class Apple(GameObject):
 ...

  def move(self):
    super().move() # call move() in our super class!
    if self.y > 500:
      self.reset()

 ...
```

Now `Apple` can use the `move()` method in the `GameObject` and decide how it will call `reset()`.

**Challenge**

Use this same idea in the `Strawberry` and `Bomb` classes!

Take a look at the `move()` method in the `GameObject` class. When you call `super().move()` you're running this code. So you can remove that code from your implementation of `move()` in the `Strawberry` and `Bomb`. 

## What about the Player? 

The player implements a different moving system. It's different enough that `Player` overrides and completely ignores the `move()` method that's implemented in `GameObject`. 

## Inheritance Tree

The inheritance tree shows who inherits from whom. For example: 

- Grandparent
  - Parent
  - Child

**Challenge**

Draw an inheritance tree that shows how `Sprite`, `GameObject`, `Apple`, `Strawberry`, and `Bomb` inherit from each other. 

<details>
<summary>

**Solution**

</summary>

- `Sprite`
  - `GameObject`
  - `Apple`
  - `Strawberry`
  - `Bomb`

</details>
