fhand = open('sc.txt')
count = 0;
for line in fhand:
    if line.startswith('From:') :
        count = count +1
        print line
print 'count:',count
