from chardet.universaldetector import UniversalDetector
import math
import copy

# Определение кодировки заданного файла
def get_encoding(path):
    detector = UniversalDetector()
    with open(path, 'rb') as fh:
        for line in fh:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
    if (detector.result == None):
        print("Неизвестная кодиковка. Невозможно открыть прочитать текст")
        exit()
    return detector.result

# Кодировка из массива с двоичным кодом в значения ascii
def get_ascii_code(bit_mas, word_length):
    code = []
    while(len(bit_mas) != 0):
        value = bit_mas[0:word_length]
        bit_mas = bit_mas[word_length:]
        s = ""
        for i in range(len(value)):
            s = s + str(value[i])
        code.append(int(s, base = 2))
    return code

# Перевод из значений ascii в текст
def get_text(code, word_length, encoding):
    text = ""
    for i in range(len(code)):
        #print(chr(code[i]))
        text = text + chr(code[i])
    #print(text)

    file_path = "my_file.txt"
    my_file = open(file_path, "w")
    my_file.write(text)
    my_file.close()

    new_encoding = get_encoding(file_path)
    
    #print("new_encoding = ")
    #print(new_encoding['encoding'])
    #print()

    return text

# Повторное вычисление кода Хемминга на принимающей стороне
def Repeat_Hamming_code(Hamming_mas, length_hamming_word_input):
    #bit_mas = []
    count_of_zero_errors = 0
    count_of_one_errors = 0
    count_of_two_errors = 0

    validation_hamming_mas = []
    Hamming_mas_copy = copy.deepcopy(Hamming_mas)

    length_hamming_word_output = length_hamming_word_input + math.floor(math.log(length_hamming_word_input, 2)) + 2
    
    count_of_iterations = math.ceil(len(Hamming_mas_copy) / length_hamming_word_output)

    for k in range(count_of_iterations):
        try:
            value_word = Hamming_mas_copy[0:length_hamming_word_output]
            Hamming_mas_copy = Hamming_mas_copy[length_hamming_word_output:]
        except:
            value_word = Hamming_mas_copy
            Hamming_mas_copy = []

        # Обнуление контрольных битов
        counter = 0
        value = 0
        control_bit = []

        # Проверка значений для контрольных групп
        counter = 0
        value = 2 ** counter
        while(value - 1 < len(value_word)):
            i = value - 1
            count_of_one = 0
            while(i < len(value_word)):
                for j in range(value):
                    if(value_word[i] == 1):
                        count_of_one = count_of_one + 1
                    i = i + 1
                    if(i >= len(value_word)):
                        break
                i = i + value
            control_bit.append(count_of_one % 2)
            counter = counter + 1
            value = 2 ** counter
        
        count_of_ones_in_value_word = 0

        for i in range(len(value_word)):
            if(value_word[i] == 1):
                count_of_ones_in_value_word = count_of_ones_in_value_word + 1

        count_of_ones = 0
        count_of_zeros = 0
        for i in range(len(control_bit)):
            if(control_bit[i] == 1):
                count_of_ones = count_of_ones + 1
            if(control_bit[i] == 0):
                count_of_zeros = count_of_zeros + 1

        print(count_of_zeros)
        print(count_of_ones)
        print(count_of_ones_in_value_word)

        if((count_of_ones_in_value_word % 2 == 0) and (count_of_ones == 0)):
            count_of_zero_errors = count_of_zero_errors + 1

            # Убираем контрольные биты
            value_word.pop()
            counter = math.floor(math.log(len(value_word), 2))
            value = (2 ** counter) - 1
            while(counter >= 0):
                value_word.pop(value)
                counter = counter - 1
                value = (2 ** counter) - 1

            for i in range(len(value_word)):
                validation_hamming_mas.append(value_word[i])
            continue
        elif((count_of_ones_in_value_word % 2 == 0) and (count_of_ones > 0)):
            count_of_two_errors = count_of_two_errors + 1

            # Убираем контрольные биты
            value_word.pop()
            counter = math.floor(math.log(len(value_word), 2))
            value = (2 ** counter) - 1
            while(counter >= 0):
                value_word.pop(value)
                counter = counter - 1
                value = (2 ** counter) - 1

            for i in range(len(value_word)):
                validation_hamming_mas.append(value_word[i])
            continue
        elif((count_of_ones_in_value_word % 2 == 1) and (count_of_ones == 0)):

            if(value_word[len(value_word) - 1] == 1):
                value_word[len(value_word) - 1] = 0
            elif(value_word[len(value_word) - 1] == 0):
                value_word[len(value_word) - 1] = 1

            # Убираем контрольные биты
            value_word.pop()
            counter = math.floor(math.log(len(value_word), 2))
            value = (2 ** counter) - 1
            while(counter >= 0):
                value_word.pop(value)
                counter = counter - 1
                value = (2 ** counter) - 1

            for i in range(len(value_word)):
                validation_hamming_mas.append(value_word[i])
            continue

        count_of_one_errors = count_of_one_errors + 1
        # Если одна ошибка, исправляем её
        # Обнуляем контрольные биты
        counter = 0
        value = 0
        while(value < len(value_word)):
            #print("value = ", value)
            control_bit.append(value_word[value])
            value_word[value] = 0
            counter = counter + 1
            value = (2 ** counter) - 1

        # Установка значений контрольных битов
        counter = 0
        value = 2 ** counter
        while(value - 1 < len(value_word)):
            i = value - 1
            count_of_one = 0
            while(i < len(value_word)):
                for j in range(value):
                    if(value_word[i] == 1):
                        count_of_one = count_of_one + 1
                    i = i + 1
                    if(i >= len(value_word)):
                        break
                i = i + value
            value_word[value - 1] = count_of_one % 2
            counter = counter + 1
            value = 2 ** counter

        try:
            first_word = Hamming_mas[k * length_hamming_word_output:(k + 1) * length_hamming_word_output]
        except:
            first_word = Hamming_mas[k * length_hamming_word_output:]

        # Находим ошибочный бит
        counter = 0
        value = 0
        number_of_error_bit = 0
        while(value < len(value_word)):
            if(value_word[value] != first_word[value]):
                number_of_error_bit = number_of_error_bit + (value + 1)
            counter = counter + 1
            value = (2 ** counter) - 1
        number_of_error_bit = number_of_error_bit - 1

        #print("number_of_error_bit = ", number_of_error_bit)

        # Исправляем слово
        if(number_of_error_bit < len(value_word)):
            if(value_word[number_of_error_bit] == 0):
                value_word[number_of_error_bit] = 1
            elif(value_word[number_of_error_bit] == 1):
                value_word[number_of_error_bit] = 0

        # Убираем контрольные биты
        value_word.pop()
        counter = math.floor(math.log(len(value_word), 2))
        value = (2 ** counter) - 1
        while(counter >= 0):
            value_word.pop(value)
            counter = counter - 1
            value = (2 ** counter) - 1

        for i in range(len(value_word)):
            validation_hamming_mas.append(value_word[i])

    #print("validation_hamming_mas = ")
    #print(validation_hamming_mas)
    #print()

    return validation_hamming_mas, count_of_zero_errors, count_of_one_errors, count_of_two_errors

# Перевод из десятичной сс в двоичную (число -> список)
def dec_bin(number):
    number_copy = copy.deepcopy(number)
    l = []
    while(number_copy != 0):
        l.append(number_copy % 2)
        number_copy = math.floor(number_copy / 2)
    l.reverse()
    #print("Десятичное число:")
    #print(l)
    return l

# Перевод из двоичной сс в десятичную (список -> число)
def bin_dec(l):
    l_copy = copy.deepcopy(l)
    number = 0
    for i in range(len(l_copy)):
        number = number + (l_copy[i] * (2 ** (len(l_copy) - i - 1)))
    return number