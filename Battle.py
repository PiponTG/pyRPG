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
        self.timeline = []
        self.time = 0


    def start_battle(self):
        # generate the timeline
        self.timeline = []
        self.time = 0

        # determine speed advantage
        for characters in self.characters:
            timeline = {'character': characters, 'pos': characters.get_spd_advantage()}
            # create this function in player.py

    def take_turn(self):
        active_characters = []
        for c in self.characters:
            if c['pos'] == self.time:
                active_characters.append(c)

        for c in active_characters:

            if c.is_player():
                # input from player
                self.perform_action()
                pass
            else:
                # input from AI
                self.perform_action()
                pass

        # go down the list of characters performing the actions below

        # display options
        # take action
        # select target

        # resolves effects

        # calculate action's consequence

        # progress the timeline one step
        self.time += 1
        return

    def perform_action(self, action_id=0, target_names=[]):
        # does a move
        # takes in a move ID and targets. If there are too many targets it selects the first one

    def end_battle(self):
        # generates loot for winning team (if player)
        # awards xp
        # displays status screen
        pass

    def generate_loot(self):
        # uses loot table to randomly give monsters valuable items.
        # items go up in value with difficulty lvl of the monster.
        pass
