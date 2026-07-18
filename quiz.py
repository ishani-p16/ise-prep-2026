#Quiz about the human body
print('Welcome to this small quiz about the human body')
print('Each correct answers will be awarded 3 marks and 1 mark will be deducted for a wrong answer')
print('you have 5 questions to answer')
print('ALL THE BESTT!!!')
score=0
question=[['Which is the longest bone in our body?:','femur'],['Which organ can regenerate itself like a lizard tail?:','liver'],['Which bone is the only one not connected to another bone?:','hyoid bone'],['What is the hardest substance in the human body?:','enamel'],['What is the name of the acid found in the stomach?:','hydrochloric acid']]
for q in question:
    answer=input(q[0]+'')
    if answer.lower()==q[1]:
      print('YAY CORRECT!!')
      score=score+3
    else:
      print('Sorry the answer is:',q[1])
      score=score-1
print('Score:',score)
if score<=6:
   print('Seems like you know nothing about the human body...time to read your biology text')
elif 6<score<12:
   print('Not bad darlingg')
else:
   print('Damn girll slayyy')