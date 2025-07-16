import math
principle = 0
rate = 0
time = 0
millionire_time = 0
while True:
    principle = float(input("Enter the principal amount : "))
    print("\n")
    while principle < 0:
        print("Principal amount cannot be negative. Please enter a valid amount.\n")
        principle = float(input("Enter the principal amount : "))
        print("\n")
    else:
        break


while True:
    rate = float(input("Enter the rate of interest : "))
    print("\n")
    while rate < 0:
        print("Rate of interest cannot be negative. Please enter a valid rate.\n")
        rate = float(input("Enter the rate of interest : "))
        print("\n")
    else:
        break

while True:
    time = float(input("Enter the time in years : "))
    print("\n")
    while time < 0:
        print("Time cannot be negative. Please enter a valid time.\n")
        time = float(input("Enter the time in years : "))
        print("\n")
    else:
        break

total_ammount = principle * pow((1 + rate / 100), time)

millionire_time = math.log(1_000_000 / principle) / math.log(1 + rate / 100)

if total_ammount >= 1000000 and principle < 1000000 and millionire_time >= 1:

    print(f"Total amount after {time} year/s is: ${total_ammount:.2f}\n")
    print(
        f"You will become a millionaire after {millionire_time:.2f} year/s!\n")

elif total_ammount >= 1000000 and principle < 1000000 and millionire_time < 1:
    print(f"Total amount after {time} year/s is: ${total_ammount:.2f}\n")
    print(
        f"You will become a millionaire in less than a year! exact to be {int(millionire_time*10)} months \n")

else:
    print(f"Total amount after {time} year/s is: ${total_ammount:.2f}\n")
