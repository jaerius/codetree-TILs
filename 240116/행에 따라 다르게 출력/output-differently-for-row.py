n = int(input())
cnt = 1

for i in range(n):
    
    for j in range(n):
        if(i%2==0):
            print(cnt, end=" ")
            
            if(j<n-1):
                cnt = cnt+1
            else:
                cnt = cnt+2
        else:
            print(cnt, end=" ")
            if(j<n-1):
                cnt = cnt+2
            else:
                cnt = cnt+1
            
            
    print()