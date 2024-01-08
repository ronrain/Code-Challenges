from statistics import mean #to simplify using average, have to import from statistics to use the mean method

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
for name, scores in student_marks.items(): #iterate through key values and have the items displayed
    if name == query_name: #if the name is the same as the query_name
        average = mean(scores) #mean the scores
        print("%.2f" % average) #use this syntax for roounding to whatever decimal place you need