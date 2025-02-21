# James Aho
# 2/20/2025
# Module 3 Programming Assignment - Lists and Functions. This program answers the questions for this assignment. 

# 7.4 ===================

things = ["mozzarella", "cinderella", "salmonella"]

# 7.5 ===================

things[1] = things[1].capitalize()
print(things)
# No, it did not change the element in the list, it simply modified what was there.

# 7.6 ===================

things[0] = things[0].upper()
print(things)

# 7.7 ===================

del things[2]
print(things)

# 9.1 ===================

def good():
    list = ['Harry', 'Ron', 'Hermione']
    return list

# 9.2 ===================

def get_odds():
    list = []
    for i in range(10):
        if i % 2 != 0:
            list.append(i)
    return list
    
list = get_odds()
iteration = 1
for i in list:
    if iteration == 3:
        print(i)
    iteration += 1

