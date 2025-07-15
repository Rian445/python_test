num = int(input("Enter a number: "))

if 0 <= num:
    for i in range(1, num + 1):
        if i % 2 == 0:
            print(i)
else:
    print("Number should be bigger than 0")
