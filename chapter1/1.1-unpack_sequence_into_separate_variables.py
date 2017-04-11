data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, (year, mon, day) = data
print(name, shares, price, year, mon, day)

_, shares, price, _ = data
print(shares, price)
