input_str = input()
a, b = map(int, input_str.split())

n = int(4)

for j in range(1,10):
        for i in reversed(range(n)):
          if (a+2*i) <= b:  
            print(f"{a+2*i} * {j} = {(a+2*i)*j} ", end="")
            if (i>=1) :
                print("/",end=" ")

        print()