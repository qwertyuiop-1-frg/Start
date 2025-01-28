class Drink:
    _volume = 150

    def __init__(self, name, price):
        self.price = price
        self.name = name
        self._remains = self._volume

    def info(self):
        print(f'Name: {self.name}. Price: {self.price} and volume {self._volume}. New volume: {self._remains}')

    def _is_enough(self, need):
        if self._remains >= need and self._remains > 0:
            return True
        else:
            print('Not enough tea (')
            return False

    def sip(self):
        if self._is_enough(20) == True:
            self._remains -= 20
            print('Gulp')

    def small_sip(self):
        if self._is_enough(10) == True:
            self._remains -= 10
            print('Small gulp')

    def drink_all(self):
        if self._is_enough(0) == True:
            self._remains = 0
            print('Very big gulp')

    def tell_price(self):
        print(f'Cost of my drink is...')
        return self.price

class Juice(Drink):

    _juice_name = 'juice'

    def __init__(self, price, taste):
        super().__init__ (self._juice_name,price)
        self.taste = taste

    def info(self):
        print(f'Name: {self.taste}. Price: {self.price} and volume {self._volume}. New volume: {self._remains}')

tea = Drink('Tea', 3)
print(tea.tell_price())
cherry_juice = Juice(100, 'cherry')
print(cherry_juice.tell_price())
cherry_juice.small_sip()
cherry_juice.sip()
cherry_juice.info()
