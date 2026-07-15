names=['ish','vish','ish','nish','rish','vish']
count={}
for name in names:
    count[name]=count.get(name,0)+1
print(count)