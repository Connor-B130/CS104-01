scoreCount = 0
numberOfTests = int(input("Please enter the number of tests you want to average: "))
total = 0
while scoreCount < numberOfTests:
 score = int(input("Please enter a score: "))
 scoreCount += 1
 total = total + score
average = total/scoreCount
print("The average is ",average) 