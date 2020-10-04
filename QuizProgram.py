#getting input from the user
regnum = input("enter your register number :")

mark = 0

stu_ans = []
#mark_list = {}
key_ans = []
#single line comment 
auth = open('student_list.txt')

auth_temp = auth.read()

if regnum in auth_temp:
    
    student_mark_list = open(regnum+'.txt','a')
        
    question = open('QuizQuestions.txt','r')
        
    print(question.read())
        
    question.close()
        
    
    key = open('key_answer.txt')
    k = key.readlines()
    print(k)
    for line1 in k:
        key_ans.append(line1.strip('\n'))
    
    for i in range(1,6):

        j = str(i)
        print('\nenter '+str(i)+' questions answer : ')
        
        getoption = input()

        stu_ans.append(getoption)
    
    #mark_list[regnum] = stu_ans
    mark = len(set(key_ans).intersection(set(stu_ans)))
        
    student_mark_list.write('Register No: '+regnum+'\n')
    
    for i in range(len(stu_ans)):
        temp = stu_ans[i]
        temp = str(temp)
        student_mark_list.write(temp+'\n')
        temp_mark = str(mark)
    student_mark_list.write('  ==> Total marks '+temp_mark+' in out of 5 marks\n')
#file opening
    print('\n  ==> Total marks '+temp_mark+' in out of 5 marks')

    f_m_list = open('stu_answers.txt','a')
    f_m_list.write('Register No: '+regnum+'\n')
    f_m_list.write('Total mark is '+temp_mark+'\n')
    f_m_list.write('------------------------------\n')
    f_m_list.close()

    student_mark_list.close()

    key.close()

auth.close()
