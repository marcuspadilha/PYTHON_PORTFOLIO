# library
from time import sleep


# function
def counter(start, end, pace):
    print("\033[1;38m-=" * 20)
    sleep(0.5)
    print(f"\033[1;38mCount from {start} to {end} by {pace}.")
    if pace >= 0:
        for count in range(start, end + 1, pace):
            print("\033[1;34m",count, end=" ")
            sleep(0.3)
        print()
    else:
        for count in range(start, end - 1, pace):
            print("\033[1;31m",count, end=" ")
            sleep(0.3)
        print()


# enhancement
counter(1, 10, 1)
sleep(0.5)
counter(10, 0, -2)
sleep(0.5)
print("\033[1;38m-=" * 20)
sleep(0.5)
print("\033[1;38mNow it is your time to customize the counter.")
sleep(0.5)
# input
start = int(input("Enter start: "))
sleep(0.5)
end = int(input("Enter end: "))
sleep(0.5)
pace = int(input("Enter pace: "))
sleep(0.5)
# output
counter(start, end, pace)
print("\033[1;38m-=" * 20)
input()
