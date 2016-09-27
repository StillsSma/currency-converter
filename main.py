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
        return Money(self.number + other.number * Money.exchange[other.currency], self.currency)
    def __sub__(self, other):
        return self.number - other.number * Money.exchange[other.currency]
    def __mul__(self, other):
        return self.number * (other.number * Money.exchange[other.currency])


print(Money(100.4, "USD") + Money(56.6, "EUR"))

print ((Money(1, "USD") + Money(1, "EUR") + Money(1, "BTC") + Money(1, "USD")).number)
