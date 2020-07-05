print('Hello,Welcome to Quiz:')
ans=input('You Want to play (yes/no):')
score=0
total_q=6
if ans.lower() == 'yes':
    ans=input('1.What is Best Programming language: Option are: 1:python,2:java')
    if ans =='1':
        score +=1
        print('correct Answer')
    else:
        print('incorrect Answer')

    ans = input('2.The members of the Rajya Sabha are elected by: Option are: 1:Lok Sabha,2:elected members of the legislative assembly ')
    if ans == '2':
        score += 1
        print('correct Answer')
    else:
        print('incorrect Answer')

    ans = input('3.What is 3+6+3 ? : Option are:1:12,2:11')
    if ans == '1':
        score += 1
        print(' correct Answer')
    else:
        print('incorrect Answer')

    ans = input('4.The nucleus of an atom consists of?: Option are:1:protons and neutrons,2:electrons and protons ')
    if ans == '1':
        score += 1
        print('correct Answer')
    else:
        print('incorrect Answer')
    ans = input('5.On July 12, 1982, the ARDC was merged into?: Option are:1:RBI,2:NABARD ')
    if ans == '1':
        score += 1
        print('correct Answer')
    else:
        print('incorrect Answer')
    ans = input('6.20th August is celebrated as?: Option are:1:Sad Bhawan Divas,2:Army Day ')
    if ans == '1':
        score += 1
        print('correct Answer')
    else:
        print('incorrect Answer')

    print('Thank for playing this game , You got',score,"question correct")
    mark=(score/total_q) * 100
    print("mark",mark)
    print("All Questions Answer is:1=python,2=narendra modi,3=12,4=2020 ")

print("good bye")

