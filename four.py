# i = 67
# while i < 100:
#     print(i)
#     i+=5

# for i in range(20,40):
#     if i == 26:
#         print(i)
#         break
#     else:
#         print('no')

# lang1 = 'Rust'
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in languages:
#     if i == lang1:
#         print('this languages is in list')
#     else:
#         pass 

# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# i = 0
# while i < len(languages):
#     if 'php' in languages[i]:
#         break
#     else:
#         print('not')
#     i = i+ 1

# a = 7
# i = 0
# while i < 8:
#     a = a * 7
#     print(a)
#     i+=1
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in languages:
#     if i == languages:
#         print(i)

# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# qnty = 0
# for i in languages:
#     qnty += 1
# print(qnty)

# i = 0
# while i < 10:
#     print('Hello')
#     i += 1

# while True:
# #     name = input('name:')
# #     print(f'Hello {name}')
# #     cont = input('continue (yes/no)')
# #     if cont == 'yes':
# #         continue
# #     elif cont == 'no':
# #         break
# #     else:
# #         print('command not found')

# # for i in range(1,10):
# #     print('Hello Faiza')

# # a = ('admin', 'python', 'js', 'fornt')
# # for i in range(len(a)):
# #     print(i, a[i])
# # for i in range(-9,10):
# #     print(10-abs(i), end="")

# # names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан')
# # odd = []
# # even = []
# # for i in range(len(names)):
# #     if i % 2 == 0:
# #         even.append(names[i])
# #     else:
# #         odd.append(names[i])
# # print('Четные-', even)
# # print('Нечетные-', odd)
# # 
# #  
# # names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан')
# # odd = names[1::2]
# # even = names[0::2]
# # print('Четные-', even)
# # print('Нечетные-', odd) 

# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан')
# every_2nd_name = names[1::2]
# print('каждое 2 имя-', every_2nd_name)

# while True:
#     number = int(input('number:'))
#     if number >= 100:
#         print('three dijit')
#     elif number < 100:
#          print('not three dijit')
#     elif number >= 0:
#         print('positive')
#     else:
#         print('negative')
#     if number % 2 ==0:
#         print('even')
#     else:
#         print('odd')
#     if number > 100 and number % 17 == 0:
#         print(number)
#     elif number > 150 and number == 13**2:
#         print(number)
#     else:
#         print('no')
#     a = input('Continue (yes/no):')
#     if a == 'yes':
#         continue
#     elif a == 'no':
#         break 

# count_first = 0
# for i in range(-100,100):
#     if i % 13 == 0 and i % 2 == 0:
#         print(i**2)
#         count_first += 1
# print('first', count_first)        

# count_second = 0
# for i in range(-100,100,7):
#     if i % 2 != 0 :
#         print(i)
#         count_second += 1

# print('second', count_second) 

# a = {7,4,2,7,2}
# a.add(9)
# a.update([7,9,23])
# a.update('bye')
# a.update(range (6,9))
# a.discard('e') #при удалении несуществуещего обьекта ошибки не будет
# a.remove(8) #при удалении несуществуещего обьекта будет ошибка 
# a.pop() #так он удалит из множества случайный обьект
# a.clear() #очистит множество
# print(a, type(a))
# #операции над множествами
# a = {3,2,4}
# print(len(a)) #узнает длину множества
# print(8 in a, 9 not in a) #есть ли или нет ли обьект(-а) в множестве

# a = {45,66,55,2}
# b = {66,99,2,12}
# # print(a&b)
# # print(a.intersection(b))  #узнает общие элементы у двух множеств

# # a.intersection_update(b)
# print(a | b)
# print(a.union(b)) #обьединяет два множества
# print(b-a)

# a = {6,2,4,8}   
# for i in a:
#     print(i)
        
# dates_of_birth = {3,10,11,13,31,7,21,1,10,3,5,6,6}
# dates_of_birth.remove(7)
# print(dates_of_birth)

# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# print(farm_1&farm_2)
# print(farm_2-farm_1) 

# foods = {'cake', 'burger', 'rice', 'fri', 'chicken'}
# foods.add('salad')
# print(foods.pop())
# print(foods)

# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# menu['besh_barmak']=130
# menu['lagman']=135
# del menu['borsh']
# menu['Coca-Cola']='drinks'
# menu['Sprite']='drinks'
# menu['Fanta']='drinks'
# print(menu)

# mws = {'update', 'add', 'clear', 'intersection','pop', 'discard', 'intersection_update', 'difference','remove'}
# mwd = {'update', 'items', 'keys', 'clear', 'get', 'values'}
# print(mws.intersection(mwd))


# south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia',
# 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
# print(list(set(south_american_countries)))

# suitcase = [] 
# for i in range(5):
#     clouther = input('Вещи:')
#     suitcase.append(clouther)

# print(suitcase)
# last = int(len(suitcase)) - 1
# print('Блин последняя вещь мне не нужна ну его')
# suitcase.pop(last)
# print(suitcase)



# names = {'Mario':'doctor', 'Alex':'actor', 'Sergey':'bomj', 'Viktor':'deejay'}
# for k,v in names.items():
#     print(f'Здравствуйте {k} Прекрасная профессия {v}')

# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# farm_3 = set()
# data = (farm_2-farm_1)
# for i in data:
#     farm_3.add(i)
# print(farm_3)

animal = {1: "dog", 2: "cat", 3: "mouse", 4:"sheep"}
print(animal[1])