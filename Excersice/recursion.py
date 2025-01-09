# Snippet 1
# Factorial
def F(n):
    if n == 0 or n == 1:
        return 1
    return n * F(n - 1)

result = F(5)
print(result)
    
# Snippet 2
# Count the occurence of vowels in a string
def fun(s):
    v = "aeiouAEIOU"
    if len(s) == 0:
        return 0
    return (1 if s[0] in v else 0) + fun(s[1:])

data = fun("aeroplane")
print(data)

# Snippet 3
# Sum of the digit of the number
def func(n):
    if n == 0:
        return 0
    return n % 10 + func(n // 10)
    
# Snippet 4
# Reverse the string
def func2(s):
    if len(s) == 0:
        return ""
    return s[-1] + func2(s[:-1])
    
