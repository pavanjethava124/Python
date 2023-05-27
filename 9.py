n=10
n1=0
n2=1
i=0

print("Fibonacci sequence:")
while i<n:
    print(n1,end=" ")
    
    nth=n1+n2
    n1=n2
    n2=nth
    i+=1
