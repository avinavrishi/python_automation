
def num_to_digit(num):
    digits = []
    while num > 0:
     digit = num % 10
     digits.append(digit)
     num //= 10
    return(digits) 

multi_input=input("Enter your equation: ")
index_of_x = multi_input.index("x")
a = int(multi_input[:index_of_x])

# print(multi_input)
my_list=[]
my_list1=[]
digits = []
for i in range(2,7):       
    if multi_input[i] != "=":
        my_list.append(int(multi_input[i]))

# given_list=list(map(int, my_list))

for i in range(10,20):
    res=a*i

    res_digit=num_to_digit(res)
    i_digit=num_to_digit(i)

    merg_list=i_digit+res_digit
    
    if sorted(merg_list)==sorted(my_list):
        print(f"The correct equation is {a}*{i}={res} ")
    else:
        pass    
    # print(i_digit+res_digit)
   
   
# 2x14=22

# Additional Test Cases
# Swap in C
# Swap between A and B
# Swap between A and C