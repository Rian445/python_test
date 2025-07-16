principle = 0
rate = 0
time = 0
millionire_time = 0
while True:
    principle = float(input("Enter the principal amount : "))
    print("\n")
    if principle < 0:
        print("Principal amount cannot be negative. Please enter a valid amount.\n")
        principle = float(input("Enter the principal amount : "))
    else:
        break


while True:
    rate = float(input("Enter the rate of interest : "))
    print("\n")
    if rate < 0:
        print("Rate of interest cannot be negative. Please enter a valid rate.\n")
        rate = float(input("Enter the rate of interest : "))
    else:
        break

while True:
    time = float(input("Enter the time in years : "))
    print("\n")
    if time < 0:
        print("Time cannot be negative. Please enter a valid time.\n")
        time = float(input("Enter the time in years : "))
    else:
        break

total_ammount = principle * pow((1 + rate / 100), time)

if total_ammount >= 1000000 and principle < 1000000:

    millionire_time = (time*1000000) / total_ammount
    print(f"Total amount after {time} year/s is: ${total_ammount:.2f}")
    print(f"You will become a millionaire after {millionire_time:.2f} year/s!")

else:
    print(f"Total amount after {time} year/s is: ${total_ammount:.2f}")
