
def num_to_digit(num):
    digits = []
    while num > 0:
     digit = num % 10
     digits.append(digit)
     num //= 10
    return(digits) 



multi_input=input("Enter your equation: ")
print(multi_input)
my_list=[]
my_list1=[]
digits = []
for i in range(2,7):
    if multi_input[i]=="=":
        pass
    else:
        my_list.append(multi_input[i])
given_list=list(map(int, my_list))

for i in range(10,20):
    res=2*i

    res_digit=num_to_digit(res)
    i_digit=num_to_digit(i)

    merg_list=i_digit+res_digit
    
    if sorted(merg_list)==sorted(given_list):
        print(f"The correct equation is{2}*{i}={res} ")
    else:
        pass    
    # print(i_digit+res_digit)
   
   