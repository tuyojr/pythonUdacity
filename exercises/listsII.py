# write a function called middle that takes a list and returns 
# a new list that contains all but the first and last elements.

def middle(a_list):
    del a_list[0]
    del a_list[-1]
    return a_list

user_list = []
print('Input what you want included in the list. Type "done" when finished')

while True:
    elements = input('Enter what you want in your list: ')
    if elements == 'done':
        break
    else:
        user_list.append(elements)

print(middle(user_list))