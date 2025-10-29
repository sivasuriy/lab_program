# program2.py
# Fibonacci series without recursion

n = int(input("Enter how many Fibonacci numbers you want: "))

a, b = 0, 1

if n <= 0:
    print("Enter a positive number.")
elif n == 1:
    print("Fibonacci series:", a)
else:
    print("Fibonacci series:", end=" ")
    print(a, b, end=" ")

    for _ in range(2, n):
        c = a + b
        print(c, end=" ")
        a = b
        b = c
