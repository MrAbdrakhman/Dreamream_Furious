




# Задание 1:
# У вас есть идея создать Back-end для игры: "Угадай число."
# Данный код генерирует рандомное число.
###################
import random as rd
random_number = rd.randint(0,10)
print(random_number)
###################
# С помощью функции:
#    my_number = int(input("Введите число: "))
# спрашивайте число от пользователя.
# Запустите бесконечный цикл!
# И пытайтесь спрашивать у пользователя какое-то число каждый раз.
# Если пользователь угадал число которое сгенерировал компьютер остановите цикл и скажите пользователю - "Вы угадали!"
# Если пользователь не угадал вы снова спросите у него число.
# Если пользователь 3 раза подряд не угадал число, вы останавливаете цикл и говорите: "Вы проиграли..."
#######################################################################



# Задание 2:
        # Напишите программу, которая циклично запрашивает у пользователя номера символов по таблице Unicode и выводит соответствующие им символы. 
        # Завершает работу при вводе нуля.
###################################################################



# Задание 3:
        # Напишите программу, которая измеряет длину введенной строки. 
        # Если строка длиннее десяти символов, то выносится предупреждение. 
        # Если короче, то к строке добавляется столько символов *, чтобы ее длина составляла десять символов, после чего новая строка должна выводиться на экран.
###################################################################



# Задание 4:
        # Напишите программу, которая запрашивает у пользователя шесть вещественных чисел. 
        # На экран выводит минимальное и максимальное из них, округленные до двух знаков после запятой. 
        # Выполните задание без использования встроенных функций min() и max().
####################################################################



# Задание 5:
        # Напишите программу которая принимает число любой длины и вытаскивает из него самое большое и самое маленькое число.
####################################################################



text = """
The Zen of Python, by Tim PetersBeautiful is better than ugly.Explicit is better than implicit.
Simple is better than complex.Complex is better than complicated.
Flat is better than nested.Sparse is better than dense.
Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.
Errors should never pass silently.Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one--and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea --let's do more of those!
"""
################################################################




# Задание 6:
#     Функция
#     Напишите функцию, которая берет текст, и возвращает строковое значение, состоящее из заглавных букв. 
#     Используйте текст, данный выше (The Zen of Python).
#     Подсказка: используйте метод строчных значений, который проверяет, “заглавность” буквы.
##################################################################

t2 =list(text.split())
t3=[]
print("Решение зад 6")
def cap(a):
    for i in a:
        if i[0].istitle():
            t3.append(i)
    return t3
print(cap(t2))



# Задание 7:
#     Чтение из файла.
#     Создайте файл с текстом The Zen of Python. 
#     Напишите функцию, которая считайте его и возвратит список из слов, которые начинаются на букву “c” или “C”.
#     Подсказка: используйте метод строчных значений, который проверяет, начинается ли слово на переданную букву.
####################################################################
print('Решение зад 7')
def creater_f(a):
    with open('zen.txt', 'w+') as f:
        f.write(a)
        return f
print(creater_f(text))
list1=[]
def check_c():
    with open("zen.txt", 'r') as f:
        txt = f.read()
        txt2 = list(txt.split(' '))
        for i in txt2:
            if "c"==i[0] or 'C'==i[0]:
                list1.append(i)
        return  list1
print(check_c())



# Задание 8:
#     Банкомат
#     Напишите код банкомата, который принимает цифру, выдает деньги с номиналом 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 3, 1.
#     Подсказка: напишите функцию, используйте divmod()
##################################################################
print('Решение зад 8')
nominal=[5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 3, 1]
money=int(input('введите сумму которую хотите получить с банкомата '))
def bank(money, nominal):
    s = 0
    for i in nominal:
        k=money//i
        if k>0:
            money=money-i*k
            print('номинал: ',i,"количество купюр: ", k)
            s=s+i*k
    return s
print("Итого вы получите: ",bank(money,nominal))



# Задание 9:
#     Напишите функцию которая принимает два аргумента (числа), умножает их друг на друга, 
#         и возвращает функцию, которая также берет два аргумента (числа), 
#             и возвращает результат умножения аргументов внешней функции плюс результат деления 
#                 аргументов внутренней функции.
#     Подсказка: (outer_arg1 * outer_arg2) + (inner_arg1 / inner_arg2)
####################################################################
print("Решение зад 9")
a = int(input("введите первый аргумент "))
b = int(input("введите второй аргумент "))

def vnesh(a, b):
    def vn(a, b):
        print(a/b)
        return a / b
    print((a * b))
    return vn(a, b) + (a * b)





# Задание 10:
#     Фильтрация с помощью filter(). Необходимо написать функцию, и передать ее filter(), 
#     чтобы получить список только тех слов из текста text (см. выше “The Zen of Python”), что содержат букву ‘p’.
#     Подсказка: необходимо заменить \n на пробел. 

#     То есть, это нужно проделать еще до фильтрации. 
#     Функция, которая будет передана в filter() должна возвращать True, если в слове есть буква ‘p’.
#####################################################################
print('Решение зад 10')
text2=list(text.split())
def f1(word_p):
    for i in range(len(word_p)):
        if word_p[i]=='p':
            return True
    return False
out_text=filter(f1,text2)
print(list(out_text))


# Задание 11:
#     Дано
dict_one = {'a':1, 'b':2, 'c':3}
dict_two = {'d':4, 'e':5, 'f':6}
dict_three = {'g':7, 'h':8, 'i':9}
dict_four = {}
#     С помощью цикла for необходимо собрать три первых словаря в словарь dict_four

#     Подсказка: Для удобства итерации, первые три словаря можно записать в кортеж (dict_one, dict_two, dict_three
#####################################################################
print('Решение зад 11')
a=tuple(dict_one.items())
b=tuple(dict_two.items())
c=tuple(dict_three.items())
d=a+b+c
for i in d:
    dict_four.update({i[0]:i[1]})
print(dict_four)



# Задание 12:
#     Аналог шифра цезаря ". Программа должна запрашивать элементы
#     списка через пробел. После чего пользователь должен ввести значение
#     для сдвига элементов списка. Значение может быть как положительным,
#     так и отрицательным. Если значение положительное, элементы списка
#     должны сдвигаться вправо, если отрицательное - влево. Результат
#     необходимо вывести на экран:

#     Пример:
#     [1, 2, 3, 4, 5], сдвиг 2
#     [3, 4, 5, 1, 2]
#####################################################################
print('Решение зад 12')
a = list(map(int, input('Введите лементы списка через пробел ').split()))
n= int(input('Введите значение для сдвига элементов '))
print(a)
def check_code(a,n):
    if n>0:
        for i in range(0,n):
            a=a + [a.pop(0)]
    elif n<0:
        for i in range(0,n,-1):
            a = [a.pop(-1)]+a
    return a
print(check_code(a,n))




# Задание 13:
#     Напишите программу, где исходный список содержит положительные и отрицательные числа. 
#     Требуется положительные поместить в один список, а отрицательные - в другой.
###################################################################
print('Решение зад 13')
l1=[-5,2,6,8,-9]
l2=[12,3,-4,6,-8,-5]
lp=[]
lo=[]
def list_dist(a):
    for i in a:
        if i>0:
            lp.append(i)
        else:
            lo.append(i)
    return lp, lo
list_dist(l1)
list_dist(l2)
print(lp,lo)


# Задание 14:
#     Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).
#####################################################################
print("Решение зад 14")
n=int(input('Введите номер месяца '))
vesna=[3,4,5]
leto=[6,7,8]
osen=[9,10,11]
zima=[12,1,2]
def sezon(a):
    if a in vesna:
        return 'весна'
    if a in leto:
        return 'лето'
    if a in osen:
        return 'осень'
    if a in zima:
        return 'зима'
print(sezon(n))



# 15 Спарсить новости с kaktus и вывести эти новости в телеграм боте
# zad_10_Bot - название бота
def newsget():
    from bs4 import BeautifulSoup
    import requests
    data = requests.get('https://kaktus.media/')
    soup = BeautifulSoup(data.text, 'html.parser')
    allNews = soup.find('div', class_='Dashboard-Board Dashboard-Board----FORE_MEDIA')
    news = allNews.findAll('a', class_='Dashboard-Content-Card--name')
    text = ''
    for i in news:
        text += str(i.text)
    return text
import logging
from aiogram import Bot, Dispatcher, executor, types
# Объект бота
bot = Bot(token="5392920690:AAEUyDHZor5gO6fr9cylQZoaP4UGeZh16Kc")
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Хэндлер на команду /test1
@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
    await message.reply(newsget())
if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
