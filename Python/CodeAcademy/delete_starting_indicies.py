def delete_starting_indicies(my_list):
  while len(my_list) > 0 and my_list[0] % 2 == 0: #while loop that ONLY MEETS the length of the list AND what numbers are even, when it is odd it stops
    my_list = my_list[1:0]#if conditons are met, we replace the list with every element except for the first one 
  return my_list