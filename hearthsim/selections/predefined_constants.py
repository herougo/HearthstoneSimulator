from hearthsim.selections.selections import (SelectCharacter, SelectFriendlyMinion, RandomCharacter,
                                             HeroSelection, OwnSelf, AdjacentMinions, AllFriendlyCharacters,
                                             AllFriendlyMinions, AllOtherFriendlyCharacters, AllOtherFriendlyMinions)

SELECT_CHARACTER = SelectCharacter()
SELECT_FRIENDLY_MINION = SelectFriendlyMinion()
ALL_FRIENDLY_CHARACTERS = AllFriendlyCharacters()
ALL_FRIENDLY_MINIONS = AllFriendlyMinions()
ALL_OTHER_FRIENDLY_CHARACTERS = AllOtherFriendlyCharacters()
ALL_OTHER_FRIENDLY_MINIONS = AllOtherFriendlyMinions()
RANDOM_OTHER_CHARACTER = RandomCharacter(ALL_OTHER_FRIENDLY_CHARACTERS)
RANDOM_OTHER_FRIENDLY_MINION = RandomCharacter(ALL_OTHER_FRIENDLY_CHARACTERS)
PLAYER = HeroSelection(opposing=False)
OPP = HeroSelection(opposing=True)
OWN_SELF = OwnSelf()
ADJACENT_MINIONS = AdjacentMinions()