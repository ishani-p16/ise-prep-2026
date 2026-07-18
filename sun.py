fhand=open('romeo-full.txt')
for line in fhand:
    line=line.rstrip()
    if line.find('sun')==-1:
        continue
    print(line)