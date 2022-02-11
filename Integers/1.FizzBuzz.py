def fizzBuzz(n):
    '''
        answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
        answer[i] == "Fizz" if i is divisible by 3.
        answer[i] == "Buzz" if i is divisible by 5.
        answer[i] == i (as a string) if none of the above conditions are true.
    '''
    res = []
    for i in range(1, n+1):
        if i%3==0 or i%5==0:
            if i%3==0 and i%5 !=0:
                res.append("Fizz")
            elif i%5==0 and i %3 !=0:
                res.append("Buzz")
            
            elif i%3==0 and i%5==0:
                res.append("FizzBuzz")
        else:
            res.append(str(i))
            
    return res


