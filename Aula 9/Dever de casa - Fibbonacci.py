x = 0
y = 1


for i in range(2):
    if i == 0:
        print(x) 
    else:
        print(y)  


conta = 2  

while conta < 10:
    z = x + y
    print(z)
    x = y
    y = z
    conta += 1