# keyword if elif else

animal = "snake"

if animal == "snake":
    print("this is a snake")
elif animal == "cat":
    print("this is a cat")
else:
    print("unknow animal")

# short hand if else

# animal = "cat"
print("this is a cat") if animal == "cat" else print("this is not a cat")

# example in a variable
animal_sound = 'meow' if animal == 'cat' else "bark"
print(animal_sound)



# multiple condition
print('this is a cat') if animal == "cat" else print("this is a dog") if animal =="dog" else print("this is not a cat or a dog")