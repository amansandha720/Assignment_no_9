#importing statistics
import statistics
# Creating a list 

list1 = []
n = int(input('Enter the no of elements: '))
for i in range(0,n):
    element = int(input('Enter the elements: '))
    list1.append(element)
print('Original list is: ',list1)

# Calculating mean

def my_mean(sample):
    result = sum(sample)/len(sample)
    print('Mean result: ',result)
my_mean(list1)

# Calculating median
def my_median(sample1):
    if n%2==0:
        res = (sample1[n//2-1] + sample1[n//2])/2
    else:
        res = (sample1[n//2])
    print('Median result is: ',res)
list1.sort()
print('Sorted list is:',list1)
my_median(list1)

# Calculating Mode
def my_mode(sample3):
    res = statistics.mode(sample3)
    print('Mode result is:',res)
list1.sort()
print('Sorted list for calculating mode: ',list1)
my_mode(list1)

#Calculating variance

def my_variance(sample4):
    res = statistics.variance(sample4)
    print('Variance result is: ',res)
list1.sort()
print('Sorted list for variance: ',list1)
my_variance(list1)

#Calculating standard deviation

def my_std(sample5):
    res = statistics.stdev(sample5)
    print('result for standard deviation is:',res)
list1.sort()
print('sorted list for std: ',list1)
my_std(list1)
