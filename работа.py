import re
class Biblioteka(): #Создание библиотеки с переменными: отдел, кол-во книг, кол-во газет, кол-во журналов
    def __init__(self, chapter, book_in, newspapers_in, journal_in):
        self.chapter = chapter                 
        self.book_in = book_in
        self.newspapers_in = newspapers_in
        self.journal_in = journal_in   

    #установка пароля при входе в библиотеку
pattern_password = \
    r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Zaz\d@$!%*?&]{8,}$"

user_input = input('Установите пароль:') #AZaz13@!*

invalid_pass_text = \
    "Для гарантии надежности пароль должен состоять как минимум из 8 символов,\
 в число которых должны входить, по крайней мере,\
 по одной заглавной и строчной букве,\
 цифре и одному специальному символу"
if (re.search(pattern_password, user_input)):
    print("Установлен надежный пароль")   
    user_input2 = input("Введите пароль:")   #ввод пароля при входе в библиотеку
    if user_input2 == user_input:
        print("Вход разрешён")
    else:
        print("Вход запрещён. Начните заново.") 
else:
     print(invalid_pass_text)


