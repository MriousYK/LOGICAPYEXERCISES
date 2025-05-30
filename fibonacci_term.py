### TERM FIBONACCI
n = int(input("Enter the term in the sequence: "))
if n == 1 or n == 2:
    print(f"{n} = 1")
else:
    a = 1
    b = 1
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c
    result = b

print(f"The term {n} of fibonacci is {b}")