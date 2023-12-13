print("Welcome to Kibo quiz game !")
print(
  'P.S: if your spelling is incorrect then it is considered as wrong answer')
score = 0
question_no = 0
playing = input('Do you want to play ? ').lower()
if playing == 'yes':
  question_no += 1
  ques = input(
    f'\n{question_no}. What is often seen as the smallest unit of memory? '
  ).lower()
  if ques == 'kilobyte':
    score += 1
    print('correct! you got 1 point')

  else:
    print('Incorrect!')
    print(f'current answer is --> kilobyte')

# ------1
  question_no += 1
  ques = input(f'\n{question_no}. what does GPU stand for? ').lower()

  if ques == 'graphics processing unit':
    score += 1
    print('correct! you got 1 point')

  else:
    print('Incorrect!')
    print(f'current answer is --> graphics processing unit')

# -----2
  question_no += 1
  ques = input(
    f'\n{question_no}. What year was the very first model of the iPhone released? '
  ).lower()

  if ques == '2007':
    score += 1
    print('correct! you got 1 point')

  else:
    print('Incorrect!')
    print(f'current answer is --> 2007')

# -----3
  question_no += 1
  ques = input(
    f'\n{question_no}. Who is often called the father of the computer? '
  ).lower()

  if ques == 'charles babbage':
    score += 1
    print('correct! you got 1 point')

  else:
    print('Incorrect!')
    print(f'current answer is --> Charles Babbage')

# -----4
  question_no += 1
  ques = input(
    f'\n{question_no}. What is the name of the open-source operating system created by Linus Torvalds? '
  ).lower()

  if ques == 'linux':
    score += 1
    print('correct! you got 1 point')

  else:
    print('Incorrect!')
    print(f'current answer is --> Linux')

# ------5
  question_no += 1
  ques = input(
    f'\n{question_no}. What part of the atom has no electric charge?').lower()

  if ques == 'neutron':
    score += 1
    print('correct! you got 1 point')

  else:
    print('Incorrect!')
    print(f'current answer is --> Neutron')

# ------6

else:
  print('thank you, you are out of this game.')
  quit()

print(f'\nnumber of question is {question_no}')
print(f'your score is {score}')
try:
  percentage = (score * 100) / question_no
except ZeroDivisionError:
  print('0% quetions are correct')

print(f'{percentage}% questions are correct.')
