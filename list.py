numbers = (list(range(10)))
print(numbers[::2])
print(numbers)
print(numbers[::-1])  # to reverse the list

# unpacing of lists

letters = ["a", "b", "c"]
items = (0, "a")
index, letter = items
for index, letter in enumerate(letters):
    print(index, letter)

# how to remove and add items into list

list = ["a", "b", "c"]
list.append("d")
list.pop()
list.insert(0, "happy")
list.remove("happy")
print(list)

# how to find the index and occurance of the item
list = ["a", "b", "c"]
print(list.count("c"))
if "a" in list:
    print(list.index("a"))

# how sort the lists

list = [3, 2, 5, 1]
list.sort()
print(list)  # this method will give you a new sorted list
print(sorted(list))  # this method will not gonna create
# new list it will just modify it for moment##
print(list.sort(reverse=True))  # it will reverse the list

items = [
    ("nike", 130),
    ("apple", 20),
    ("puma", 50),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)

items = [
    ("a", 0),
    ("n", 130),
    ("p", 50),
]

items.sort(key=lambda item: item[1])
print(items)
print(items[1])

items = [
    ("a", 20),
    ("n", 130),
    ("p", 50),
]
price = []
for item in items:
    price.append(item[1])

print(price)


##### we can use the map function as well####

items = [
    ("a", 20),
    ("n", 130),
    ("p", 50),
]
# price = []
# for item in items:
#     price.append(item[1])


x = map(lambda item: item[1], items)
for item in x:
    print(item)
# filtering the function#


items = [
    ("a", 50),
    ("n", 130),
    ("p", 50),
]

price = []

for item in items:
    if item[1] == 50:
        price.append(item[0])
print(price)

# to filter and map the thing use comprehension function

items = [
    ("a", 50),
    ("n", 130),
    ("p", 50),
]
# price = []
prices = [item[1] for item in items]

print(prices)
result = 10/2
print("this is result{b:10.3f}".format(b=result))

print("{}".format("'python rules!'"))

my = open("my.txt")
# my.read()
# print(my.read())
my.seek(0)
print(my.read())

my = open("my.txt")
with open("my.txt", mode="a")as f:
    print(f.write(" are you happy"))
# my.seek(0)

print(my.read())
