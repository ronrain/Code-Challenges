if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

sum_not_three = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]

#[[i,j,k]] the expression that defines each element of the resulting list
#each for is its own loop
#ex: for i in range(x+1) means iterating over values of "i" from 0 to "x" inclusive. the +1 allows for the number inputed to be inclusive
# the if condition is what determines the list that is satisfied