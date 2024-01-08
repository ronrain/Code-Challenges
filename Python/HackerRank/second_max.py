if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
second_max = list(set(arr)) #removes duplicates from the list
second_max.sort() #sorts them in ascending order
print(second_max[-2]) #identifies the second to last number in the list as the second highest number