import cPageFunc
while True:
    c = 1
    print("\nВы хотите создать файл? \n 1)Y \n 2)N ")
    anw = input("\nВведите ответ:")
    if anw == "y":
        print("\n1)Web\n2)Prog")
        create = input("\nВведите ответ:")

        if create == "1":
            DerictFirst = "Web"
            print("\n1)None\n2)Html\n3)JS")
            create = input("\nВведите ответ:")
            i = int(input("Сколько файлов:"))
            if create == "1":
                while c <= i:
                    fileName = input('\nВведите название файла:') #appoint file name
                    PageName = "webIndex"
                    cPageFunc.cPage(fileName, PageName, DerictFirst)
                    c+=1
            elif create == "2":
                while c <= i:
                    fileName = input('\nВведите название файла:') #appoint file name
                    DerictSecond = "HTML"
                    PageName = "html"
                    NameLink = input()
                    cPageFunc.cPageAdd(fileName, PageName, DerictFirst, DerictSecond, NameLink)
                    c+=1
            elif create == "3":
                while c <= i:
                    fileName = input('\nВведите название файла:') #appoint file name
                    DerictSecond = "JS"
                    PageName = "js"
                    NameLink = input()
                    cPageFunc.cPageAdd(fileName, PageName, DerictFirst, DerictSecond, NameLink)
                    c+=1

        elif create == "2":
            DerictFirst = "Prog"
            print("\n1)None\n2)Python")
            create = input("\nВведите ответ:")
            i = int(input("Сколько файлов:"))
            if create == "1":
                while c <= i:
                    fileName  = input('\nВведите название файла:') #appoint file name
                    PageName = "progIndex"
                    cPageFunc.cPage(fileName, PageName, DerictFirst)
                    c+=1
            elif create == "2":
                while c <= i:
                    fileName = input('\nВведите название файла:') #appoint file name
                    DerictSecond = "Python"
                    PageName = "python"
                    NameLink = input("Название страницы:")
                    cPageFunc.cPageAdd(fileName, PageName, DerictFirst, DerictSecond, NameLink)
                    c+=1

    elif anw == "n":
        print("До свидания")
        break;
