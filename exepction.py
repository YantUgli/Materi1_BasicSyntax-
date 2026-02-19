"""
litarly sama kaya try catch di node

try:
(statements) -> run this as a normal part of program

except:
(statements) -> execute this when there is an exception

else:
(statements) -> execute this only if no exceptions are raised

finally:
(statements) -> always execute this

"""

x = 10

try:
    result = x / 1
except ZeroDivisionError:
    print("ga bisa membagi 0")
else:
    print("ini hasil pembagiannya: ", result)
finally:
    print("this will always run")