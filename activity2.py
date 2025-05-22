print("Is this a prime number")
lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break  # not a prime number, so stop checking
        else:
            print(num)


