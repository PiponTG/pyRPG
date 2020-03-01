import json

class ItemList:
    def __init__(self):
        self.item_list = self.load_item_list()

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

    def print_item_list(self):
        for items in self.item_list:
            print(items.get_name())


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



class Treasure(Item):
    def __init__(self, price=0, **stats):
        super().__init__(**stats)
        self.price = price

    def get_price(self):
        return self.price
    def set_price(self, price):
        self.price = price

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

    def get_kw(self):
        return {'i_type': 'Equipment',
                'name': self.name,
                'description': self.description,
                'e_type': self.e_type,
                'effects': self.effects}

class Bag:
    def __init__(self, contents=[]):
        self.contents = contents
        if len(self.contents) == 0:
            self.empty = True
        else:
            self.empty = False
    def is_Bag(self):
        return True
    def is_empty(self):
        if len(self.contents) == 0:
            return True
        else:
            return False

    def add_item(self, item, quantity=1):
        flag = False
        for items in self.contents:
            if items[1] == item:
                flag = True
                items[2] += quantity
                if items[2] > 99:
                    items[2] = 99
        if not flag:
            # need to replace Item() object here and replace it with load_item(name)
            self.contents.append([Item(), int(quantity)])

    def remove_item(self, item, quantity=1):
        for items in self.contents:
            if items[0].get_name() == item:
                items[1] -= quantity
                if items[1] <= 0:
                    self.contents.remove(items)


    def get_contents(self):
        for items in self.contents:
            pass
    def print_inv(self):
        if not self.is_empty():
            for items in self.contents:
                print(items[0].get_name() + ': ' + str(items[1]))
        else:
            print('bag empty')




