# Create a function called middle_element that has one parameter named my_list.

# If there are an odd number of elements in my_list, the function should return the middle element. If there are an even number of elements, the function should return the average of the middle two elements.


def middle_element(my_list):
  if len(my_list) % 2 == 0: #used % to determine if the list had an even elements
    sum = my_list[int(len(my_list)/2)] + my_list[int(len(my_list)/2) - 1] #if it is even, calculates the sum of the middle 2 elemetns
    #len(my_list)/2 > calculates the index of the second middle element (using float=point division)
    #int(len(my_list)/2) > converts the floating-point index to an integer, which is used to access the second middle elelment
    #int(len(my_list)/2)-1 > calculates the index of the forst middle element, which is one position before the second middle element
    #int(len(my_list)/2) and int(len(my_list)/2)-1 > access the 2 middle positions and calculate their sum
    return sum / 2 # retuens the avaerg
  else:
    return my_list[int(len(my_list)/2)] #if it is odd, returns the single middle element. It calculates the index of the middle element and retrieves it fromt the list