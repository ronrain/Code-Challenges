result = [] #will store student names and their scores
scorelist = [] #will store a list of all the scores

if __name__ == '__main__':
    for _ in range(int(input())): #initiates a loop that will iterate as many times as specified by the user
      name = input() #reads a string input
      score = float(input()) #reads a floating point number
      result += [[name, score]] #appends a list to the result list
      scorelist += [score] #appends a list to the scorelist
    b = sorted(list(set(scorelist)))[1] 
      #set() removes duplicates
      #list() converts unique scores back into a list
      #sorted() sorts unique characters into ascending order
      #[1] selects second number in list which is the second highest number
    
    for names, scores in sorted(result): #iterates through the pairs of student names and scores stored in the result list
      if scores == b: # if scores equals the number recieved above then print the name correlated to the scores
        print(names)