#1
pay=float(input('enter your pay: '))

taxes=pay*0.1

finalpay=pay-taxes

print(f'===== calculating your pay =====')
print(f'your pay: {pay} \n taxes: {taxes} \n finalpay: {finalpay}')


#2
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Addition:", num1 + num2, type(num1 + num2))
print("Subtraction:", num1 - num2, type(num1 - num2))
print("Multiplication:", num1 * num2, type(num1 * num2))
print("Division:", num1 / num2, type(num1 / num2))