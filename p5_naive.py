i=20
while True:
    i = i+20
    print(i)
    divs = True
    for j in range(1,21):
        if i % j != 0:
            divs = False
    if divs == True:
        break

print(i)
