import Characters
import Items


# This class will hold the logic for battles in the game.
# Battles are free for all but each player can be assigned a team.
# Last team standing wins.
# # There can be unlimited teams.

class Battle:
    def __init__(self, characters, stage='default'):
        # this should be a list of dictionaries (keys = character and team)
        self.characters = characters
        self.stage = stage
        self.time = 0

    def start_battle(self):
        # generate the timeline
        timeline = []
        self.time = 0

        # determine speed advantage
        for characters in self.characters:
            timeline = {'character': characters, 'pos': characters.get_spd_advantage()}
            # create this function in player.py

    def take_turn(self):

        # display options
        # take action
        # select target
        # resolves effects

        # progress the timeline one step
        self.time += 1
        return

    def end_battle(self):
        # generates loot for winning team (if player)
        # awards xp
        # displays status screen
        pass

    def generate_loot(self):
        # uses loot table to randomly give monsters valuable items.
        # items go up in value with difficulty lvl of the monster.
        pass
