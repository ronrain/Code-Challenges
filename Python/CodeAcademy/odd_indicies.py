def odd_indicies(my_list):
  list = [] #create an empty list
  for index in range(1, my_list[index], 2): #for loop >>
    #range specifeis the start, end and step value.
    #starts ar index 1, ends at the length of the list, and jumps 2 places
    list.append(my_list[index])
    #retrieves the current odd index (my_list[index]) and appends it to the list
  return list
