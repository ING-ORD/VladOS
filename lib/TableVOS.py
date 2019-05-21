import json
import os.path

# Вспомогательная функция опредиляющая совпадают ли в "таблице" с лева от столбца i в строках j и k занчения всех ячеек
# Если проще то, есть ли с лева одинаковые ячейки во всех столбцах до i в строках j и k
def rightEquality(bd,i,j,k):
    for id in range(i):
        if bd[j][id] != bd[k][id]:
            return False
    return True

def sort_dict(bd,bd_id):
    bdValues = list(bd[bd_id].values())
    bdKeys = list(bd[bd_id].keys())
    #Сортировка значений , ключи остаются прежними
    for i in range(len(bd[bd_id]["firstline"])):
        for j in range(1,len(bdValues)-1):
            for k in range(1,len(bdValues)-1):
                if (i>0):
                    if(bdValues[j][i]<bdValues[k][i] and j>k and rightEquality(bdValues,i,j,k)):
                        bdValues[j],bdValues[k] = bdValues[k], bdValues[j]
                elif(i == 0):
                    if(bdValues[j][i]<bdValues[k][i]and j>k):
                        bdValues[j],bdValues[k] = bdValues[k], bdValues[j]
    newDict = {}
    answer = {}
    # создание отсортировонного словаря для одной базы
    for id in range(len(bdValues)):
        newDict.update([(bdKeys[id],bdValues[id])])
    for id in list(bd.keys()):
        if id == bd_id:
            answer.update([(bd_id,newDict)])
        else:
            answer.update([(id,bd[id])])
    return answer

def add(bd = None,bd_id = "student"):
    if (bd != None):
        answer = bd.copy()
        id = 1 if len(answer[ bd_id ])==1 else list(answer[ bd_id ].keys())[-1]+1
        answer[ bd_id ].update([( id, add_question( bd[bd_id]["firstline"] ) )])
        return answer

def add_question (bd):
    answer = []
    for id in range(len(bd)):
        answer.append(input("Введите значение поля \""+str(bd[id]).lower()+"\": " ))
    return answer

def delete_by_name (bd = None,bd_id = "student",name = None,quantity = -1):
    if (bd != None):
        if quantity == -1 or quantity>=len(bd[bd_id]):
            quantity = len(bd[bd_id])-1
        count_del = 0
        answer = bd.copy()
        for key,ell in list(bd[bd_id].items()):
            if ell[1].lower() == name.lower() and key != "firstline" and quantity > count_del:
                answer["student"].pop(key,"lol")
                count_del += 1
        return answer

def delete_by_id(bd,bd_id,id=-1):
    if (bd != None):
        if id == -1 or id>=len(bd[bd_id]):
            id = len(bd[bd_id])-1
            if len(bd[bd_id])==1:
                return bd
        answer = bd.copy()
        del(answer[bd_id][id])
        return answer

def change(bd = None,bd_id = "student",id = -1,what = "FIOGA"):
    if (bd != None):
        answer = bd.copy()
        answer = sort_dict(answer,bd_id)
        if id == -1 and id>=len(bd[bd_id]):
            id = len(bd[bd_id])-1
            if len(bd[bd_id])==1:
                return bd
        answer[bd_id][list(answer[bd_id].keys())[id]] = what_change(bd[bd_id][ list(bd[bd_id].keys())[id] ],bd[bd_id]["firstline"],bd_id,what )
        return answer

def what_change(bd, bd_first, bd_id, what):
    answer = bd 
    what_bd = {0:"F",1:"I",2:"O",3:"G",4:"A"}
    for key_bd, val_bd in list(what_bd.items()):
        if val_bd in what:
            answer[key_bd] = input("Введите значение поля \""+str(bd_first[key_bd]).lower()+"\": ")
            if answer[key_bd] =="":
                answer[key_bd] = bd[key_bd]
    return answer 

def table_student(bd,bd_id = "student"):
    if (len(bd)==0):
        print(">>> База пустая <<<")
        return

    max_len_first = [0]

    max_len_first[0] = int(len(str(len(bd))))
    for ell in bd[bd_id]["firstline"]:
        max_len_first.append(len(ell))

    max_len = max_len_first

    for key,vall in list(bd[bd_id].items()):
        for id in range(1,len(vall)):
            max_len[id] = len(vall[id-1]) if max_len[id]<len(vall[id-1]) else max_len[id]

    for id in range(len(bd[bd_id]["firstline"])):
        if id == 0:
            print("№"+" "*(max_len[0]), end = "| ")
        else:
            print(max_len_first[id]+" "*max_len[id]-(max_len_first[id]-1), end ="| ")
        if id == len(bd[bd_id]["firstline"]):
            break

    count = 1 
    ##Осталось доделать вот этот кусок кода под списки
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
    ##Вот этот

def save(bd):
    nameJsonFile = "save.json"
    jsonStr = json.dumps(bd, ensure_ascii=False)
    jsonFile = open(nameJsonFile,"w")
    jsonFile.writelines(jsonStr)
    jsonFile.close()

def load():
    count = 0
    nameJsonFile = "save.json"
    if(not os.path.exists(nameJsonFile)):
        zeroFile = open(nameJsonFile,"w")
        zeroFile.write('{ "student":{ "firstline":["ФАМИЛИЯ","ИМЯ","ОТЧЕСТВО","ГРУППА","ЛЕТ"] },"teacher":{"firstline":["ФАМИЛИЯ","ИМЯ","ОТЧЕСТВО","СВОЯ ГРУППА","ЛЕТ"] } }')
        zeroFile.close()
        return []
    else:
        jsonFile = open(nameJsonFile,"r")
        answer = json.loadline(link)
        jsonFile.close()
        return answer

def rebase ():
    id.lower() = input("""Какую бызу использовать?(цифра):
1)Student
2)Teacher
    : """))
    if (id in ["1","student"]):
        return "student"
    if (id in ["2","teacher"])


dict_s = {
    "student":{
        "firstline":["ФАМИЛИЯ","ИМЯ","ОТЧЕСТВО","ГРУППА","ЛЕТ"],
        1:["Марковский","Игнат","Петрович","ССА 18-11-2","18"],
        2:["Марковский","Слава","Петрович","ССА 18-11-2","18"],
        3:["Марковский","Игнат","Петрович","ССА 18-11-2","18"],
        4:["Марковский","Газинур","Петрович","ССА 18-11-2","18"]
    },
    "teacher":{"firstline":["ФАМИЛИЯ","ИМЯ","ОТЧЕСТВО","СВОЯ ГРУППА","ЛЕТ"]}
}
# print(delete_by_name(dict_s,"student","Игнат",2))
# print(add(dict_s,"student"))
print("add(Студент): ",add(dict_s,"student"))
print("-"*30)
print("sort_dict(): ",sort_dict(dict_s,"student"))
print("-"*30)
print("delete_by_id(1): ",delete_by_id(dict_s,"teacher",1))
print("-"*30)
print("delete_by_name(Игнат): ",delete_by_name(dict_s,"student","Игнат",2))
print("-"*30)
print("change(студент,2,FIOGA): ",change(dict_s,"student",2,"FIOGA"))
