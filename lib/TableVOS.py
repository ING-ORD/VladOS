import json
import os.path

def add (bd = None,bd_id = 1,id = None):
    answer = []
    if(bd != None):
        if (id != None ):
            for i in range(len(bd)):
                if (i == int(id)):
                    answer.append(add_question(bd_id))
                answer.append(bd[i])
            return answer
        else:
            answer = bd
            answer.append(add_question(bd_id))
            return answer

def add_question (id = 1):
    answer_question = []
    
    if(id == 1):
        answer_question.append(input("Введите фамилию студента: "))
        answer_question.append(input("Введите имя студента: "))
        answer_question.append(input("Введите отчество студента: "))
        answer_question.append(input("Введите группу студента(н-р:КП 18-11-2): "))
        answer_question.append(input("Введите кол-во полных лет студенту: "))
    else:
        answer_question.append(input("Введите фамилию преподавателя: "))
        answer_question.append(input("Введите имя преподавателя: "))
        answer_question.append(input("Введите отчество преподавателя: "))
        answer_question.append(input("Введите курируемую группу(н-р:КП 18-11-2): "))
        answer_question.append(input("Введите кол-во полных лет преподавателю: "))
    return answer_question

def delete(bd = None,id = None):
    answer = []
    if(bd != None):
        if (id == None ):
            id = len(bd)-1
        for i in range(len(bd)):
            if (i != int(id)):
                answer.append(bd[i])
        return answer

def change(bd,what = "FIOGA",id = None):
    answer = bd
    if (id == None ):
        id = len(bd)-1
    id = int(id)
    answer[id] = what_change(answer[id],what)
    return answer

def what_change(bd, what,bd_id):
    answer = bd
    if(bd_id == 1):
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
    else:
        if "F" in what:
            answer[0] = input("Введите фамилию преподавателя: ")
        if "I" in what:
            answer[1] = input("Введите имя преподавателя: ")
        if "O" in what:
            answer[2] = input("Введите отчество преподавателя: ")
        if "G" in what:
            answer[3] = input("Введите группу преподавателя(н-р:КП 18-11-2): ")
        if "A" in what:
            answer[4] = input("Введите кол-во полных лет преподавателя: ")
    return answer 

def table_student(bd, id = 1):
    if (len(bd)==0):
        print(">>> База пустая <<<")
        return
    if(id == 1):
        max_len = [0,7,3,8,6,3]
    else:
        max_len = [0,7,3,8,11,3]


    for ell in bd:
        max_len[0] = int(len(str(len(bd))))
        for i in range(1,6):   
            max_len[i] = len(ell[i-1]) if max_len[i]<len(ell[i-1]) else max_len[i]

    count = 1 
    if(id == 1):
        print("№"+" "*(max_len[0]) + "| ФАМИЛИЯ"+" "*(max_len[1]-6)+"| ИМЯ"+" "*(max_len[2]-2)+"| ОТЧЕСТВО"+" "*(max_len[3]-7)+"| ГРУППА"+" "*(max_len[4]-5)+"| ЛЕТ"+" "*(max_len[5]-2)+"|")
    else:
        print("№"+" "*(max_len[0]) + "| ФАМИЛИЯ"+" "*(max_len[1]-6)+"| ИМЯ"+" "*(max_len[2]-2)+"| ОТЧЕСТВО"+" "*(max_len[3]-7)+"| СВОЯ ГРУППА"+" "*(max_len[4]-10)+"| ЛЕТ"+" "*(max_len[5]-2)+"|")
    
    for ell in bd:

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

def save(bd = [[]],id = 1):
    id-=1
    # count = 0
    nameJsonFile = "save.json"
    jsonStr = json.dumps(bd, ensure_ascii=False)
    jsonFile = open(nameJsonFile,"r")
    links = jsonFile.readlines()
    links[id] = jsonStr

    jsonFile = open(nameJsonFile,"w")
    jsonFile.writelines(links[0]+"\n"+links[1])
    # jsonFile.writelines(links)
    # for link in jsonFile:
    #     if id == count:
    #         jsonFile.write(jsonStr)
    #     else:
    #         jsonFile.write(link)
    #     count+=1
    jsonFile.close()

def load(id = 1):
    id-=1
    count = 0
    nameJsonFile = "save.json"
    if(not os.path.exists(nameJsonFile)):
        zeroFile = open(nameJsonFile,"w")
        zeroFile.write("[]\n[]")
        zeroFile.close()
        return []
    else:
        jsonFile = open(nameJsonFile,"r")
        for link in jsonFile:
            if count == id :
                answer = json.loads(link)
            count+=1
        jsonFile.close()
        return answer
def rebase ():
    return int(input("""Какую бызу использовать?(цифра):
    1)Student
    2)Teacher
    : """))