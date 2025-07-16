import time
my_time = int(input("Enter the time in seconds: "))
print("\n")
print("Countdown starts now!\n")
for i in range(my_time, 0, -1):
    seconds = int(i % 60)
    minutes = int((i // 60) % 60)
    hours = int(i // 3600)

    print(f"{hours:02}:{minutes:02}:{seconds:02}\n")
    time.sleep(1)

print("Time's up!\n")
print("Countdown finished!\n")
print("Thank you for using the countdown timer!\n")
print("Have a great day!\n")
print("Goodbye!\n")
