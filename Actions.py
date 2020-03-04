# this is a placeholder for the Actions file of the program
# this will contain the Action list available to characters
# actions will use a code similar to effects.

# this will mainly be used in conjunction with battles (it might get moved there on a later date.)

class Action:
    def __init__(self, dmg=0, dur=1, acc=100, cost={}, effects=[]):
        self.dmg = dmg  # negative is healing
        self.dur = dur  # duration of move
        self.acc = acc  # accuracy of action
        self.cost = cost  # cost of move to perform (mana, battery, or stamina)
        self.effects = effects

    def do_action(self, actor, target_list):
        # "targets" are character objects
        for targets in target_list:
            # do effects
            pass
        # do effects to actor (move timeline and other effects like lowered att)

    pass

