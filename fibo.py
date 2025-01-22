def is_armstrong_number(num):
    digits = list(map(int, str(num)))
    return num == sum([d**len(digits) for d in digits])
num=int(input("enter a number : "))
print("Is num an Armstrong Number?", is_armstrong_number(num))