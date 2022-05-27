number = int(input('Enter a number: '))
binary = []
while number > 0:
    binary.append(number%2)
    number=number//2
binary.reverse()
for i in range(len(binary)):
    print(binary[i], end='')
