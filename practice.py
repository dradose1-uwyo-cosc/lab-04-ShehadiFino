items = ["Apples", "Carrots", "Bread", "Toothpaste", "Milk" ]
prices = [1, 2, 3.5, 2, 4.5]

print("Length of items", len(items))
print("What is this doing?", range(len(items)))
for i in range(len(items)):
    print(f"I bought {items[i]} for ${prices[i]}")

total = 0
for t in prices:
    total = total + t
print(f"I spent ${total} at Walmart")

cheapest = prices[0]
#names = items[0]
for i in range(len(prices)):
    if (prices[i] <= cheapest):
        cheapest = prices[i]
        name = items[i]

print(f"The cheapest item was {name}")

leastIndex = prices.index(min(prices))
mostIndex = prices.index(max(prices))
print(f"The cheapest item was {items[leastIndex]}")
print(f"The most expensive item was {items[mostIndex]}")     

#for item, price in zip(items, prices):
#print(f" I bought {item} for ${price}")