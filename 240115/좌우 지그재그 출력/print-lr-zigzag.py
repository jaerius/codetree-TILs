n = int(input())
cnt =1
for i in range(n):
    for j in range(n):
        if i%2 ==0 :
            print(cnt+j + i*n, end=" ")    
        else:
            print(cnt+(n-(j+1))+i*n, end=" ")
            
    print()