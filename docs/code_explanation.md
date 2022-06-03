# Code Explanation

Here is a breakdown of the core code behind this simulator. You can search the code for the referenced classes.

### Effects

I wrote the effects as classes that can be easily composed with each other. For example, you can write Battlecry(NEffects(DrawCard(PLAYER), n=2)) to express an effect which allows the player to draw 2 cards when a minion's battlecry is triggered. Effects is an abstract class, with the following subclasses:

- One-Time: An effect that happens once.
  - implements the execute method
- Continuous: An effect that is constantly in effect.
  - implements the start, stop, and possibly send_event methods
- Trigger: An effect that runs a specified one-time effect when a certain event occurs (see above battlecry example).
  - implements the start, stop, and send_event methods
- Wrapper: As it's name suggests, objects of this kind are meant to wrap around other effects, and their behaviour depend on the effect object it was wrapped around. See AbusiveSergeant for an example.
- Activated: An effect which is an effect which activates when the user activates it themselves. It is a subclass of TriggerEffect.

### CardSlots

When a game is running, each card is wrapped in its own CardSlot object. These objects help keep track of metadata, stats, etc.

### EffectManager

To manage the effects, I use an effect manager. Each effect is tied to a card slot. When a minion is played, its field effects get pushed to the EffectManager. They are popped when the minion dies. I made a use of dictionary data structures to make sure events are only sent to the relevant effects. This is also true for retrieving effects based on the card slot.
