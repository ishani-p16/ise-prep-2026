#WHETHER THE ENTERED NUMBER IS VALID OR NOT
NUM=input('Enter a number:')
try:
    num=int(NUM)
except:
    num=-1

if num>0:
    print('NICE WORK')
else:
    print('NOT A NUMBER')