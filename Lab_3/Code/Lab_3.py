from ftplib import FTP
import functions

server_name = 'ftp.cse.buffalo.edu' # Только анонимное подключение

# Множество книг по математике и научных публикаций  
math_books_ftp_server = 'ftp.mccme.ru' # Подключение по логину

# огромное количество видео, в том числе HD. Фильмы, ТВ шоу, Формула 1
ftp_server_1 = 'ftp://91.122.30.115/'

# очень много музыки в формате mp3, фильмов и книг
ftp_server_2 = 'ftp://92.242.39.60/'

# Не существующий сервер
ftp_server_3 = 'ftp.my_good_server.ru'

# Множество дистрибутивов Linux
ftp_server_4 = 'ftp://mirror.yandex.ru/'

# Имя каталога для сервера "server_name"
catalog_1 = 'mirror'

# Список с директориями на сервере "server_name"
list_of_directory = ["mirror"]
#list_of_directory = ["mirror", "pub", "users"]

if __name__ == '__main__':
    my_ftp_server = functions.FTP_server(server_name)
    #my_ftp_server = functions.FTP_server(ftp_server_3)

    #functions.Standart_autorization()
    #functions.Set_port_autorization()
    #functions.Catalog_navigation()
    #functions.Change_directory()
    #functions.Load_file()
    #functions.Load_all_files()

    #functions.Load_some_files_at_server_anonymos(math_books_ftp_server) # Ошибка - нельзя подключаться анонимно
    #functions.Load_some_files_at_server_user(math_books_ftp_server, 'username', 'password') # Ошибка - неверный логин и/или пароль
    #functions.Load_some_files_at_server_anonymos(ftp_server_3)

    #functions.Check_connection_to_FTP_server(server_name, list_of_directory)

    #functions.Standart_autorization(server_name) # Подключение проходит
    #functions.Standart_autorization(ftp_server_4)
    #functions.Load_some_files_at_server_anonymos(ftp_server_4)