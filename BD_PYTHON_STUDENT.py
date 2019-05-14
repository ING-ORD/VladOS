def add (bd_arr = None,id = None):
    bd_answer_add = []
    answer = []
    if(bd_arr != None):
        if (id != None ):
            for i in range(len(bd_arr)):
                if (i == id):
                    answer.append(add_question())
                answer.append(bd_arr[i])
            return answer
        else:
            answer = bd_arr
            answer.append(add_question())
            return answer

def add_question ():
    answer_question = []
    answer_question.append(input("Введите фамилию студента: "))
    answer_question.append(input("Введите имя студента: "))
    answer_question.append(input("Введите отчество студента: "))
    answer_question.append(input("Введите группу студента(н-р:КП 18-11-2): "))
    answer_question.append(input("Введите кол-во полных лет студента: "))
    return answer_question

def delete(bd_arr = None,id = None):
    answer = []
    if(bd_arr != None):
        if (id == None ):
            id = len(bd_arr)
        for i in range(len(bd_arr)):
            if (i != id):
                answer.append(bd_arr[i])
        return answer

def change(bd_arr,what = "FIOGA",id = None):
    answer = bd_arr
    if (id == None ):
        id = len(bd_arr)-1
    answer[id] = what_change(answer[id],what)
    return answer

def what_change(bd_id, what):
    answer = bd_id
    if "F" in what:
        answer[0] = input("Введите фамилию студента: ")
    if "I" in what:
        answer[1] = input("Введите имя студента: ")
    if "O" in what:
        answer[2] = input("Введите отчество студента: ")
    if "G" in what:
        answer[3] = input("Введите группу студента(н-р:КП 18-11-2): ")
    if "A" in what:
        answer[4] = input("Введите кол-во полных лет студента: ")
    return answer 

def table_student(bd_arr):
    max_len = [0,0,0,0,0,0]
    for ell in bd_arr:
        max_len[0] = int(len(str(len(bd_arr))))
        for i in range(1,6):   
            max_len[i] = len(ell[i-1]) if max_len[i]<len(ell[i-1]) else max_len[i]
    for i in max_len:
        print(i,"|",end = " ")
    print()

    # max_firs_st = int(len(str(len(bd_arr))))

    count = 1 
    for ell in bd_arr:

        for i in range(6):
            if (i==0):
                if (max_len[i]%2==0 and len(ell[i])%2==0):  
                    print(" "*((max_len[i]-len(ell[i]))//2),count," "*((max_len[i]-len(ell[i]))//2), end="|" )
                    print(" "*((max_len[i+1]-len(ell[i]))//2),ell[i]," "*((max_len[i+1]-len(ell[i]))//2), end="|" )
                elif (max_len[i]%2!=0 and len(ell[i])%2==0):
                    print(" "*(((max_len[i]-len(ell[i]))//2)-1),count," "*(((max_len[i]-len(ell[i]))//2)+1), end="|" )
                    print(" "*(((max_len[i+1]-len(ell[i]))//2)-1),ell[i]," "*(((max_len[i+1]-len(ell[i]))//2)+1), end="|" )
                else:
                    print(" "*(((max_len[i]-len(ell[i]))//2)-1),count," "*((max_len[i]-len(ell[i]))//2), end="|" )
                    print(" "*(((max_len[i+1]-len(ell[i]))//2)-1),ell[i]," "*(((max_len[i+1]-len(ell[i]))//2)), end="|" )
            if (i!=0 and i !=5):
                if (max_len[i]%2==0 and len(ell[i])%2==0):  
                    print(" "*((max_len[i+1]-len(ell[i]))//2),ell[i]," "*((max_len[i+1]-len(ell[i]))//2), end="|" )
                else:
                    print(" "*(((max_len[i+1]-len(ell[i]))//2)-1),ell[i]," "*(((max_len[i+1]-len(ell[i]))//2)), end="|" ) 
            if (i==5):
                print()
             
        # print(" "*((max_len[0]-len(ell[0]) + len(ell[0])%2)//2),end = "|" )


        # print(" "*((max_len[1]-len(ell[1]))//2), end = " ")
        # print(ell[0], end = " ")
        # print(" "*((max_len[0]-len(ell[0]) + len(ell[1])%2)//2), end = "|")
        # print(" "*((max_len[1]-len(ell[1]))//2), end = " ")
        # print(ell[1], end = " ")
        # print(" "*((max_len[1]-len(ell[1]) + len(ell[2])%2)//2), end = "|")
        # print(" "*((max_len[2]-len(ell[2]))//2), end = " ")
        # print(ell[2], end = " ")
        # print(" "*((max_len[2]-len(ell[2]) + len(ell[3])%2)//2), end = "|")
        # print(" "*((max_len[3]-len(ell[3]))//2), end = " ")
        # print(ell[3], end = " ")
        # print(" "*((max_len[3]-len(ell[3]) + len(ell[4])%2)//2), end = "|")
        # print(" "*((max_len[4]-len(ell[4]))//2), end = " ")
        # print(ell[4], end = " ")
        # print(" "*((max_len[4]-len(ell[4]) + len(ell[4])%2)//2), end = "|\n")


        count += 1

    
   


bd_student = [
    ["Марковский","Игнат","Петрович","ССА 18-11-2","18"]
]

bd_student = [
    ['Марковский', 'Игнат', 'Петрович', 'ССА 18-11-2', '25'],
    ['привет', 'что', 'расскажешь', 'мне', 'нового'], 
    ['из', 'свое', 'удивительной', 'жизни', 'а'],
    ['Марковский', 'Игнат', 'Петрович', 'ССА 18-11-2', '25'],
    ['привет', 'что', 'расскажешь', 'мне', 'нового'], 
    ['из', 'свое', 'удивительной', 'жизни', 'а'],
    ['Марковский', 'Игнат', 'Петрович', 'ССА 18-11-2', '25'],
    ['привет', 'что', 'расскажешь', 'мне', 'нового'], 
    ['из', 'свое', 'удивительной', 'жизни', 'а'],
    ['Марковский', 'Игнат', 'Петрович', 'ССА 18-11-2', '25'],
    ['привет', 'что', 'расскажешь', 'мне', 'нового'], 
    ['из', 'свое', 'удивительной', 'жизни', 'а']
]
# add(bd,id) - Добавляет/bd - база/id - место вставки элемента,все оставльные сдвигаются, по умолчанию в конец
# delete(bd,id) - Удаление/bd - база/id - удаляемый элемент, по умолчанию, последний
# change(bd,what,id) - Изменение элементов/bd - база/what - что изменять,{F -Фамилия,I -Имя,O -Отчество,G -Группа,A -Возвраст}, по умолчанию перезаписывает полностью/id - изменяемый элемент, по умолчанию последний

print("-"*25)
print("VladOS v0.0.1 - все права защищены ©")
print("-"*25)

# for i in range(2):
#     bd_student = add(bd_student)
# print(change(bd_student,"A",0))
table_student(bd_student)





