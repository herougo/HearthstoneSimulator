from hearthsim.selections.core import  SelectCharacterFrom
from hearthsim.selections.selections import (AllOtherMinions, AllOtherCharacters, RandomCharacter,
                                             HeroSelection, OwnSelf, AdjacentMinions, AllFriendlyCharacters,
                                             AllFriendlyMinions, AllOtherFriendlyCharacters, AllOtherFriendlyMinions,
                                             AllCharacters)

ALL_CHARACTERS = AllCharacters()
ALL_FRIENDLY_CHARACTERS = AllFriendlyCharacters()
ALL_FRIENDLY_MINIONS = AllFriendlyMinions()
ALL_OTHER_FRIENDLY_CHARACTERS = AllOtherFriendlyCharacters()
ALL_OTHER_FRIENDLY_MINIONS = AllOtherFriendlyMinions()
ALL_OTHER_MINIONS = AllOtherMinions()
ALL_OTHER_CHARACTERS = AllOtherCharacters()

SELECT_CHARACTER = SelectCharacterFrom(ALL_CHARACTERS)
SELECT_OTHER_FRIENDLY_MINION = SelectCharacterFrom(ALL_OTHER_FRIENDLY_MINIONS)
SELECT_OTHER_CHARACTER = SelectCharacterFrom(ALL_OTHER_CHARACTERS)
SELECT_OTHER_MINION = SelectCharacterFrom(ALL_OTHER_MINIONS)

RANDOM_OTHER_CHARACTER = RandomCharacter(ALL_OTHER_FRIENDLY_CHARACTERS)
RANDOM_OTHER_FRIENDLY_MINION = RandomCharacter(ALL_OTHER_FRIENDLY_CHARACTERS)
PLAYER = HeroSelection(opposing=False)
OPP = HeroSelection(opposing=True)
OWN_SELF = OwnSelf()
ADJACENT_MINIONS = AdjacentMinions()