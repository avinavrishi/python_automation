# Print even number  from 0 to 20
# for i in range (0,20,2):
#     print(i)

# #Reverse print
# my_str=input("Enter your string: ")
# print(my_str[::-1])

# # print vowels from the string
# my_str=input("Enter your string: ")
# vowels='aeiou'
# count=0
# for i in my_str:
#     if i in vowels:
#         print(i)
#         count+=1

# print(count)

# Prime number
# def prime_num(num):
#     count=0
#     for i in range (2,num+1):
#         if num%i==0:
#             count+=1
#     if count==1:
#         return 1
#     return 0

# num=int(input("Enter your number: "))
# res=prime_num(num)
# if res==1:
#     print("Number is prime number")
# else:
#     print("Number is not prime")    


# l1=[1,2,2,3,3,4,4,5,6,6]
# l2=list(set(l1))
# l3=[]

# for i in l2:
#     count=0
#     for x in l1:
#         if i==x :
#             count+=1
#     l3.append({"Number ":i,"Count":count})        

# print(l2)
# print(l3)        


'''Given an array of integers nums and an integer target, return indices of the two numbers such 
that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same
element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]'''

# def two_sum(my_list,target):
#     l2=[]
#     for i in range(0,len(my_list)):
#         if i+1==len(my_list):
#             break
#         elif (my_list[i]+my_list[i+1])==target:
#             return(i,i+1)

# my_list=[2,7,11,15]
# res=two_sum(my_list,9)
# print(res)


'''
Given an integer x, return true if x is a palindrome,and false otherwise.

Example 1:
Input: x = 121
Output: true

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. 
Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
# '''
# def palindrom(num):
#     reverserd_num=0
#     digit=0
#     while num>0:
#         digit=num%10
#         reverserd_num=reverserd_num*10+digit
#         num=num//10
#     return reverserd_num

# num=int(input("Enter your number: "))
# res=palindrom(num)
# if res==num:
#     print(f"{num} is a palindrom number")
# else:
#     print(f"{num} is not a palindrom number")    

'''
Roman to Integer

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''
# def roman_to_integer(roman_num):
#     roman_dict={'I': 1,
#                 'V': 5,
#                 'X': 10,
#                 'L': 50,
#                 'C': 100,
#                 'D': 500,
#                 'M': 1000}
#     total=0
#     i=0
#     int_num=0

#     while i<len(roman_num):
#         int_num=roman_dict[roman_num[i]]
#         if i+1<len(roman_num) and int_num < roman_dict[roman_num[i+1]]:
#              total+=roman_dict[roman_num[i+1]]-int_num
#              i+=2
#         else:
#              total+=int_num
#              i+=1
#     return total

# roman_num=input("Enter your roman number : ")
# int_num=roman_to_integer(roman_num)
# print(f"The integer value of {roman_num} is {int_num}\n")

'''
Merge Two Sorted Lists
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
'''     

def merging_two_sorted_list(list_1,list_2):

    my_list=list_1+list_2
    my_list.sort()
    print(my_list)

merging_two_sorted_list([1,2,4],[1,3,4])
