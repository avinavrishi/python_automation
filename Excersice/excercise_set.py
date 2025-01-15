'''1. Event Attendance Tracker
A company organized an event, and attendees are tracked across different sessions using sets. 
For example:
session1 = {"Alice", "Bob", "Charlie"}
session2 = {"Alice", "David", "Charlie"}
session3 = {"Alice", "Bob", "Eve"}
Write a function that:

Returns the set of people who attended all sessions.
Returns the set of people who attended at least one session.
Returns the set of people who attended only one session.'''

# def all_sessions(set_1,set_2,set_3):
#     set_4=set_1.intersection(set_2,set_3)
#     # set_5=set_4.intersection(set_3)
#     return set_4

# def at_least_one_session(set_1,set_2,set_3):
#     set_4=set_1.symmetric_difference(set_2)
#     set_5=set_2.symmetric_difference(set_3)
#     set_6=set_1.symmetric_difference(set_3)
#     set_7=set_4.intersection(set_5,set_6)
#     return set_7
    

# def only_one_session(set_1,set_2,set_3):
#     set_4=set_1.symmetric_difference(set_2)
#     print(set_4)
#     set_5=set_4.symmetric_difference(set_3)
#     return set_5

# session1 = {"Alice", "Bob", "Charlie"}
# session2 = {"Alice", "David", "Charlie"}
# session3 = {"Alice", "Bob", "Eve"}
# res_1=all_sessions(session1,session2,session3)
# print(res_1)
# res_2=at_least_one_session(session1,session2,session3)
# print(res_2)
# res_3=only_one_session(session1,session2,session3)
# print(res_3)


'''2. Exclusive Customer Rewards
A store has multiple categories of customers based on their purchases:

electronics = {"Alice", "Bob", "Charlie"}
groceries = {"Bob", "Charlie", "David"}
clothing = {"Alice", "Eve"}
Write a function that:

Returns the set of customers who purchased items from all three categories.
Returns the set of customers who purchased items from exactly two categories.
Returns the set of customers who purchased items from only one category.'''

# def items_from_all_three_categories(set_1,set_2,set_3):
#     set_4=set_1.intersection(set_2,set_3)
#     return set_4

# # def items_from_exactly_two_categories(set_1,set_2,set_3):
     
     

# def items_from_only_one_category(set_1,set_2,set_3):
#      set_4=set_1.symmetric_difference(set_2)
#      set_5=set_4.symmetric_difference(set_3)
#      return set_5

# electronics = {"Alice", "Bob", "Charlie"}
# groceries = {"Bob", "Charlie", "David"}
# clothing = {"Alice", "Eve","David"}

# res_1=items_from_all_three_categories(electronics,groceries,clothing)
# print(res_1)
# # res_2=items_from_exactly_two_categories(electronics,groceries,clothing)
# # print(res_2)
# res_3=items_from_only_one_category(electronics,groceries,clothing)
# print(res_3)

'''3. Shopping List and Inventory
A store's inventory is stored as a set:

inventory = {"Milk", "Eggs", "Bread", "Butter"}
A customer provides their shopping list as a list:

shopping_list = ["Eggs", "Bread", "Cheese"]
Write a function that:

Returns a list of items from the shopping list that are available in the inventory.
Returns a list of items from the shopping list that are not available.'''

# def item_available(inven,shop_list):
#     set_1=inven.intersection(shop_list)
#     return set_1

# def item_not_vailable(inven,shop_list):
#     set_02=set(shop_list)
#     set_1=set_02.difference(inven)
#     return set_1


# inventory = {"Milk", "Eggs", "Bread", "Butter"}
# shopping_list = ["Eggs", "Bread", "Cheese"]
# available_items_list=list(item_available(inventory,shopping_list))
# print(available_items_list)
# not_available_items_list=list(item_not_vailable(inventory,shopping_list))
# print(not_available_items_list)

'''4. Tourist Spot Popularity
A travel company tracks visits to tourist spots using a list of tuples, 
where each tuple contains a tourist's name and the list of places they visited:

tourists = [
    ("Alice", ["Beach", "Museum", "Park"]),
    ("Bob", ["Park", "Beach"]),
    ("Charlie", ["Museum", "Beach"])
]
Write a function that:

Returns a set of all unique places visited.
Returns a list of places visited by more than one tourist.'''

def all_places_visited(tourist):
    set_1=set()
    for tuples in tourist:
        for i in tuples[1]:
            set_1.add(i)
    return set_1

def list_of_places_visited_twice(tourists):

    places_visited = []
    unique_places = all_places_visited(tourists)   

    for places in unique_places:
        count = 0
        for data in tourists:
             if places in data[1]:
                count+=1
        if count > 1:
            places_visited.append(places)
    
    return places_visited

tourists = [("Alice", ["Beach", "Museum", "Park"]),
            ("Bob", ["Park", "Beach"]),
            ("Charlie", ["Museum", "Beach"])]

places_visited=all_places_visited(tourists)            
print(places_visited)

print(list_of_places_visited_twice(tourists))