#hrs = raw_input("Enter Hours:")
#h = float(hrs)
#rate = raw_input("Enter Rate:")
#r = float(rate)

def computepay(h,r):
    if h > 40 :
        pay = 10.50 * 40 + (10.50 * 1.5)*(h - 40)
        return pay
    else :
        pay = h * 10.50
        return pay

pays = computepay(45,10.50)
print pays
    
