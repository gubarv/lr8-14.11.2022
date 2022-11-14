from dataclasses import dataclass
import re
class Biblioteka(): #Создание библиотеки с переменными: отдел, кол-во книг, кол-во газет, кол-во журналов
    def __init__(self, chapter, book_in, newspapers_in, journal_in):
        if  isinstance(chapter, str):
            self.chapter = chapter
        else:                                   
            raise InvalidNameError()        
        
        self.book_in = book_in
        self.newspapers_in = newspapers_in
        self.journal_in = journal_in

    #Перегрузка операций
    def __add__(self, zavoz):
        self.book_in += zavoz
        
    def __call__(self, zavoz):
        self.book_in = zavoz

    def Monitoring(self):
        print(f"Количество книг:{self.book_in}")

    def nn(self): 
        self.__number_of_newspapers_in_chapter()
        self.__number_of_journal_in_chapter()
    def __number_of_newspapers_in_chapter(self): #кол-во газет в отделе с приватным доступом
        print("В отделе " + self.chapter + " находится " + str(self.newspapers_in) + " газет.")
    def __number_of_journal_in_chapter(self): #кол-во журналов в отделе с приватным доступом
        print("В отделе " + self.chapter + " находится " + str(self.journal_in) + " журналов.")



    #Класс для вывода ошибки
class InvalidNameError(Exception):
    def __str__(self):
        return f"Неправильное название! Название состоит из цифр, а должно из букв! Проверка"


    #Реализация датакласса
    #Данный датакласс приписан к классу <<Читательные залы>>
@dataclass
class Place_book:
    #Класс "местоположение книги" с переменными: номер шкафа, номер полки, номер места
    number_wardrob: int
    number_shelf: int
    number_place: int

def Get_place_books() -> Place_book:
    return 'Полное местоположение книги:', Place_book(48, 86, 61)

def Get_place_book() -> Place_book:
    return Place_book(13, 10, 4)
    #Конец датакласса



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


#Начало проверки на ошибки
try:
    b1 = Biblioteka("Психология", 115, 22, 34)
    # b1.nn() 
    # b1.otdel()

except InvalidNameError as e:
    print(e)
#Конец проверки на ошибки

# Начало перегрузки операций
#b1.Monitoring()
#b1(150)
#b1.Monitoring()
#b1 + 50
#b1.Monitoring()
# Конец перегрузки операций

#Использование датакласса

#print(Get_place_books())
#print("Полное метоположение книги:", Get_place_book())
#print("Номер шкафа:", Get_place_book().number_wardrob)
#print("Номер полки:",Get_place_book().number_shelf)
#print("Номер места:",Get_place_book().number_place)

