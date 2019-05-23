import json
import os.path

# Вспомогательная функция опредиляющая совпадают ли в "таблице" с лева от столбца i в строках j и k занчения всех ячеек
# Если проще то, есть ли с лева одинаковые ячейки во всех столбцах до i в строках j и k
def rightEquality(bd,i,j,k):
    for id in range(i):
        if bd[j][id] != bd[k][id]:
            return False
    return True

def sort_dict(bd):
    answer = {}
    for key in bd:
        answer_sub = {}
        bdValues = list(bd[key].values())
        bdKeys = list(bd[key].keys())
        #Сортировка значений , ключи остаются прежними
        for i in range(len(bd[key]["firstline"])):
            for j in range(1,len(bdValues)-1):
                for k in range(1,len(bdValues)-1):
                    if (i>0):
                        if(bdValues[j][i]<bdValues[k][i] and j>k and rightEquality(bdValues,i,j,k)):
                            bdValues[j],bdValues[k] = bdValues[k], bdValues[j]
                    elif(i == 0):
                        if(bdValues[j][i]<bdValues[k][i]and j>k):
                            bdValues[j],bdValues[k] = bdValues[k], bdValues[j]
        for id in range(len(bdValues)):
            answer_sub.update([(bdKeys[id],bdValues[id])])
        answer.setdefault(key,answer_sub)
    return answer

def add(bd = None,bd_id = "student"):
    if (bd != None):
        answer = bd.copy()
        id = 1 if len(answer[ bd_id ])==1 else int(list(answer[ bd_id ].keys())[-1])+1
        answer[ bd_id ].update([( int(id), add_question( bd[bd_id]["firstline"] ) )])
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
        del(answer[bd_id][list(bd[bd_id].keys())[id]])
        print(">Удалил<")
        return answer

def change(bd = None,bd_id = "student",id = -1,what = "fioga"):
    if (bd != None):
        id = int(id)
        answer = bd.copy()
        # answer = sort_dict(answer,bd_id)
        if id == -1 or id>=len(bd[bd_id]):
            id = len(bd[bd_id])-1
            if len(bd[bd_id])==1:
                return bd
        answer[bd_id][list(answer[bd_id].keys())[id]] = what_change(bd[bd_id][ list(bd[bd_id].keys())[id] ],bd[bd_id]["firstline"],bd_id,what )
        return answer

def what_change(bd, bd_first, bd_id, what):
    answer = bd 
    what_bd = {0:"f",1:"i",2:"o",3:"g",4:"a"}
    for key_bd, val_bd in list(what_bd.items()):
        if val_bd in what:
            answer[key_bd] = input("Введите значение поля \""+str(bd_first[key_bd]).lower()+"\": ")
            if answer[key_bd] =="":
                answer[key_bd] = bd[key_bd]
    return answer 

def table_bd(bd,bd_id = "student"):
    if (len(bd[bd_id])==1):
        print(">>> База пустая <<<")
        return
    # bdsort_dict(bd,bd_id)
    max_len_first = [0]

    max_len_first[0] = int(len(str(len(bd))))
    for ell in bd[bd_id]["firstline"]:
        max_len_first.append(len(ell))

    max_len = max_len_first.copy()

    for vall in list(bd[bd_id].values() ):
        for id in range(1,len(max_len_first)):
            max_len[id] = len(vall[id-1]) if max_len[id]<len(vall[id-1]) else max_len[id]

    for id in range(len(bd[bd_id]["firstline"])+1):
        if id == 0:
            print("№"+" "*(max_len[id]), end = "| ")
        else:
            print(bd[bd_id]["firstline"][id-1]+" "*(max_len[id]-(max_len_first[id]-1)), end ="| ")
        if id == len(bd[bd_id]["firstline"]):
            print()
            break

    count = 0
    for vall in list(bd[bd_id].values() ):
        if count != 0:
            for id in range(len(vall)):
                if (id == 0):
                    print(count, " " * ( max_len[id] - len( str(count) ) ), end="| " )
                    print(vall[id], " " * ( max_len[id+1] - len( vall[id] ) ), end="| " )
                if(id != 0 and id != len(vall)):
                    print(vall[id], " " * ( max_len[id+1] - len( vall[id] ) ), end="| " )
            print()
        count += 1

def save(bd):
    bd_sort = sort_dict(bd).copy()
    nameJsonFile = "save.json"
    jsonStr = json.dumps(bd_sort, ensure_ascii=False)
    jsonFile = open(nameJsonFile,"w")
    jsonFile.writelines(jsonStr)
    jsonFile.close()

def load():
    nameJsonFile = "save.json"
    if(not os.path.exists(nameJsonFile)):
        zeroFile = open(nameJsonFile,"w")
        zeroFile.write('{ "student":{ "firstline":["ФАМИЛИЯ","ИМЯ","ОТЧЕСТВО","ГРУППА","ЛЕТ"] },"teacher":{"firstline":["ФАМИЛИЯ","ИМЯ","ОТЧЕСТВО","СВОЯ ГРУППА","ЛЕТ"] } }')
        zeroFile.close()
    jsonFile = open(nameJsonFile,"r")
    jsonStr = jsonFile.read()
    answer = json.loads(jsonStr)
    jsonFile.close()
    return answer

def rebase ():
    id = input("""Какую бызу использовать?(цифра):
    1)Student
    2)Teacher
    : """).lower()
    if (id in ["1","student"]):
        return "student"
    if (id in ["2","teacher"]):
        return "teacher"


# dict_s = {
#     "student":{
#         "firstline":["ФАМИЛИЯ","ИМЯ","ОТЧЕСТВО","ГРУППА","ЛЕТ"],
#         1:["Марковский","Игнат","Петрович","ССА 18-11-2","18"],
#         2:["Марковский","Слава","Петрович","ССА 18-11-2","18"],
#         3:["Марковский","Игнат","Петрович","ССА 18-11-2","18"],
#         4:["Марковский","Газинур","Петрович","ССА 18-11-2","18"]
#     },
#     "teacher":{"firstline":["ФАМИЛИЯ","ИМЯ","ОТЧЕСТВО","СВОЯ ГРУППА","ЛЕТ"]}
# }
# print(delete_by_name(dict_s,"student","Игнат",2))
# print(add(dict_s,"student"))

# print("add(Студент): ",add(dict_s,"student"))
# print("-"*30)
# print("sort_dict(): ",sort_dict(dict_s,"student"))
# print("-"*30)
# print("delete_by_id(1): ",delete_by_id(dict_s,"teacher",1))
# print("-"*30)
# print("delete_by_name(Игнат): ",delete_by_name(dict_s,"student","Игнат",2))
# print("-"*30)
# print("change(студент,2,FIOGA): ",change(dict_s,"student",2,"FIOGA"))
# print(dict_s)
# table_bd(dict_s)
# print(load())
# save(dict_s)
# dict_s = load()
# table_bd(dict_s)
# bd_id = rebase()
# table_bd(dict_s,bd_id)