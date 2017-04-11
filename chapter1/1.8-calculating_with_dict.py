prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
print(sorted(zip(prices.values(), prices.keys())))
print(min_price, max_price)

# zip创建的是只能访问一次的迭代器
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))  # OK
try:
    print(max(prices_and_names))  # 已遍历过在访问时会出错
except ValueError:
    print("iter Error")

# 以键值排序, 仅返回键值
print(min(prices))
print(max(prices))

# 以值排序, 返回值
print(min(prices.values()))
print(max(prices.values()))

# 得到最值的键值信息
print(max(prices, key=lambda k: prices[k]))
print(min(prices, key=lambda k: prices[k]))
