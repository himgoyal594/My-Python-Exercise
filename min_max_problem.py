largest = None
smallest = None
while True:
    num = raw_input("Enter a number ")
    if num == "done" :
        break
    try :
        num1 = int(num)
    except :
        print 'Invalid input'
        
        #print num
    if largest is None or num1 >= largest :
        largest = num1
        #print 'Loop:', num, largest
    if smallest is None or num1 <= smallest :
        smallest = num1
        #print 'Loop:', num, largest
print 'Maximum', largest
print 'Minimum', smallest
