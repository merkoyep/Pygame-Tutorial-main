# Polymorphism

The game has many different objects. But it needs to manage them all at the same time. 

In the you've been working on this happens with Sprites. 

Remember! When class inherits from a super class it is the super class. In other words. If a `GameObject` in herits from `Sprite` then a `GameObject` is a `Sprite`. 

The same is true for `Apple`. The `Apple` inherits from `GameObject` and `GameObject` inherits from `Sprite`. 

Remember the inheritence chart: 

- `Sprite`
  - `GameObject`
    - `Apple`
    - `Strawberry`
    - `Bomb`

Since `Apple`, `Strawberry`, and `bomb` are all `GameObject`s we can use them in place of a `GameObject` when our program expects a `GameObject`. 

Where does that happen? Since `GameObject` can be rendered to the screen using the `render()` method. All of the subclasses inherit this method! 

Where does this in the game code? We have a group of sprites callded `all_sprites`. Somewhere in your code you did these things: 

```python
# Make a group
all_sprites = pygame.sprite.Group()

# Add sprites to group
all_sprites.add(player)
all_sprites.add(apple)
all_sprites.add(strawberry)
all_sprites.add(bomb)
```

Notice you added several instances to `all_sprites`. They are all instances of different classes. But they all inherit from `GameObject`, which inherits from `Sprite`. So everything in the `all_sprites` group is a `Sprite`!

Later in your code (look in the game loop) you did this: 

```python
# Move and render Sprites
for entity in all_sprites:
  entity.move()
  entity.render(screen)
```

If an `entity` doesn't have a `move()` and a `render()` method our code breaks. Luckily we understand that all of our `GameObjects` have a `move()` and `render()` methods and `all_sprites` only contains `GameObjects`. 

When we play the game we can see that there are four types of objects. These are all visually different. 

This is possible because each class defines a different value for `surf`. They all use the same `render()` method from `GameObject`.

In the loop above we draw them all the same way, by calling the `render(screen)` on each. 

They all behave differently. Some move down, some move across, and some go either direction, and one is controlled by the keyboard. 

This is possible because each of these classes implements their own move `method()`. Some of the classes invoke the `move()` method from their parent class `GameOBject` and others use their own implementation. And some do both using `super().move()`. 

**Ploymorphism** allows you to call `move()` on each of the objects while each object moves in it's own way. 

Think about it like this. You can have a collection of objects that all behave differently but are handled in the same way. 

For example: You invoke `.move()` on all objects in the collection but the objects all move in their own way. 

From other side the pygame sprite group requires all of it's members to be a group. When you created a group with: `pygame.sprite.Group()` that group expects anything you add to be a `Sprite`. 

But `Sprite`s don't have all of the behaviors we want! By subclassing `Sprite` we can create new classes that are still sprites but have different behaviors. 

Ploymorphism allows us to use instances of `Apple`, `Strawberry`, `Bomb`, and `Player` in a `pygame.sprite.Group`. 






