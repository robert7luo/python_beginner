# The mean of a set of numbers is the sum of the numbers divided by the
# number of numbers. Write a procedure, list_mean, which takes a list of numbers
# as its input and return the mean of the numbers in the list.

# Hint: You will need to work out how to make your division into decimal
# division instead of integer division. You get decimal division if any of
# the numbers involved are decimals.



def list_mean(p):
    result=0
    n=len(p)
    for e in p:
        result=result+e
    i=0
    while result-n>=0:
        i=i+1
        result=result-n
    result=result*10
    j=0
    while result-n>=0:
        j=j+1
        result=result-n
    result=result*10
    k=0
    while result-n>=0:
        k=k+1
        result=result-n
    result=result*10
    l=0
    while result-n>=0:
        l=l+1
        result=result-n
    return i+j*0.1+k*0.01+l*0.001
        
    


print list_mean([1,2,3,4])
#>>> 2.5
print list_mean([1,3,4,5,2])
#>>> 3.0
#print list_mean([])
#>>> ??? You decide. If you decide it should give an error, comment
# out the print line above to prevent your code from being graded as
# incorrect.
print list_mean([2])
#>>> 2.0

print list_mean([2, 4, 5, 6, 7, 1, 1, 1])


#ERROR Incorrect. Your procedure did not return the correct mean 3.375 for input [2, 4, 5, 6, 7, 1, 1, 1]. Your submission passed 4 out of 6 test cases.???