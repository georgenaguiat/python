for x in range(0, 151):
    print(x)
    
for x in range(5, 1001, 5):
    print(x)

for int in range(0, 101):
    if int % 10 == 0:
        print("Coding Dojo")
    elif int % 5 == 0:
        print("Coding")
    else:
        print(int)

count = 0
for i in range(1, 500001, 2):
    count += i
print(count)

for count_down in range(2018, 1, -4):
    print(count_down)

lowNum = 7
highNum = 10
mult = 5

for i in range(lowNum, highNum +1):
    if i % mult == 0:
        print(i)
