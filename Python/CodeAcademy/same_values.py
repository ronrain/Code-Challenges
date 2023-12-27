def same_values(lst1, lst2):
  list = [] # create a new list
  for index in range(len(lst1)): #iterate through the indicies of one of the lists; ensures we go through each pair of elements in the list
    if lst1[index] == lst2[index]:# checks if theyre equal the list indicies are equal to eachother
      list.append(index) #if they are equal it appends to the new list
  return list