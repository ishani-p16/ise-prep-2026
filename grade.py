def grades(score):
   if score>=97:
      return 'A+'
   elif score>=90:
      return 'A'
   elif score>=80:
      return 'B'
   elif score>=70:
      return 'C'
   elif score >=60:
      return 'D'
   elif 0<=score<60:
      return 'F'

Score=int(input("Enter a score(0-100):"))
print (grades(Score))