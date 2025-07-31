num = int(input("Enter the number: "))

def fact(num):
    if num < 2:
        return 1
    else:
        return num * fact(num - 1)

rslt = fact(num)
print(f"Factorial of {num} is {rslt}")
