import pickle

def version():
    print("VladOS - все права защищены ©")
    print("Версия 0.0.3af")

def help(helpStr):
    helpBD = {
        "add":"""add:\n    -l\t\tДобавляет в базу строку""",
        "ch":"ch:\n    -all <id>\tИзменение в базе, всех значений строки под номером id\n    <keys> <id>\tИзменение в базе значений строки под номером id по ключм: F-Фамилия,I-Имя,O-Отчество,G-Группа,A-Возвраст",
        "del":"del:\n    -l <id>\tУдаление элемента строки под номером id, по умолчанию удаляет последнюю строку",
        "look":"look:\t\tВыводит содержимое базы в виде таблицы",
        "rebase":"rebase:\t\tОсуществляет переход на другую базу",
        "save":"save:\t\tСохраняет содержимое всех баз данных в которые были внесены изменения",
        "version":"version:\tИнформация о релизе",
        "shutdown":"shutdown:\tЗавершение процесса"
    }
    tru = False
    if(helpStr != "help"):
        for key in helpBD.keys():
            if helpStr in key  :
                print(helpBD[key])
                tru = True
    else:
        for key in helpBD.keys():
            print(helpBD[key])
        tru = True
    if (not tru):
        print("данной команды не существует, попробуйте снова")


    # with open("../bin/help.bin","wb") as file:
    #     pickle.dump(helpStr, file)
    # file.close()
    # with open("../bin/help.bin","rb") as file:
    #     loadStr = pickle.load(file)
    #     print(file)
    # print(loadStr)
    # file.close()
# helpStr = input(": ")
# help(helpStr)
# help("add")
# help("del")
# help("look")
# help("rebase")
# help("save")