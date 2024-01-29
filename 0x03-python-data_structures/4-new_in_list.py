#!/usr/bin/python3
def new_in_list(my_list, idx, element):
<<<<<<< HEAD
    if idx < 0 or idx >= len(my_list):
         return my_list
    else:
        new_list = my_list
        new_list[idx] = element
        return new_list
=======
    if 0 <= idx < len(my_list):
        new_list = my_list[:]
        new_list[idx] = element
        return new_list
    else:
        return my_list

>>>>>>> dbbedb6bd943bda6c6d41bd1160872f88f1c418f
