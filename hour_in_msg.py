name = raw_input("Enter file:")
if len(name) > 1 :
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    line = line.rstrip()
    words = line.split()
    if len(words) == 0 or words[0] != 'From':
        continue
    #counts[words[1]] = counts.get(words[1],0)+1
    tics = words[5].split(":")
    hour = tics[0]
    counts[hour] = counts.get(hour,0) + 1
lst = counts.items()
lst.sort()
for key ,val in lst :
    print key,val
        
    
