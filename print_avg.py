# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
total =  0
count = 0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    line = line.rstrip()
    atpos = line.find('X-DSPAM-Confidence:')
    count = count + 1
    host = line[atpos+19:]
    x = float(host)
    total = total + x
    total = float(total)
    count = float(count)
    avg = float(total/count)
print 'Average spam confidence:',avg
#print "Done"
