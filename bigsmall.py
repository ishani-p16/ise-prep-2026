number=[]
while True:
    entry=input('Number:')
    if entry=='done':
        break
    number.append(float(entry))
print('Largest:',max(number))
print('Smallest:',min(number))