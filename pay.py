#Pay calculator-PY4E chap2
def yourpay(h,r):
    if h<=40:
        pay=hours*rate
    else:
        overtime=h-40
        pay=40*rate+overtime*rate*1.5
    return pay

hours=float(input('enter your working hours:'))
rate=float(input('enter your rate:'))
print('your pay is',yourpay(hours,rate))
