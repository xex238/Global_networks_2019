import functions
import math

#bit_mas_1 = [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1]
#bit_mas_2 = [0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]

#print("bit_mas_1 = ")
#print(bit_mas_1)
#print()

##print("bit_mas_2 = ")
##print(bit_mas_2)
##print()

#length_hamming_word_input = 16
#length_hamming_word_output = length_hamming_word_input + math.floor(math.log(length_hamming_word_input, 2)) + 1

#print("length_hamming_word_output = ", length_hamming_word_output)

#hamming_mas_1 = functions.Hamming_code(bit_mas_1, 16)
#hamming_mas_2 = functions.Hamming_code(bit_mas_2, 16)

#ham_mas_1 = [1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1]
#ham_mas_1_copy = [1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1]

#print("Hamming_mas_1 = ")
#print(hamming_mas_1)
#print()

#print("len(hamming_mas_1) = ")
#print(len(hamming_mas_1))
#print()

#functions.Repeat_Hamming_code(ham_mas_1_copy, length_hamming_word_input)




## Работа с сокетами (серверное приложение)
#import socket

#sock = socket.socket()
#sock.bind(('', 9090))
#sock.listen(1)
#conn, addr = sock.accept()

#print ("connected:", addr)

#while True:
#    data = conn.recv(1024)
#    if not data:
#        break
#    conn.send(data.upper())

#conn.close()




#number = 553
#l = functions.dec_bin(number)
#functions.bin_dec(l)

def word(x):
    return x
    return x + 1

x1, x2 = word(10)
print("x1 = ", x1)
print("x2 = ", x2)

## Работа с сокетами (отправка данных)
#import socket

#sock = socket.socket()
##sock.connect(('127.0.0.1', 9090))
#sock.connect(('127.0.0.1', 49100))
##sock.send(Hamming_mas)
#l = [0, 1, 1, 0, 1]
#b1 = bytes(l)
#s = "!"
#b2 = bytes(s.encode('utf8'))
##sock.send(b2) # Работает
#sock.send(b1)

#data = sock.recv(1024)
#sock.close()

#print(data)





# Проверка данных без отправки сообщения

#if(bit_mas == bit_mas_new):
#    print("Раскодировка прошла успешно")
#else:
#    print("Всё плохо :с")

#    if(len(bit_mas) != len(bit_mas_new)):
#        print("Длина массивов разная")
#        print("len(bit_mas) = ", len(bit_mas))
#        print("len(new_bit_mas) = ", len(bit_mas_new))


#if(file_code_2 == file_code):
#    print("Урааа! Кодировки совпадают!")
#else:
#    print("Иэх.. Кодировки не совпадают :с")






#print("Количество правильно переданных слов -", count_of_true_words)
#print("Количество неправильно переданных слов -", count_of_false_words)
#print("Количество исправленных слов -", count_of_corrected_words)
#print("Количество неисправленных слов -", count_of_uncorrected_words)