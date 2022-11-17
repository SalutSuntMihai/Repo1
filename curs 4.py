# cicluri repetitive
# while
i = 1
while i < 4:
    print(i)
    i += 1

print('while - else')
# while - else
x = 10
y = 5
while x > 0 and y > 0:
    print(x + y)
    x -= 2
    y -= 1
else:
    print("valorile lui x si y sunt " + str(x) + str(y))

# while - break
print('break')
x = 10
while x > 0:
    print(x)
    if x == 4:
        break
    x -= 2
    y -= 1

# while - continue
print("continue")
y = 8
while y > 4:
    y -= 1
    if y == 6:
        continue
    print(y)

# for
print('for')
for i in range(4):
    print(i)
else:
    print(i)

print('for - in range')
for i in range(3, 10, 2):
    print(i)

# for each
print('for each')
logo = "apple"
for x in logo:
    print(x)

firme = ['kfc', 'mcdonalts', 'subway']
for x in firme:
    print(x)

dict = {
    "masina": "dacia",
    "casa": "mare"
}
for x in dict:
    print(x)

# for break continue
print('for - break')
dict = {
    "masina": "dacia",
    "casa": "mare"
}
for x in dict:
    if dict[x] == "mare":
        break
    print(x)

print('for - continue')
firme = ['kfc', 'mcdonalts', 'subway']
for x in firme:
    if x == 'mcdonalts':
        continue
    print(x)

# for - else
print('for - else')
logo = "apple"
for x in logo:
    print(x)
else:
    print('s-a parcurs stringul')