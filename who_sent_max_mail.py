fname = raw_input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print 'File cannot be opened:', fname
    exit()
counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) == 0 or words[0] != 'From':
        continue
    k = words[1]
    #print k
    for word in k:
        counts[word] = counts.get(word,0) + 1
print counts

