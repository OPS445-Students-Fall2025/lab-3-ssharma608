#!/usr/bin/env python3

# Create the list called "my_list" here, not within any function defined below.
my_list = [ 100, 200, 300, 'six hundred' ]


# That makes it a global object. We'll talk about that in another lab.


def give_list():
    # Does not accept any arguments
    # Returns all of items in the global object my_list unchanged
    mylist = (my_list[0:])
    return mylist

def give_first_item():
    # Does not accept any arguments
    # Returns the first item in the global object my_list as a string
    f_item = str(my_list[0])
    return f_item

def give_first_and_last_item():
    # Does not accept any arguments
    # Returns a list that includes the first and last items in the global object my_list
    fi_li = [my_list[0], my_list[-1]]
    return fi_li

def give_second_and_third_item():
    # Does not accept any arguments
    # Returns a list that includes the second and third items in the global object my_list
    si_ti = [my_list[1], my_list[2]]
    return si_ti

if __name__ == '__main__':   # This section also referred to as a "main block"
    print(give_list())
    print(give_first_item())
    print(give_first_and_last_item())
    print(give_second_and_third_item())
