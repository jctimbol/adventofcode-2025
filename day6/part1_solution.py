with open('day6/input.txt', 'r') as file:
    lines = [file.readline().split() for _ in range(5)]
    total = 0
    for i in range(len(lines[0])):
        num1 = lines[0][i]
        num2 = lines[1][i]
        num3 = lines[2][i]
        num4 = lines[3][i]
        operator = lines[4][i]
        equation = num1 + operator + num2 + operator + num3 + operator + num4
        total += eval(equation) 

print(total)
