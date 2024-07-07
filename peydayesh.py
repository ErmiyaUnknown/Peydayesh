list_nums = {1, 2, 3, 4}

def find(num1, num2, num3):
    list_new = {num1, num2, num3}
    number = list_nums.difference(list_new)
    number = str(number).strip("{ }")
    print(int(number))
    
find(4, 2, 3)    