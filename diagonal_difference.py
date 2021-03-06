''' 
input : array 
output : number
algorithim:
1- calculate length of outer array
2- once as length is known 
 a- loop through each array and get the value of an index incrementing by 1 for array
 b- calculate total
 c- do opposite for second loop
3- subtract and get absolute value
'''
def diagnol(big_arr):
    x = len(big_arr) - 1
    i = 0
    totalright = 0
    totalleft = 0
    for row in big_arr:
        totalleft += row[i]
        i += 1
    for row in big_arr:
        totalright += row[x]
        x -= 1
    return abs(totalleft - totalright)
    