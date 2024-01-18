number=int(input("Input a number from 0 to 9999: "))
if number == 0:
    print(f"No digits: 0")
elif 0<number<10:
    print(f"Unit: {number}.")
elif 9<number<100:
    print(f"ten: {number//10}; Unit: {number%10}.")
elif 99<number<1000:
    print(f"Hundred: {number//100}; ten: {(number//10)%10}; Unit: {number%10}.")
elif 999 < number < 10000:
    print(f"Thousand: {number//1000}; Hundred: {(number // 100) %10}; ten: {(number // 10) % 10}; Unit: {number % 10}.")
else:
    print("No answer")
input()