# file = open('student.txt', 'w')
# file.write('yaaaaaayuuuuuu\n')
# file.write('yayayaychachacha')
# file = open('student.txt')
# print(file.readline()) #читает целую строчку
# file.seek(0) #идет в исходное место
# print(file.read(4)) #читать сколько-то символов 
# for row in file: #вывести все строки 
#     for letter in row: #выведет каждую строку по буквам
#         print(letter)
# s = file.readlines() #cделает каждую строчку элементом списка
# print(s)



# file = open('/Users/churokbai/Desktop/st.txt', 'w')
# for i in range(10):
#     file.write('hello faiza\n')
# file.close()

# with open('/Users/churokbai/Desktop/st.txt', 'r') as file:
#     print(file.read())
# file.close()


# file_write = open('users.txt', 'a')
# popup = input('Registration or Login:')
# file_read = open('users.txt', 'r')
# if popup.lower() == 'registration':
#     username = input('username:')
#     password = input('password:')
#     password_confirm = input('password confirm:')
#     if password == password_confirm:
#         print('Password incorrect')
#         if username and password not in file_read.read():
#             file_write.write(f'Username:{username}\nPassword:{password}\n')
#             print('Success')
#         else:
#             print('User already exists')
# elif popup.lower() == 'login':
#     username = input('username:')
#     password = input('password:')
#     if username and password in file_read.read():
#         print('Success')
#     else:
#         print('User not found')
# file_read.close()
# file_write.close()
# file = open('st.txt', 'r')
# if 'w' in file:
#     print('да, в тексте есть w')
# else:
#     print('нет в тексте w')

# file_write = open('python.txt','w')
# file_write.write('Mind the clock\n And keep the rule:\n Always come in time to school')
# file_write.close()

# file_read = open('python.txt', 'r')
# t_word = []
# convert = (file_read.read().split())
# for i in convert:
#     if 'T' in i or 't' in i:
#         t_word.append(i)
#     else:
#         print('Not Found')
# print(list(set(t_word)))
# file_read.close()

# file = open('database.txt', 'a')
# file.write('имя:Zyzy пароль:203\nимя:William пароль:333\nимя:Garri пароль:67\n')
# files = open('database.txt', 'r')
# tap = input('Зарегистироваться или войти?:')
# if tap == 'Зарегистироваться':
#     name = input('имя:')
#     password = input ('пароль:')
#     password_confirm = input('повторите пароль:')
#     if password == password_confirm:
#         print('замечательно')
#         if name and password_confirm not in files.read():
#             file.write(f'имя:{name} пароль:{password}\n')
#         else:
#             print('Этот пользователь уже существует, войдите')  
#     file.close() 
 
# file = open('database.txt', 'w')
# Login = input('login:')
# Password = input('password:')
# photo = input('photo:')
# files = open(photo, 'rb')
# if files.read():
#     file.write(f'{Login}, {Password}, {photo}')
# else:
#     print('file not found')

file = open('database.txt', 'w')
photo_1 = input('photo:')
photo_2 = input('photo remove:')
files = open(photo_2, 'rb')
files2 = open(photo_2, 'rb')
if files.read():
    file.write(f'{photo_1}')
elif files2.read():
    file.write(f'{photo_2}')
else: 
    print('какой-то картинки не существует')



     
    

    



