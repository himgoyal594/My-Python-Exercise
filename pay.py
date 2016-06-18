hours = int(raw_input('Enter no. of hrs:\n'))
if hours <= 40 :
    pay = 475.0
else :
    h = hours - 40;
    pay =475*1.5
print pay
