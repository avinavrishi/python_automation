# Snippet 1
def F(n):
    if n == 0 or n == 1:
        return 1
    return n * F(n - 1)
    
# Snippet 2
def fun(s):
    v = "aeiouAEIOU"
    if len(s) == 0:
        return 0
    return (1 if s[0] in v else 0) + fun(s[1:])
    
# Snippet 3
def func(n):
    if n == 0:
        return 0
    return n % 10 + func(n // 10)
    
# Snippet 4
def func2(s):
    if len(s) == 0:
        return ""
    return s[-1] + func2(s[:-1])
    
result = f(5)

print(result)