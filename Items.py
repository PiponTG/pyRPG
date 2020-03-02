import json

class ItemList:
    def __init__(self):
        self.item_list = self.load_item_list()

    # Loads item list from json file "SAVES/itemlist.json"
    @staticmethod
    def load_item_list():
        item_list = []
        with open('saves/itemlist.json', 'r') as f:
            json_decode = json.load(f)
            for ob in json_decode:
                i_type = ob.pop('i_type')
                if i_type == 'Treasure':
                    item_list.append(Treasure(**ob))
                elif i_type == 'Consumable':
                    item_list.append(Consumable(**ob))
                elif i_type == 'KeyItem':
                    item_list.append(KeyItem(**ob))
                elif i_type == 'Equipment':
                    item_list.append(Equipment(**ob))
                else:
                    print('ERROR - UNRECOGNIZED TYPE')
        return item_list

    def save_item_list(self):
        dict_list = []
        for items in self.item_list:
            dict_list.append(items.get_kw())
        with open('saves/itemlist.json', 'w+') as f:
            json.dump(dict_list, f, indent=4)

    def add_item(self, i_type=None, name=None, description=None, price=None, effects=None, key_id=None, e_type=None):
        if name is None:
            print('an item needs a name!')
            return

        # pre-generates created item
        if i_type == 'Treasure':
            stats = {'name': name,
                     'description': description,
                     'price': price}
            new_item = Treasure(**stats)
        elif i_type == 'Consumable':
            stats = {'name': name,
                     'description': description,
                     'effects': effects}
            new_item = Consumable(**stats)
        elif i_type == 'KeyItem':
            stats = {'name': name,
                     'description': description,
                     'key_id': key_id}
            new_item = KeyItem(**stats)
        elif i_type == 'Equipment':
            stats = {'name': name,
                     'description': description,
                     'effects': effects,
                     'e_type': e_type}
            new_item = Equipment(**stats)




        for items in self.item_list:
            # overwrites old item with same name
            if items.get_name() == name:
                items = new_item
                return
        # if it cant find an item with that name it makes one up
        self.item_list.append(new_item)

    def remove_item(self, name=None):
        if name is None:
            print('an item needs a name!')
            return

        for items in self.item_list:
            if items.get_name() == name:
                self.item_list.remove(items)
                return
        print('item not found')

    def edit_item(self, item, name=None, description=None, price=None, effects=None, key_id=None, e_type=None):
        # ability to load item and change its attributes
        # (will be more useful when i have a GUI to preload  the values in)
        # check for None, if not None: change the values!
        pass

    def sort_item_list(self, sort_key='name'):
        if sort_key is 'name':
            self.item_list.sort(key=lambda x: x.get_name())
        elif sort_key is 'type':
            t_list = []
            c_list = []
            k_list = []
            e_list = []

            for items in self.item_list:
                if type(items) == Treasure:
                    t_list.append(items)
                elif type(items) == Consumable:
                    c_list.append(items)
                elif type(items) == KeyItem:
                    k_list.append(items)
                elif type(items) == Equipment:
                    e_list.append(items)
                else:
                    print('ERROR - NOT CORRECT TYPE')

            t_list.sort(key=lambda x: x.get_name())
            c_list.sort(key=lambda x: x.get_name())
            k_list.sort(key=lambda x: x.get_name())
            e_list.sort(key=lambda x: x.get_name())

            self.item_list = c_list + e_list + k_list + t_list
        else:
            print('ERROR - unable to sort by that key')

        for items in self.item_list:
            print(items.get_name())

    def print_item_list(self):
        for items in self.item_list:
            print(items.get_name())

    def get_item(self, item_name=''):
        if item_name is '':
            print('error - no name provided')
            return
        else:
            for items in self.item_list:
                if items.get_name() == item_name:
                    return items
            print('unable to find item')
        return None

class Item:
    def __init__(self, name='???', description='What is this?'):
        self.name = name
        self.description = description

    def get_name(self):
        return self.name
    def get_description(self):
        return self.description
    def set_name(self, name):
        self.name = name
    def set_description(self, description):
        self.description = description

    def get_type(self):
        return 'Item'

class Treasure(Item):
    def __init__(self, price=0, **stats):
        super().__init__(**stats)
        self.price = price

    def get_price(self):
        return self.price
    def set_price(self, price):
        self.price = price

    def get_type(self):
        return 'Treasure'
    def get_kw(self):
        return {'i_type': 'Treasure',
                'name': self.name,
                'description': self.description,
                'price': self.price}

class Consumable(Item):
    def __init__(self, effects=None, **stats):
        super().__init__(**stats)
        if effects is None:
            self.effects = []
        else:
            self.effects = effects

    def get_effects(self):
        return self.effects

    def add_effect(self, effect):
        # once effects are created for weapons/equipment we can use this to give current armor new effects! UPGRADES!
        # when same effect is active it will be overwritten when you add it again
        pass
    def remove_effect(self, effect):
        # can remove old effects from weapons/equipment
        pass


    def get_type(self):
        return 'Consumable'
    def get_kw(self):
        return {'i_type': 'Consumable',
                'name': self.name,
                'description': self.description,
                'effects': self.effects}

class KeyItem(Item):
    def __init__(self, key_id='000', **stats):
        super().__init__(**stats)
        self.key_id = key_id

    def get_key_id(self):
        return self.key_id
    def set_key_id(self, key_id):
        self.key_id = key_id

    def get_type(self):
        return 'KeyItem'
    def get_kw(self):
        return {'i_type': 'KeyItem',
                'name': self.name,
                'description': self.description,
                'key_id': self.key_id}

class Equipment(Item):
    def __init__(self, e_type=None, effects=None, **stats):
        super().__init__(**stats)
        self.e_type = e_type
        if effects is None:
            self.effects = []
        else:
            self.effects = effects

    def get_type(self):
        return 'Equipment'
    def get_kw(self):
        return {'i_type': 'Equipment',
                'name': self.name,
                'description': self.description,
                'e_type': self.e_type,
                'effects': self.effects}

class Bag:
    def __init__(self, contents=[]):
        self.contents = contents

    def is_empty(self):
        if len(self.contents) == 0:
            return True
        else:
            return False

    def add_item(self, item_name, quantity=1):
        for items in self.contents:
            if items['name'] == item_name:
                items['quantity'] += quantity
                if items['quantity'] > 99:
                    items['quantity'] = 99
                return
        try:
            self.contents.append({'name': item_name, 'quantity': int(quantity), 'type': i.get_item(item_name).get_type()})
        except:
            print('item does not exist')

    def remove_item(self, item_name, quantity=1):
        for items in self.contents:
            if items['name'] == item_name:
                items['quantity'] -= quantity
                if items['quantity'] <= 0:
                    self.contents.remove(items)
                return
        print('item not found. unable to remove')

    def get_contents(self):
        return self.contents

    def print_inv(self):
        if not self.is_empty():
            for items in self.contents:
                print('<' + items['type'] + '> ' + items['name'] + ': ' + str(items['quantity']))
        else:
            print('bag empty')

    def sort_content_list(self, sort_key='name'):
        if sort_key is 'name':
            self.contents.sort(key=lambda x: x['name'])
        elif sort_key is 'type':
            t_list = []
            c_list = []
            k_list = []
            e_list = []

            for items in self.contents:
                if items['type'] == 'Treasure':
                    t_list.append(items)
                elif items['type'] == 'Consumable':
                    c_list.append(items)
                elif items['type'] == 'KeyItem':
                    k_list.append(items)
                elif items['type'] == 'Equipment':
                    e_list.append(items)
                else:
                    print('ERROR - NOT CORRECT TYPE')

            t_list.sort(key=lambda x: x['name'])
            c_list.sort(key=lambda x: x['name'])
            k_list.sort(key=lambda x: x['name'])
            e_list.sort(key=lambda x: x['name'])

            self.contents = c_list + e_list + k_list + t_list
        else:
            print('ERROR - unable to sort by that key')

i = ItemList()



