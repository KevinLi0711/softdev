def front_times(str, n):
    retval = ''
    if len(str) < 3 :
        while ( n > 0 ):
            retval = retval + str
            n = n-1
    else:
        while ( n > 0):
            retval = retval + str[:3]
            n = n -1
    return retval

print(front_times("chocolate" ,2))