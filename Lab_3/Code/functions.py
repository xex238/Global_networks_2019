from ftplib import FTP
import ftplib
import socket
#import easygui

# Немного об обработке исключений
# — Исключения socket.error и IOError вызваны соединением сокета

# — Исключение ftplib.error_reply: исключение возникает при получении от сервера неожиданного ответа.

# — Исключение ftplib.error_temp: исключение возникает, когда получен код ошибки, обозначающий временную ошибку
# (коды ответов в диапазоне 400-499).

# — Исключение ftplib.error_perm: исключение возникает, когда получен код ошибки, означающий постоянную ошибку
# (коды ответов в диапазоне 500-599).

# — Исключение ftplib.error_proto: исключение возникает, когда от сервера получен ответ, который не соответствует
# спецификациям ответа протокола передачи файлов, т. е. начинается с цифры в диапазоне 1-5.

class FTP_server:
    ftp_server = ''
    username = ''
    password = ''

    def __init__(self, ftp_server):
        self.ftp_server = ftp_server

        print("Connect anonymously? Y/N")

        answer = str(input())
        while((answer.lower() != 'y') and (answer.lower() != 'n')):
            print("Connect anonymously? Y/N")
            answer = str(input())

        #self.Check_connection_to_FTP_server()

        if(answer.lower() == 'n'):
            print("Enter username")
            self.username = str(input())
            print("Enter password")
            self.password = str(input())

        ftp = self.Autorization()
        self.Work_with_ftp_server(ftp)

    def Work_with_ftp_server(self, ftp):
        print()
        print("Вы успешно вошли на сервер!")
        self.Help()
        print()
        command = ""
        while(command != "exit"):
            print(">>", end = ' ')
            command = str(input())

            list_command = command.split(' ')

            if(command == "list"):
                data = ftp.retrlines('LIST')
                print(data)

            if(list_command[0] == "catalog"):
                try:
                    ftp.cwd(list_command[1])
                except(Exception):
                    print("Такой директории не существует")

            if(list_command[0] == "download"):
                try:
                    my_file = open(list_command[1], 'wb')
                    print(my_file)
                    ftp.retrbinary('RETR ' + list_command[1], my_file.write, 1024)
                    print("Загрузка успешно выполнена")
                except(Exception):
                    print("Такого файла не существует")

            if(list_command[0] == "load"):
                try:
                    path = easygui.fileopenbox(filetypes=["*.txt"])
                    my_file = open(path)
                    ftp.storlines('STOR ' + path, my_file)
                except(Exception):
                    print("Невозможно загрузить файл на сервер")

            if(command == "help"):
                self.Help()

            if(command == "exit"):
                ftp.quit()
                exit()
         
    # Вызов справки
    def Help(self):
        print("Для навигации по серверу пользуйтесь следующими командами:")
        print("   list - вывод всех текущих файлов в каталоге")
        print("   catalog <имя каталога> - навигация по каталогам")
        print("   download <имя файла> - загрузка файла на диск с сервера")
        print("   load <имя файла> - загрузка файла с диска на сервер")
        print("   help - вызов справки")
        print("   exit - завершение работы")

    # Подключение к FTP-серверу
    def Autorization(self):
        try:
            if((self.username == '') or (self.password == '')):
                print("Анонимный вход")
                ftp = FTP(self.ftp_server)
            else:
                print("Неанонимный вход")
                ftp = FTP(self.ftp_server, self.username, self.password)
            print(ftp.login())
            return ftp
        except(IOError, socket.error) as e:
            print("Ошибка IOError")
            print("Ошибка вызвана соединением сокета")
            exit()
        except(ftplib.error_reply) as e:
            print("Ошибка error_reply")
            print("Исключение возникает при получении от сервера неожиданного ответа")
            exit()
        except(ftplib.error_temp) as e:
            print("Ошибка error_temp")
            print("Исключение возникает, когда получен код ошибки, обозначающий временную ошибку")
            print("Вероятно, время ожидания ответа от сервера истекло")
            exit()
        except(ftplib.error_perm) as e:
            print("Ошибка error_perm")
            print("Данное исключение возникает, когда от сервера получен ответ, который не соответствует спецификациям ответа протокола передачи файлов")
            print("Возможно, данный сервер предоставляет только анонимное подключение или вы ввели неверный логин и/или пароль")
            exit()
        except(ftplib.error_proto) as e:
            print("Ошибка error_proto")
            print("Исключение возникает, когда от сервера получен ответ, который не соответствует спецификациям ответа протокола передачи файлов")
            exit()
        except(Exception) as e:
            print(e.strerror)
            exit()

    # Подключаемся к серверу на заданный порт
    def Set_port_autorization(ftp_server):
        try:
            ftp = FTP()
            PORT = 9090
            ftp.connect(ftp_server, PORT)
        except(IOError, socket.error) as e:
            print("Ошибка IOError")
            print("Ошибка вызвана соединением сокета")
        except(ftplib.error_reply) as e:
            print("Ошибка error_reply")
            print("Исключение возникает при получении от сервера неожиданного ответа")
        except(ftplib.error_temp) as e:
            print("Ошибка error_temp")
            print("Исключение возникает, когда получен код ошибки, обозначающий временную ошибку")
            print("Вероятно, время ожидания ответа от сервера истекло")
        except(ftplib.error_perm) as e:
            print("Ошибка error_perm")
            print("Данное исключение возникает, когда от сервера получен ответ, который не соответствует спецификациям ответа протокола передачи файлов")
            print("Возможно, данный сервер предоставляет только анонимное подключение или вы ввели неверный логин и/или пароль")
        except(ftplib.error_proto) as e:
            print("Ошибка error_proto")
            print("Исключение возникает, когда от сервера получен ответ, который не соответствует спецификациям ответа протокола передачи файлов")
        except(Exception) as e:
            print(e.strerror)

    # Получаем спосок файлов в каталоге
    def Catalog_navigation(ftp_server):
        try:
            ftp = FTP(ftp_server)
            ftp.login()

            data = ftp.retrlines('LIST')
 
            print(data)
        except(IOError, socket.error) as e:
            print("Ошибка IOError")
            print("Ошибка вызвана соединением сокета")
        except(ftplib.error_reply) as e:
            print("Ошибка error_reply")
            print("Исключение возникает при получении от сервера неожиданного ответа")
        except(ftplib.error_temp) as e:
            print("Ошибка error_temp")
            print("Исключение возникает, когда получен код ошибки, обозначающий временную ошибку")
            print("Вероятно, время ожидания ответа от сервера истекло")
        except(ftplib.error_perm) as e:
            print("Ошибка error_perm")
            print("Данное исключение возникает, когда от сервера получен ответ, который не соответствует спецификациям ответа протокола передачи файлов")
            print("Возможно, данный сервер предоставляет только анонимное подключение или вы ввели неверный логин и/или пароль")
        except(ftplib.error_proto) as e:
            print("Ошибка error_proto")
            print("Исключение возникает, когда от сервера получен ответ, который не соответствует спецификациям ответа протокола передачи файлов")
        except(Exception) as e:
            print(e.strerror)

    # Меняем директорию и выводим список файлов
    def Change_directory(ftp_server, catalog):
        try:
            ftp = FTP(ftp_server)
            ftp.login()
 
            # Меняем директорию
            ftp.cwd(catalog)
 
            data = ftp.retrlines('LIST')
            print(data)
        except(IOError, socket.error) as e:
            print("Ошибка IOError")
            print("Ошибка вызвана соединением сокета")
        except(ftplib.error_reply) as e:
            print("Ошибка error_reply")
            print("Исключение возникает при получении от сервера неожиданного ответа")
        except(ftplib.error_temp) as e:
            print("Ошибка error_temp")
            print("Исключение возникает, когда получен код ошибки, обозначающий временную ошибку")
            print("Вероятно, время ожидания ответа от сервера истекло")
        except(ftplib.error_perm) as e:
            print("Ошибка error_perm")
            print("Данное исключение возникает, когда от сервера получен ответ, который не соответствует спецификациям ответа протокола передачи файлов")
            print("Возможно, данный сервер предоставляет только анонимное подключение или вы ввели неверный логин и/или пароль")
        except(ftplib.error_proto) as e:
            print("Ошибка error_proto")
            print("Исключение возникает, когда от сервера получен ответ, который не соответствует спецификациям ответа протокола передачи файлов")
        except(Exception) as e:
            print(e.strerror)

    # Загрузка (скачивание) файлов через FTP (out - путь на нашем компьютере где сохранить файл)
    def Load_file(ftp_server, catalog, out = 'xex.txt'):
        try:
            ftp = FTP(ftp_server)
            ftp.login()
 
            ftp.cwd(catalog) # Меняем папку
 
            my_file = open(out, 'wb')
            print(my_file)
            ftp.retrbinary('RETR ' + out, my_file.write, 1024)
        except(IOError, socket.error) as e:
            print("Ошибка IOError")
            print("Ошибка вызвана соединением сокета")
        except(ftplib.error_reply) as e:
            print("Ошибка error_reply")
            print("Исключение возникает при получении от сервера неожиданного ответа")
        except(ftplib.error_temp) as e:
            print("Ошибка error_temp")
            print("Исключение возникает, когда получен код ошибки, обозначающий временную ошибку")
            print("Вероятно, время ожидания ответа от сервера истекло")
        except(ftplib.error_perm) as e:
            print("Ошибка error_perm")
            print("Данное исключение возникает, когда от сервера получен ответ, который не соответствует спецификациям ответа протокола передачи файлов")
            print("Возможно, данный сервер предоставляет только анонимное подключение или вы ввели неверный логин и/или пароль")
        except(ftplib.error_proto) as e:
            print("Ошибка error_proto")
            print("Исключение возникает, когда от сервера получен ответ, который не соответствует спецификациям ответа протокола передачи файлов")
        except(Exception) as e:
            print(e.strerror)

    # Загрузка (скачивание) всех файлов через FTP
    def Load_all_files():
        try:
            ftp = FTP('ftp.debian.org')
            ftp.login()
            ftp.cwd('debian')
            filenames = ftp.nlst() # Получаем список названий файлов и каталогов
 
            # Создание путей для сохранения
            for filename in filenames:
                host_file = os.path.join('C:\\Users\\Дмитрий\\Desktop\\Учебники\\7 семестр\\Глобальные сети\\Лабораторная работа №3\\Download_files', filename)
    
                try:
                    with open(host_file, 'wb') as local_file:
                        ftp.retrbinary('RETR ' + filename, local_file.write)
                except ftplib.error_perm:
                    pass
 
            ftp.quit() # Завершить FTP-соединение

        except(ftplib.error_reply):
            print("Ошибка error_reply")
            print("Исключение возникает при получении от сервера неожиданного ответа")
        except(ftplib.error_temp):
            print("Ошибка error_temp")
            print("Исключение возникает, когда получен код ошибки, обозначающий временную ошибку")
            print("Вероятно, время ожидания ответа от сервера истекло")
        except(ftplib.error_perm):
            print("Ошибка error_perm")
            print("Данное исключение возникает, когда от сервера получен ответ, который не соответствует спецификациям ответа протокола передачи файлов")
            print("Возможно, данный сервер предоставляет только анонимное подключение или вы ввели неверный логин и/или пароль")
        except(ftplib.error_proto):
            print("Ошибка error_proto")
            print("Исключение возникает, когда от сервера получен ответ, который не соответствует спецификациям ответа протокола передачи файлов")

    #####
    # Методы загрузки файлов на сервер
    def Load_file_at_server(ftp_obj, path, ftype = 'TXT'):
        """
        Функция для загрузки файлов на FTP-сервер
        @param ftp_obj: Объект протокола передачи файлов
        @param path: Путь к файлу для загрузки
        """
        if ftype == 'TXT':
            my_file = open(path)
            ftp.storlines('STOR ' + path, my_file)
            #with open(path) as fobj:
            #    ftp.storlines('STOR ' + path, fobj)
        else:
            my_file = open(path, 'rb')
            ftp.storlines('STOR ' + path, my_file, 1024)
            with open(path, 'rb') as fobj:
                ftp.storbinary('STOR ' + path, fobj, 1024)

    # Реализация загрузки файлов на сервер
    def Load_some_files_at_server(ftp):
        ftp.login()
    
        path = '/path/to/something.txt'
        Load_file_at_server(ftp, path)
 
        pdf_path = '/path/to/something.pdf'
        Load_file_at_server(ftp, pdf_path, ftype='PDF')
    
        ftp.quit()

    # Анонимная загрузка файлов на сервер (не должна работать)
    def Load_some_files_at_server_anonymos(server_name):
        try:
            ftp = FTP(server_name)
            Load_some_files_at_server(ftp)
        except(IOError, socket.error) as e:
            print("Ошибка IOError")
            print("Ошибка вызвана соединением сокета")
        except(ftplib.error_reply) as e:
            print("Ошибка error_reply")
            print("Исключение возникает при получении от сервера неожиданного ответа")
        except(ftplib.error_temp) as e:
            print("Ошибка error_temp")
            print("Исключение возникает, когда получен код ошибки, обозначающий временную ошибку")
            print("Вероятно, время ожидания ответа от сервера истекло")
        except(ftplib.error_perm) as e:
            print("Ошибка error_perm")
            print("Данное исключение возникает, когда от сервера получен ответ, который не соответствует спецификациям ответа протокола передачи файлов")
            print("Возможно, данный сервер предоставляет только анонимное подключение или вы ввели неверный логин и/или пароль")
        except(ftplib.error_proto) as e:
            print("Ошибка error_proto")
            print("Исключение возникает, когда от сервера получен ответ, который не соответствует спецификациям ответа протокола передачи файлов")
        except(Exception) as e:
            print(e.strerror)

    # Загрузка файлов на сервер от лица пользователя
    def Load_some_files_at_server_user(server_name, username, password):
        try:
            ftp = FTP(server_name, username, password)
            Load_some_files_at_server(ftp)
        except(IOError, socket.error) as e:
            print("Ошибка IOError")
            print("Ошибка вызвана соединением сокета")
        except(ftplib.error_reply) as e:
            print("Ошибка error_reply")
            print("Исключение возникает при получении от сервера неожиданного ответа")
        except(ftplib.error_temp) as e:
            print("Ошибка error_temp")
            print("Исключение возникает, когда получен код ошибки, обозначающий временную ошибку")
            print("Вероятно, время ожидания ответа от сервера истекло")
        except(ftplib.error_perm) as e:
            print("Ошибка error_perm")
            print("Данное исключение возникает, когда от сервера получен ответ, который не соответствует спецификациям ответа протокола передачи файлов")
            print("Возможно, данный сервер предоставляет только анонимное подключение или вы ввели неверный логин и/или пароль")
        except(ftplib.error_proto) as e:
            print("Ошибка error_proto")
            print("Исключение возникает, когда от сервера получен ответ, который не соответствует спецификациям ответа протокола передачи файлов")
        except(Exception) as e:
            print(e.strerror)