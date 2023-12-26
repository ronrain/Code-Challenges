def exponents(bases, powers):
  list = [] #create an empty list
  for base in bases: #outer loop
    for power in powers: #nested loop
      list.append(base ** power)#adding the answerr to the new list
  return list


#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))