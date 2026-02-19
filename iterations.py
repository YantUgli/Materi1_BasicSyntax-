# iterating over a list

fruits = ["apple", "banana", "tomato"]

for fruit in fruits:
    print(fruit)


# use "for" untuk index. enumerate nih penting deh
for index, fruit in enumerate(fruits):
    print(f"{fruit} in index {index}")


for number in range(1, 11):
    print(number)

print(enumerate(fruits))