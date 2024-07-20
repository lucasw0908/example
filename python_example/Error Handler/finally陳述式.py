try:
    print(1/0)
except ZeroDivisionError:
    print("You can't divide by zero....")
finally:
    print("calculation is done....")