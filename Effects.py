# this is a  placeholder file for when we decide to implement effects

# effects need to have parameters:
# name
# description

# can use codes to explain parts of the effect to the computer
# for manip i.e: MUL SUB ADD DIV


# x for value parameter
# y for second value parameter (default 0)

# load character stats into dictionary
# modify a stat if effected_stats == key in dictionary (stat name)
# update character stat dictionary


# mod is the modification of the stat
# could be a tuple? ('mul', 0.5)
class Effect:
    def __init__(self, name, e_id, effected_stats=['str'], mod=[]):
        pass
