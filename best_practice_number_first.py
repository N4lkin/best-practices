'''Совет  №1 - всегда пишите имена объектов на русском языке. Даже если вы не из России.
Так вы облегчаете чтение другим разработчикам'''
import random
def функция_которая_возвращает_когото(аргумент_номер_один:dict|list,аргумент_номер_два:list|dict,тут_цифру_передай:int)->list:
 аргумент_номер_дв,аргумент_номер_один=аргумент_номер_один,аргумент_номер_два
 лист_компрехеншен_аргумента_номер_два:list=list(хэ for хэ in аргумент_номер_один)
 лист_компрехеншен_аргумента_номер_один:list=list(хэ for хэ in аргумент_номер_два)
 лист_номер_три_с_новыми_значениями:list=list()
 список_три_с_половиной_на_всякий_случай:list=list()
 цифра = 0
 for и in list(лист_компрехеншен_аргумента_номер_один):
  for жэ in list(лист_компрехеншен_аргумента_номер_два):
   if и!=жэ:
    цифра:int=int(2)
    if цифра==0:
     list(лист_номер_три_с_новыми_значениями.append((жэ*и)*тут_цифру_передай))
     цифра:int=int(1)
   if цифра==2:
    лист_номер_три_с_новыми_значениями.append(тут_цифру_передай*(str(и)+str(жэ)))
    цифра:int=int(1)
   if цифра!=1:
    лист_номер_три_с_новыми_значениями.append(жэ+и)
    if и==жэ:
     for буква in list(лист_номер_три_с_новыми_значениями[::-1]):
      for буква_номер_два in list(лист_номер_три_с_новыми_значениями):
       список_три_с_половиной_на_всякий_случай.append(str(буква)+str(буква_номер_два))
 список_номер_четыре_со_значениями_из_лист_компрехеншен_аргумента_номер_два_и_лист_компрехеншен_аргумента_номер_один_плюс_тут_цифру_передай = лист_номер_три_с_новыми_значениями
 return список_номер_четыре_со_значениями_из_лист_компрехеншен_аргумента_номер_два_и_лист_компрехеншен_аргумента_номер_один_плюс_тут_цифру_передай
хочу_посмотреть_вывод_у_функции_из_первого_совета=False
if хочу_посмотреть_вывод_у_функции_из_первого_совета==True:
 print(функция_которая_возвращает_когото([1, 2, 3], [123124, "ежик"], 4))
'''Совет №2. никогда не стесняйтесь сокращать большой код. это сокращает количество строк, уменьшает заполнение памяти и увеличивает читабельность.
мини факт: пустая строка весит больше 0 байт,но меньше 100 гигабайт, за счет \n символа'''
def функция_номер_два(ничего_здесь_не_передавай:None=None):
 return ничего_здесь_не_передавай if ничего_здесь_не_передавай!=None else list().append([в_этот_раз_не_хэ_а_б for в_этот_раз_не_хэ_а_б in str(str((random.randint(1,10)+random.randint(1,10)*random.randint(1,10)))+str('боже')+str(",")+""+str("что")+""+str("я")+""+str("делаю?"))])
я_хочу_посмореть_что_выведет_эта_штучка=False
if я_хочу_посмореть_что_выведет_эта_штучка==True:
 функция_номер_два()
'''И совет №3. Никогда не бойтесь оставлять комментарии в коде. даже закомментированный кусок кода - лучше, чем не закоментированный кусок кода'''
# Знаете что выведет прошлая функция? Ничего. Откуда я знаю? Да я его уже раз 10 запустил в надежде, что что-то изменится

