class Money:

    exchange = {"USD" : 1, "EUR" : .9, "JPY": 100.3, "BTC": .00165}

    def __init__(self, number, currency = "USD"):
        self.number = number
        self.currency = currency
        self.value = 1 / Money.exchange[self.currency]

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __eq__(self,other):
        return self.value == other.value

    def __ne__(self,other):
        return self.value != other.value

    def __add__(self, other):
        return self.number + other.number * Money.exchange[other.currency]

    def __sub__(self, other):
        return self.number - other.number * Money.exchange[other.currency]

    def __str__(self):
        return "Value is {}".format(self)

print(Money(100, "USD") - Money(56, "EUR"))
