input_str = input()
a, b = map(int, input_str.split())

for i in range(2, 9, 2):
    for j in range(b, a-1, -1):
        print(f"{j} * {i} = {(i)*j} ", end="")
        if (j!=a) :
            print("/",end=" ")
    print()