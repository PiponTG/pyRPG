#todo
# create function to retrieve stats modified by effects.
# def get_mod_stat(stat):
#
#   calculate stat change from effects
#
#   modified_stat += stat_change
#   return modified_stat


from random import randint
import json

def save_player(player='DEFAULT'):
    if player == 'DEFAULT':
        file_name = 'saves/default_SAVE.json'
        with open(file_name, 'w+') as f:
            json.dump({
                'name':'default',
                'money':999,
                'lvl':50,
                'xp': 0,
                'hp':400,
                'maxhp':500,
                'mp':200,
                'maxmp':300,

                'pwr':1,
                'dfn':2,
                'mag':3,
                'mdf':4,
                'agi':5,
                'eva':6,

                'res':(0,0,0,0,0)
                #'dead':player.is_dead,


            }, f, indent=4)

    else:
        file_name = 'saves/' + player.get_name() + '_SAVE.json'
        with open(file_name, 'w+') as f:
            json.dump({
                'name': 'P1_default',
                'money': player.get_money(),
                'lvl': player.get_lvl(),
                'xp': player.get_xp(),
                'hp': player.get_hp(),
                'maxhp': player.get_maxhp(),
                'mp': player.get_mp(),
                'maxmp': player.get_maxmp(),

                'pwr': player.get_pwr(),
                'dfn': player.get_dfn(),
                'mag': player.get_mag(),
                'mdf': player.get_mdf(),
                'agi': player.get_agi(),
                'eva': player.get_eva(),

                'res': player.get_res()
                # 'dead':player.is_dead(),

            }, f, indent=4)

def load_player(player_name='default'):
    file_name = 'saves/' + player_name + '_SAVE.json'
    with open(file_name) as f:
        stats = json.load(f)
    return Player(**stats)

class Character:
    def __init__(self, name='georgio', lvl=1, hp=0, maxhp=1, mp=0, maxmp=1, pwr=0, dfn=0, mag=0, mdf=0, agi=0, eva=0, res=(0,0,0,0,0)):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.maxhp = maxhp
        self.mp = mp
        self.maxmp = maxmp

        self.pwr = pwr
        self.dfn = dfn
        self.mag = mag
        self.mdf = mdf
        self.agi = agi
        self.eva = eva
        self.res = res

        self.dead = False
    #get
    def get_name(self):
        return self.name
    def get_lvl(self):
        return self.lvl
    def get_hp(self):
        return self.hp
    def get_maxhp(self):
        return self.maxhp
    def get_mp(self):
        return self.mp
    def get_maxmp(self):
        return self.maxmp
    def get_pwr(self):
        return self.pwr
    def get_dfn(self):
        return self.dfn
    def get_mag(self):
        return self.mag
    def get_mdf(self):
        return self.mdf
    def get_agi(self):
        return self.agi
    def get_eva(self):
        return self.eva
    def get_res(self):
        return self.res
    def is_dead(self):
        return self.dead

    #set
    def set_name(self, name):
        self.name = name
    def set_lvl(self, lvl):
        self.lvl = lvl
    def set_hp(self, hp):
        self.hp = hp
    def set_maxhp(self, maxhp):
        self.maxhp = maxhp
    def set_mp(self, mp):
        self.mp = mp
    def set_maxmp(self, maxmp):
        self.maxmp = maxmp
    def set_pwr(self, pwr):
        self.pwr = pwr
    def set_dfn(self, dfn):
        self.dfn = dfn
    def set_mag(self, mag):
        self.mag = mag
    def set_mdf(self, mdf):
        self.mdf = mdf
    def set_agi(self, agi):
        self.agi = agi
    def set_eva(self, eva):
        self.eva = eva
    def set_res(self, res):
        self.res = res

    def is_player(self):
        return True

    def die(self):
        self.hp = 0
        self.dead = True
        print('kilt')

    def hp_change(self, change):
        if not self.dead:
            self.hp += change
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        if self.hp <= 0:
            self.hp = 0
            self.dead = True
    def mp_change(self, change):
        self.mp += change
        if self.mp > self.maxmp:
            self.mp = self.maxmp
        if self.mp <= 0:
            self.mp = 0

    def get_spd_advantage(self):
        return 1

    def to_string(self):
        '''
        print('**CHARACTER SHEET**')
        print('::{}::\nlvl: {}\nhp: {}/{}\nmp: {}/{}\n__________\n\npwr: {}\ndef: {}\nmag: {}\nmgd: {}\nagi: {}\n__________\n\neva: {}\nres: {}'.format(self.name.capitalize(),
                                                                                                                        self.lvl,
                                                                                                                        self.hp,
                                                                                                                        self.maxhp,
                                                                                                                        self.mp,
                                                                                                                        self.maxmp,
                                                                                                                        self.pwr,
                                                                                                                        self.dfn,
                                                                                                                        self.mag,
                                                                                                                        self.mdf,
                                                                                                                        self.agi,
                                                                                                                        self.eva,
                                                                                                                        self.res))
        '''
        print('**CHARACTER SHEET**')
        print(
            '::{}::\nlvl: {}\nhp: {}/{}\nmp: {}/{}\n'.format(
                self.name.capitalize(),
                self.lvl,
                self.hp,
                self.maxhp,
                self.mp,
                self.maxmp))

class Monster(Character):

    def __init__(self, name, **x):
        #super.__init__(self, name, **lookup_monster(name))
        super().__init__(name, **x)
        self.set_hp(self.maxhp)
        self.set_mp(self.maxmp)
        self.gold_reward = self.calc_gold_reward()
        self.xp_reward = self.calc_xp_reward()

    def is_player(self):
        return False

    def calc_gold_reward(self):
        maxrange = (100 * self.lvl)
        minrange = (50 * self.lvl)
        return randint(minrange, maxrange)

    def calc_xp_reward(self):
        return (self.pwr + self.dfn + self.mag + self.mdf + self.agi)

    def calc_loot_reward(self):
        pass

class Player(Character):
    def __init__(self, name='player', money=30, xp=0, inventory=None, **stats):
        super().__init__(**stats)
        self.money = money
        self.xp = xp
        self.inventory = inventory
    def get_money(self):
        return self.money
    def get_xp(self):
        return self.xp
    def get_inventory(self, bag):
        bag.get_contents()





'''
    @dfnperty
    def load_player(self):
        load_dict = {}
        try:
            with open('files\\saves\\{}.txt'.format(self.name), 'r') as f:
                for line in f:
                    line_list = line.split(' ')[:3]

                    if line_list[0] == '*':
                        load_dict[line_list[1]] = float(line_list[2])

                    elif line_list[0] == '@':
                        var_list = next(f).split(' ')[:-1]
                        load_dict[line_list[1]] = var_list

                    elif line_list[0] == '#':
                        if line_list[1] == 'effects':
                            var_list = []
                            print 'hello'
                            for items in next(f).split(', ')[:-1]:
                                var_list.append(effect.Effect(items, **lookup_effect(items)))
                                print var_list
                            load_dict['effects'] = var_list


        except:
            print 'failed to load from file'
        return load_dict

                        elif line_list[0] == '#':
                            if line_list[1] == 'effects':
                                var_list = []
                                print 'hello'
                                for items in next(f).split(', '):
                                    var_list.append(effect.Effect(items, **lookup_effect(items)))
                                    print var_list
                                load_dict['effects'] = var_list


    def load_effects(self):
        effects_list = []
        for name in self.effects:
            effects_list.append()


    def save_player(self):
        with open('files\\saves\\{}.txt'.format(self.name), 'w') as f:
            f.write('* lvl {} \n'.format(self.lvl))
            f.write('* hp {} \n'.format(self.hp))
            f.write('* maxhp {} \n'.format(self.maxhp))
            f.write('* mp {} \n'.format(self.mp))
            f.write('* maxmp {} \n'.format(self.maxmp))

            f.write('* pwr {} \n'.format(self.pwr))
            f.write('* dfn {} \n'.format(self.dfn))
            f.write('* mag {} \n'.format(self.mag))
            f.write('* mdf {} \n'.format(self.mdf))
            f.write('* agi {} \n'.format(self.agi))

            f.write('* eva {} \n'.format(self.eva))

            f.write('@ res \n')
            for i in range(5):
                f.write('{} '.format(pwrn(self.res[i])))
            f.write('\n')


            f.write('# inventory \n')
            for items in self.inventory:
                f.write('{} '.format(items))
            f.write('\n')

            f.write('# effects \n')
            pwring_list = []
            for object in self.effects:
                pwring_list.append(object.get_name())
            for items in pwring_list:
                f.write('{}, '.format(items))
            f.write('\n')





def main():
    c = Player('jojo')
    c.to_pwring()


    pass

if __name__ == "__main__":
    main()
'''