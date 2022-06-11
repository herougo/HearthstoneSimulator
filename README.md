# HearthstoneSimulator

A simulator for the digital card game known as Hearthstone. I wrote this because I thought it would be a challenging software design exercise (how do card effects work?). It was!

Here is a brief overview of why this problem is difficult.

- How do you classify your card effects in a class structure? 
- How do you keep track of them?
- How do you make sure that continuous effects stay in effect?
- How do you allow yourself to easily express a card effect, then have it carry out its duties in a game?
  - e.g. express Battlecry(DrawCard(PLAYER)), and have this object carry out its duties in the game

See docs folder for the following documentation:

- **code_explanation.md**: basic overview of how the code works
- **to_do.md**: to do list
- **software_design_issues.md**: current questions/issues I am examining with the code base
