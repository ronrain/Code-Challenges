def reversed_list(lst1, lst2):
  for index in range(len(lst1)):#loops through indicies of lst1
    #goes from 0 to the length, have to add the -1 to match index number
    if lst1[index] != lst2[len(lst2) - 1 - index]: # checks if the element at the current index is not equal to the aleemnt at the corresponding position when counting to the end of lst2. lst2[len(lst2) - 1 - index] retrieves the element from lst2 at the position that iw ould correspond in reverse order
      return False
  return True


def reversed_list(lst1, lst2):
    reversed_lst1 = lst1.copy()  # Create a copy of lst1 to avoid modifying it in-place
    reversed_lst1.reverse()  # Reverse the copy

    if reversed_lst1 == lst2:
        return True
    else:
        return False
