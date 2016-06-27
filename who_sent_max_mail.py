name = raw_input("Enter file:")
if len(name) == 1 : name = "mbox-short.txt"
fhand = open(name)

counts = dict()
k=dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) == 0 or words[0] != 'From':
        continue
    counts[words[1]] = counts.get(words[1],0)+1
    
max_count =0;
email = None
for key,value in counts.items():
	if value>max_count:
		max_count = value
		email = key

print email,max_count
