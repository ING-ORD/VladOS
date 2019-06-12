
from lib.TableVOS import *
from lib.infoVOS import *
import sys


print("-"*25)
print("VladOS- все права защищены ©")
print("-"*25)
bd_id = rebase()
bd = load()
while(1):
    req = input("~/"+bd_id+" : ").lower()
    #help
    if (len(req.split())== 2 and req.split()[0] == "help"):
        help(req.split()[1])
    elif (req == "help"):
        help(req)
    #add
    elif (len(req.split())==2 and req.split()[0] == "add" and req.split()[1] =="-l"):
            bd = add(bd,bd_id)
    #del
    elif (len(req.split())>=2 and req.split()[0] == "del" and req.split()[1] =="-l"):
        if( len(req.split()) == 3 and req.split()[2].isdigit()):    
            bd = delete_by_id(bd,bd_id,int(req.split()[2]))
        else:
            bd = delete_by_id(bd,bd_id)
    #ch
    elif (len(req.split())==3 and req.split()[0] == "ch" and req.split()[1] =="-all"):
        if( req.split()[2].isdigit() ):
            bd = change( bd, bd_id, req.split()[2] )
        else:
            print(req.split()[2]+" - не является коректным id, необходимо ввеси число")
    elif (len(req.split())==3 and req.split()[0] == "ch" and (req.split()[1].find("f") or req.split()[1].find("i") or req.split()[1].find("o") or req.split()[1].find("g") or req.split()[1].find("a"))):
        if( req.split()[2].isdigit() ):
            bd = change(bd, bd_id,req.split()[2],req.split()[1] )
        else:
            print(req.split()[2]+" - не является коректным id, необходимо ввеси число")
    #look
    elif (req == "look"):
        table_bd(bd,bd_id)
    #version
    elif (req == "version"):
        version()
    #rebase
    elif (req == "rebase"):
        bd_id = rebase()
    #save
    elif (req == "save"):
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
    #shutdown
    elif (req == "shutdown"):
        while(1):
            shutdown = input("Сохранить изменения пред выходом?(y-yes, n-no, c-cancel): ")
            if (shutdown == ""):
                continue
            if shutdown in ["y","д"]:
                save(bd)
                print("Saving...")
                print("Good")
                print("Всего доброго")
                sys.exit()
            if shutdown in ["n","н"]:
                print("Всего доброго")
                sys.exit()
            if shutdown in ["c","о"]:
                break
    elif (req == "history"):
        checkhistory()
    elif (req == "clear"):
        clear()
    else:
        print("Не коректный ввод команды...")
    checkhistory(req)



