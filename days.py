f = open('mbox-short.txt')
for line in f:
    line = line.rstrip()
    if not line.startswith("from"):
        continue
    word = line.split()
    print word[2]
