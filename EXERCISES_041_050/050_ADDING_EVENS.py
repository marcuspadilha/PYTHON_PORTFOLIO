sum = 0
count = 0
# input
for c in range (1,7):
    num = int(input(f"Input the {c}º value: "))
    if num%2==0:
        sum = sum + num
    count +=1

# processing
print(f"You stated {count} numbers and the sum of the even numbers is {sum}.")

input()