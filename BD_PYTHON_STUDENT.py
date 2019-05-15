def add (bd_arr = None,id = None):
    answer = []
    if(bd_arr != None):
        if (id != None ):
            for i in range(len(bd_arr)):
                if (i == int(id)):
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
            if (i != int(id)):
                answer.append(bd_arr[i])
        return answer

def change(bd_arr,what = "FIOGA",id = None):
    answer = bd_arr
    if (id == None ):
        id = len(bd_arr)-1
    id = int(id)
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

    max_len = [0,7,3,8,6,3]

    for ell in bd_arr:
        max_len[0] = int(len(str(len(bd_arr))))
        for i in range(1,6):   
            max_len[i] = len(ell[i-1]) if max_len[i]<len(ell[i-1]) else max_len[i]
    # for i in max_len:
    #     print(i,"|",end = " ")
    # print()

    count = 1 
    print("№"+" "*(max_len[0]) + "| ФАМИЛИЯ"+" "*(max_len[1]-6)+"| ИМЯ"+" "*(max_len[2]-2)+"| ОТЧЕСТВО"+" "*(max_len[3]-7)+"| ГРУППА"+" "*(max_len[4]-5)+"| ЛЕТ"+" "*(max_len[5]-2)+"|")
    for ell in bd_arr:

        for i in range(6):
            if (i==0):
                if (max_len[i]%2==0 and len(ell[i])%2==0):  
                    print(count, " " * ( max_len[i] - len( str(count) ) ), end="| " )
                    print(ell[i], " " * ( max_len[i+1] - len( ell[i] ) ), end="| " )
                else:
                    print(count, " " * ( max_len[i] - len( ell[i] ) ), end="| " )
                    print(ell[i], " " * ( max_len[i+1] - len( ell[i] ) ), end="| " )
            if (i!=0 and i !=5):
                if (max_len[i]%2==0 and len(ell[i])%2==0):  
                    print(ell[i], " " * ( max_len[i+1] - len( ell[i] ) ), end="| " )
                elif (max_len[i]%2!=0 and len(ell[i])%2==0):
                    print(ell[i], " " * ( max_len[i+1] - len(ell[i] ) ), end="| " )
                else:
                    print(ell[i], " " * ( max_len[i+1] - len( ell[i] ) ), end="| " ) 
            if (i==5):
                print()
        count += 1

    
   


bd_student = [
    ["Марковский","Игнат","Петрович","ССА 18-11-2","18"]
]

bd_student = [
    ['Марковский', 'Игнат', 'Петрович', 'ССА 18-11-2', '25']
    
]
# add(bd,id) - Добавляет/bd - база/id - место вставки элемента,все оставльные сдвигаются, по умолчанию в конец
# delete(bd,id) - Удаление/bd - база/id - удаляемый элемент, по умолчанию, последний
# change(bd,what,id) - Изменение элементов/bd - база/what - что изменять,{F -Фамилия,I -Имя,O -Отчество,G -Группа,A -Возвраст}, по умолчанию перезаписывает полностью/id - изменяемый элемент, по умолчанию последний
# table_student(bd) - Выводит содержимое на экран в таблице

print("-"*25)
print("VladOS v0.0.1 - все права защищены ©")
print("-"*25)
valid = True
while(1):
    if(valid):
        req = input(":")
    if (req =="help"):
        print("adds - режим добавления студентов в список")
        print("del - режим удаления студентов из списка")
        print("change - режим коректировки элементов списка")
        print("look - просмотр содержимого списка")
    if (req =="adds"):
        while(1):
            req_adds = input("adder_student:")
            if (req_adds =="help"):
                print("add -l <позиция> - создание студента на заданной поззиции")
                print("del - режим удаления студентов из списка")
                print("change - режим коректировки элементов списка")
                print("look - просмотр содержимого списка")
            if (req_adds.split()[0] == "add" and req_adds.split()[1] =="-l"):
                bd_student = add(bd_student,req_adds.split()[2])
            if (req_adds == "look"):
                table_student(bd_student)
            if (req_adds =="del" or req_adds == "change"):
                valid = False
                req = req_adds
                break
    if(req == "del"):
        while(1):
            req_del = input("delete:")
            if (req_del =="help"):
                print("del -l <позиция> - удаляет элемент с позиции")
                print("change - режим коректировки элементов списка")
                print("adds - режим добавления студентов в список")
                print("look - просмотр содержимого списка")
            if (req_del.split()[0] == "del" and req_del.split()[1] =="-l"):
                bd_student = delete(bd_student,req_del.split()[2])
            if (req_del == "look"):
                table_student(bd_student)
            if (req_del =="adds" or req_del == "change"):
                valid = False
                req = req_del
                break
    if (req == "change"):
        while(1):
            req_change = input("change:")
            if (req_change =="help"):
                print("ch -all <объект> - перезаписывает элемент полностью")
                print("ch <ключи> <объект> - перезаписывает элемент по ключам(F -Фамилия,I -Имя,O -Отчество,G -Группа,A -Возвраст)")
                print("adds - режим добавления студентов в список")
                print("del - режим удаления студентов из списка")
                print("look - просмотр содержимого списка")
            if (req_change.split()[0] == "ch" and req_change.split()[1] =="-all"):
                bd_student = change(bd_student,"FIOGA", req_change.split()[2])
            elif (req_change.split()[0] == "ch" and (req_change.split()[1].find("F") or req_change.split()[1].find("I") or req_change.split()[1].find("O") or req_change.split()[1].find("G") or req_change.split()[1].find("A"))):
                bd_student = change(bd_student,req_change.split()[1], req_change.split()[2])
            if (req_change == "look"):
                table_student(bd_student)
            if (req_change =="del" or req_change == "adds"):
                valid = False
                req = req_change
                break
    if (req == "look"):
        table_student(bd_student)




