s = 0
counter = int(input("Number of sums: "))
while counter > 0:
    number = int(input("Number to add: "))
    s = s + number
    counter -= 1  #*
    print(f"Result: {s}")
    print(f"Remaining iterations: {counter}")