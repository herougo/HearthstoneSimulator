# Software Design Issues

- Is _effect_area necessary for effects?
- Why not use MVC?
  - This is a prototype with the purpose of exploring how to design the card effect engine. I will probably implement it in MVC eventually.
- DecisionMaker get_action returning multiple types
- Whose job should it be to execute play minion? Game or DecisionMaker?
- Do we need affected_slot vs origin_slot?
- Are start and stop needed for ContinuousSelectionFieldEffect?
  - no because it only resolves when a minion is played or dies
- maybe group hands, players, weapons, battleboard, and decks into CardSlotManager