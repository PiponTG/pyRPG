import Characters
import Items


# This class will hold the logic for battles in the game.
# Battles are free for all but each player can be assigned a team.
# Last team standing wins.
# There can be unlimited teams.

class Battle:
    def __init__(self, characters):
        # this should be a list of dictionaries (keys = character and team)
        self.characters = characters

    def start_battle(self):
        # determine everyone's turn order and speed advantage
        # generate the timeline
        pass
    def take_turn(self):
        # progress the timeline one step
        pass
    def end_battle(self):
        # generates loot for winning team (if player)
        # awards xp
        pass

    def generate_loot(self):
        # uses loot table to randomly give monsters valuable items.
        # items go up in value with difficulty lvl of the monster.
        pass
