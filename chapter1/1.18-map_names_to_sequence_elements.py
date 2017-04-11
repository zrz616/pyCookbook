from collections import namedtuple


Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub, sub.addr, sub.joined)


def compute_cost(records):
    Stock = namedtuple('Stock', ['name', 'shares', 'price'])
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total
