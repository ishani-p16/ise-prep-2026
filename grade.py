score=int(input("Enter a score(0-100):"))
if score>100:
    print("NOT POSSIBLE")
elif score>=97:
    print("A+ GRADE")
elif score>=90:
    print("A GRADE")
elif score>=80:
    print("B GRADE")
elif score>=70:
    print("C GRADE")
elif score >=60:
    print("D GRADE")
elif 0<=score<60:
    print("FAIL")
else:
    print("NOT POSSIBLE")

