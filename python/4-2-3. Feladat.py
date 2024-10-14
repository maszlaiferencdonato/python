num = int(input())
if num % 3 == 0:
    if num % 4 == 0:
        print("3-mal és 4-gyel is osztható")
    else:
        print("csak 3-mal osztható")
else:
    if num % 4 == 0:
        print("csak 4-gyel osztható")
    else:
        print("sem 3-mal, sem 4-gyel nem osztható")
