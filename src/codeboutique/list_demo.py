numbers = []

while True:
    number = input("enter a #, q to quit: ")
    if number == "q":
        break
    numbers.append(int(number))

for number in numbers:
    print(number)

print(sum(numbers))

print(len(numbers))

if 9 in numbers:
    print("yes")
else:
    print("no")

names = ["a", "b"]
