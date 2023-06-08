import random
import string
import time

def passwordGenerator(n=8):
    target = "EWjC90c"
    while True:
        goal = ""
        concat = string.ascii_letters + string.digits
        res = [a:=random.choice(concat) for x in range(n)]
        for i in res:
            goal += i
        print(goal)
        time.sleep(0.3)
        if goal == target:
            break

by_user = int(input("Enter: "))
passwordGenerator(by_user)
