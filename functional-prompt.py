my_array = [7, [4, 1, 3], 8, 9, [4, 1]]


def flattener(my_list:list):
    new_list = [] #this will make this pure
    for element in my_list:
        #check if the index is type of list 
        if type(element) == list:
            new_list.extend(element) # basically merging arrays instead of inserting the array
        else:
            #assuming that it is not a list it will insert to the end of the new list
            new_list.append(element)
    return new_list



flatten_list = flattener(my_array)
print(flatten_list)