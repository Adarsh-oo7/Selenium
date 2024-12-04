z=int(input('''SELECT THE TASK FORM THE FOLLOWING
ENTER THE SELECT NUMBER TO BE SELCTE

1) TO FIND THE TYPE
2)TO FIND THE LENGTH OF STRING
3)TO CHANGE THE CAUSE OF THE CHARCTER
4)ADD TWO FLOATING NUMBERS
5)TO DATA TO BIO
6)day 2/07/2024
7)change the tuple elements
8)PRINT KEY VALUE PAIRS
9)list to tuple
10)which is larger
11)Print the count down
12)
'''))

if(z==1):
    a=input('enter the anything to find the type:-')
    print(type(a))
elif(z==2):
    print("length of string")
    b=input("enter the stirng")
    print(len(b))
elif(z==3):
    c=input("enter the word to change its cause  :-")
    print(c.swapcase())
elif(z==4):
    e=float(input('enter first number'))
    d=float(input('enter the second number'))
    g=d+e
    print(f'sum={g}')
elif(z==5):
    h=input("enter the name")
    i=input('enter your age')
    j=input('enter you place')
    print(f'my name is {h} age is {i} and place {j}')
    print('my name is %s age is %s and place %s'%(h,i,j))
    d="my name is {0} age is {1} amd place {2}"
    print(d.format(h,i,j))
elif(z==6):
    a = int(input('enter a number'))
    if a > 10:
        s = True
    else:
        s = False
    print(s)
elif(z==7):
    tu = ('one', 'two', 'three')
    print(tu)
    tu = list(tu)
    tu[1] = 'one'
    tu = tuple(tu)
    print(tu)
elif(z==8):
    di = {'one': '1', 'two': '2', 'three': '3'}
    for x in di:
        print(x)
    for x, y in di.items():
        print(x, y)

elif(z==9):
    li = ['apple', 'mango', 'orange']
    li = tuple(li)
    print(li)
elif(z==10):
    one = int(input('enter the first number'))
    two = int(input("enter the second number"))

    if one > two:
        print(f'{one} is larger')
    elif one < two:
        print(f'{one} is smaller')
    else:
        print(f'both are {one}  are equla')


elif(z==11):
    n = int(input("Enter the number"))

    while (n >= 0):
        print(n)
        n = n - 1



