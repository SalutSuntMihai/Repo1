#operatori de atribuire
x = 10
x += 5 #x=x+5
x -= 7 #x=x-7
x *= 2 #x=x*2
x /= 3 #x=x/2
x %= 4 #x=x%4
x //= 2 #x=x//2

#operatori aritmetici
x = 5
y = 2
z = x % y
print(z)

#operatori de comparare
x == y #egal
x != y #diferit
x > y #mai mare
x < y #mai mic
x >= y #mai mare sau egal
x <= y #mai mic sau egal

#operatori logici
x and y #si
x or y #ori
not x #negatie

#if statement
a = 20
b = 30
if (b + a) == 50 and b > a:
    print("succes")

#if else statement
a = 20
b = 30
if (b + a) < 50 and b > a:
    print("succes")
else:
    print("mai incearca")

#if elseif stament
a = 5
b = 9
if b > a:
    print("succes2")
elif b == a:
    print("aici e bine")
elif a < b:
    c = a+b
    print (type(c))
else:
    print("iesire")

#if else in oneline
print(a) if a>b else print (b)
print(a) if a>b else print ("aici") if b>a else print (b)

#nested if
if a == b:
    if a+b == 15:
        print ("succes3")
    else:
        print ("iesire1")
else:
    print ("iesire2")

#pass statement
if a>b:
    pass
elif b==a:
    print (a)
else:
    print(b)




