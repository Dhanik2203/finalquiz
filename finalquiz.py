print('Hello,Welcome to Quiz:')
ans=input('You Want to play (yes/no):')
score=0
total_q=4
if ans.lower() == 'yes':
    ans=input('1.What is Best Programming language: Option are:1:python,2:java')
    if ans.lower() =='1':
        score +=1
        print('correct Answer')
    else:
        print('incorrect Answer')

    ans = input('2.Who is india Prime Minister:Option are:1:narendra Modi,2:Rahul Gandhi ')
    if ans.lower()== '1':
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

    ans = input('4.which Year corona virus war introduce: Option are:1:2019,2:2020')
    if ans == '2':
        score += 1
        print('correct Answer')
    else:
        print('incorrect Answer')

    print('Thank for playing this game , You got',score,"question correct")
    mark=(score/total_q) * 100
    print("mark",mark)
    print("All Questions Answer is:1=python,2=narendra modi,3=12,4=2020 ")

print("good bye")

