
from lib.TableVOS import *
from lib.infoVOS import *
# from Table_VOS import *
    
   


# bd_student = load()

# add(bd,bd_id,id) - Добавляет/bd - база/bd_id - ид базы которая используется(поумалочанию = 1)/id - место вставки элемента,все оставльные сдвигаются, по умолчанию в конец
# delete(bd,id) - Удаление/bd - база/id - удаляемый элемент, по умолчанию, последний
# change(bd,what,id) - Изменение элементов/bd - база/what - что изменять,{F -Фамилия,I -Имя,O -Отчество,G -Группа,A -Возвраст}, по умолчанию перезаписывает полностью/id - изменяемый элемент, по умолчанию последний
# table_student(bd) - Выводит содержимое на экран в таблице
visionOS = "VladOS"
print("-"*25)
print(visionOS,"- все права защищены ©")
print("-"*25)
valid = True
# print(bd_student + "1")
bd_id = rebase()
bd = load()
print(bd)
while(1):
    if(valid):
        req = input(bd_id+" : ").lower()
    if (req =="help"):
        print("  addbd -> режим добавления студентов в список")
        print("  del -> режим удаления студентов из списка")
        print("  change -> режим коректировки значения(-ий) элемента списка")
        print("  look -> просмотр содержимого базы")
        print("  rebase -> переключение между базами")
        print("  version -> информация об операционной системе")
        print("  save -> сохранение базы данных")
    if (req =="addbd"):
        while(1):
            req_adds = input(bd_id+" -> adder bd: ").lower()
            if(req_adds != ""):
                if (req_adds =="help"):
                    print("   add -l -> добавление в базу значения")
                    print("   del -> режим удаления студентов из списка")
                    print("   change -> режим коректировки значения(-ий) элемента списка")
                    print("   look -> просмотр содержимого базы")
                    print("   exit -> выход из режима")
                if (req_adds.split()[0] == "add" and req_adds.split()[1] =="-l"):
                        bd = add(bd,bd_id)
                if (req_adds == "look"):
                    table_bd(bd,bd_id)
                if (req_adds =="del" or req_adds == "change"):
                    valid = False
                    req = req_adds
                    break
                if(req_adds == "exit"):
                    valid = True
                    break
    if(req == "del"):
        while(1):
            req_del = input(bd_id+" -> delete: ").lower()
            if(req_del != ""):
                if (req_del =="help"):
                    print("   del -l <позиция> -> удаляет элемент по №, по умолчанию удаляет последний эллемент")
                    print("   change -> режим коректировки значения(-ий) элемента списка")
                    print("   addbd -> режим добавления элементов в базу")
                    print("   look -> просмотр содержимого базы")
                    print("   exit -> выход из режима")
                if (req_del.split()[0] == "del" and req_del.split()[1] =="-l"):
                    if( len(req_del.split()) == 3 and req_del.split()[2].isdigit()):    
                        bd = delete_by_id(bd,bd_id,int(req_del.split()[2]))
                    else:
                        bd = delete_by_id(bd,bd_id)
                if (req_del == "look"):
                    table_bd(bd,bd_id)
                if (req_del =="addbd" or req_del == "change"):
                    valid = False
                    req = req_del
                    break
                if(req_del == "exit"):
                    valid = True
                    break
    if (req == "change"):
        while(1):
            req_change = input(bd_id+" -> change: ").lower()
            if(req_change != ""):
                if (req_change =="help"):
                    print("   ch -all <объект> - перезаписывает элемент полностью")
                    print("   ch <ключ> <объект> - перезаписывает элемент по ключам(F -Фамилия,I -Имя,O -Отчество,G -Группа,A -Возвраст)")
                    print("   addbd - режим добавления элементов в базу")
                    print("   del - режим удаления элементов из базы")
                    print("   look - просмотр содержимого базы")
                    print("   exit - выход из режима")
                if (req_change.split()[0] == "ch" and req_change.split()[1] =="-all"):
                    if( len( req_change.split() ) == 3 and req_change.split()[2].isdigit() ):
                        bd = change( bd, bd_id, req_change.split()[2] )
                elif (req_change.split()[0] == "ch" and (req_change.split()[1].find("F") or req_change.split()[1].find("I") or req_change.split()[1].find("O") or req_change.split()[1].find("G") or req_change.split()[1].find("A"))):
                    bd = change(bd, bd_id,req_change.split()[2],req_change.split()[1] )
                if (req_change == "look"):
                    table_bd(bd,bd_id)
                if (req_change =="del" or req_change == "addbd"):
                    valid = False
                    req = req_change
                    break
                if(req_change == "exit"):
                    valid = True
                    break
    if (req == "look"):
        table_bd(bd,bd_id)
    if (req == "version"):
        version()
    if (req == "rebase"):
        bd_id = rebase()
    if (req == "save"):
        while(1):
            true_save = input("Вы хотите сохранить изменения в базе?(y-yes, n-no): ").lower()
            if(true_save == ""):
                continue
            if true_save[0] in ["y","д"] :
                save(bd)
                print("База сохранена")
                break
            if true_save[0] in ["n","н"] :
                print("...")
                break




