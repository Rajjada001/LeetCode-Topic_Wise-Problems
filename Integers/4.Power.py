def power(x,n):
    if n == 0:
        return 1
    if n<0:
        return power(1/x, -n)
    
    temp = power(x, n//2)

    if n%2 == 0:
        return temp*temp
    else:
        return temp*temp*x



t = int(input("Test Cases:"))
for _ in range(t):
    x = int(input("Enter x:"))
    n = int(input("Enter n:"))

    print(power(x, n))
