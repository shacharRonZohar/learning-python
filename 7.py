num1 = int(input('First num: '))
num2 = int(input('Second num: '))
num3 = int(input('Third num: '))

op = "="
if (num1 + num2 != num3):
    op = "!="

formatted_string = "{num1} + {num2} {op} {num3}".format(
    num1=num1,num2=num2,num3=num3,op=op
)
print(formatted_string)
