
from lib.TableVOS import *
# from Table_VOS import *
    
   


# bd_student = load()

# add(bd,bd_id,id) - Добавляет/bd - база/bd_id - ид базы которая используется(поумалочанию = 1)/id - место вставки элемента,все оставльные сдвигаются, по умолчанию в конец
# delete(bd,id) - Удаление/bd - база/id - удаляемый элемент, по умолчанию, последний
# change(bd,what,id) - Изменение элементов/bd - база/what - что изменять,{F -Фамилия,I -Имя,O -Отчество,G -Группа,A -Возвраст}, по умолчанию перезаписывает полностью/id - изменяемый элемент, по умолчанию последний
# table_student(bd) - Выводит содержимое на экран в таблице
visionOS = "VladOS v0.0.2"
print("-"*25)
print(visionOS,"- все права защищены ©")
print("-"*25)
valid = True
# print(bd_student + "1")
bd_id = int(input("""Какую бызу использовать?:
    1)Student
    2)Teacher
    : """))
bd = load(bd_id)

while(1):
    if(valid):
        req = input(visionOS+" : ")
    if (req =="help"):
        print(">> adds - режим добавления студентов в список")
        print(">> del - режим удаления студентов из списка")
        print(">> change - режим коректировки элементов списка")
        print(">> look - просмотр содержимого списка")
        print(">> save - сохранение базы данных")
    if (req =="adds"):
        while(1):
            req_adds = input(visionOS+" -> adder_student: ")
            if(req_adds != ""):
                if (req_adds =="help"):
                    print(">>> add -l <позиция> - создание студента на заданной поззиции")
                    print(">> del - режим удаления студентов из списка")
                    print(">> change - режим коректировки элементов списка")
                    print(">> look - просмотр содержимого списка")
                    print(">> exit - выход из режима")
                if (req_adds.split()[0] == "add" and req_adds.split()[1] =="-l"):
                    if(len(req_adds.split())==3):
                        bd = add(bd,bd_id,req_adds.split()[2])
                    else:
                        bd = add(bd,bd_id)
                if (req_adds == "look"):
                    table_student(bd)
                if (req_adds =="del" or req_adds == "change"):
                    valid = False
                    req = req_adds
                    break
                if(req_adds == "exit"):
                    valid = True
                    break
    if(req == "del"):
        while(1):
            req_del = input(visionOS+" -> delete: ")
            if(req_del != ""):
                if (req_del =="help"):
                    print(">>> del -l <позиция> - удаляет элемент с позиции")
                    print(">> change - режим коректировки элементов списка")
                    print(">> adds - режим добавления студентов в список")
                    print(">> look - просмотр содержимого списка")
                    print(">> exit - выход из режима")
                if (req_del.split()[0] == "del" and req_del.split()[1] =="-l"):
                    if( len(req_del.split()) == 3 ):    
                        bd = delete(bd,req_del.split()[2])
                    else:
                        bd = delete(bd)
                if (req_del == "look"):
                    table_student(bd)
                if (req_del =="adds" or req_del == "change"):
                    valid = False
                    req = req_del
                    break
                if(req_del == "exit"):
                    valid = True
                    break
    if (req == "change"):
        while(1):
            req_change = input(visionOS+" -> change: ")
            if(req_change != ""):
                if (req_change =="help"):
                    print(">>> ch -all <объект> - перезаписывает элемент полностью")
                    print(">>> ch <ключи> <объект> - перезаписывает элемент по ключам(F -Фамилия,I -Имя,O -Отчество,G -Группа,A -Возвраст)")
                    print(">> adds - режим добавления студентов в список")
                    print(">> del - режим удаления студентов из списка")
                    print(">> look - просмотр содержимого списка")
                    print(">> exit - выход из режима")
                if (req_change.split()[0] == "ch" and req_change.split()[1] =="-all"):
                    bd = change(bd,"FIOGA", req_change.split()[2])
                elif (req_change.split()[0] == "ch" and (req_change.split()[1].find("F") or req_change.split()[1].find("I") or req_change.split()[1].find("O") or req_change.split()[1].find("G") or req_change.split()[1].find("A"))):
                    bd = change(bd,req_change.split()[1], req_change.split()[2])
                if (req_change == "look"):
                    table_student(bd)
                if (req_change =="del" or req_change == "adds"):
                    valid = False
                    req = req_change
                    break
                if(req_change == "exit"):
                    valid = True
                    break
    if (req == "look"):
        table_student(bd,bd_id)
    if(req == "save"):
        while(1):
            true_save = input("Вы хотите сохранить изменения в базе?(y-yes, n-no): ")
            if(true_save == ""):
                continue
            if true_save[0] in ["y","Y","д","Д"] :
                save(bd,bd_id)
                print("База сохранена")
                break
            if true_save[0] in ["n","N","Н","н"] :
                print("Отменяю")
                break




