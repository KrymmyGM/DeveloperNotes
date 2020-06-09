import cPageFunc
while True:
    c = 1
    print("\nВы хотите создать файл? \n 1)Y \n 2)N ")
    anw = input("\nВведите ответ:")
    if anw == "1":
        print("\n1)Web\n2)Prog")
        create = input("\nВведите ответ:")

        if create == "1":
            DerictFirst = "Web"
            print("\n1)None\n2)Category")
            create = input("\nВведите ответ:")
            i = int(input("Сколько файлов:"))
            if create == "1":
                while c <= i:
                    fileName = input('\nВведите название файла:') #appoint file name
                    PageName = "webIndex"
                    DerictSecond = fileName
                    cPageFunc.cPage(fileName, PageName, DerictFirst, DerictSecond)
                    c+=1
            elif create == "2":
                while c <= i:
                    fileName = input('\nВведите название файла:') #appoint file name
                    PageName = input("Название страницы:")
                    DerictSecond = PageName
                    NameLink = input()
                    cPageFunc.cPageAdd(fileName, PageName, DerictFirst, DerictSecond, NameLink)
                    c+=1

        elif create == "2":
            DerictFirst = "Prog"
            print("\n1)None\n2)Category")
            create = input("\nВведите ответ:")
            i = int(input("Сколько файлов:"))
            if create == "1":
                while c <= i:
                    fileName  = input('\nВведите название файла:') #appoint file name
                    PageName = "progIndex"
                    DerictSecond = fileName
                    cPageFunc.cPage(fileName, PageName, DerictFirst, DerictSecond)
                    c+=1
            elif create == "2":
                while c <= i:
                    fileName = input('\nВведите название файла:') #appoint file name
                    PageName = input("Название страницы:")
                    DerictSecond = PageName
                    NameLink = input()
                    cPageFunc.cPageAdd(fileName, PageName, DerictFirst, DerictSecond, NameLink)
                    c+=1

    elif anw == "2":
        print("До свидания")
        break;
