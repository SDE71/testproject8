# конвертация из списка в строку и из строки в список

# a, b, c = input('Enter something: ').split()
# print(a, b, c)

print("Hello people of Earth".split())
# метод split разбивает строку в список (на входе строка, на выходе список)
# у split есть параметр sep (сепаратор) по умолчанию стоят скобки? значит используется пробел
# но если в строке стоят слова с запятой и пробелом, то по умолчанию будут показываться и запятые
print("Hello, people, of, Earth".split())
# чтобы убрать запятые нужно в методе split указать так - b запятая не будет показываться
print("Hello, people, of, Earth".split(', '))
# при этом, если между какими-либо словами не будет пробела, то они склеются в один элемент
print("Hello, people,of, Earth".split(', '))
# наоборот - не будет запятой, а пробел останется, то слова тоже склеются в один элемент
print("Hello, people of, Earth".split(', '))
# так же и по цифрам
print("123-1234-12345678".split('-'))

a, b, c = [1, 2, 3]
print(a)
print(b)
print(c)

# a, b, c = input('Enter something: ').split()
# print(a)
# print(b)
# print(c)

# делаем из списка строку через метод join
courses = ['History', 'Math', 'Programming', 'Literature', 'Physics']
numbers = [1, 13, 6, 0.232, -123, 4, 7, 9, 11]
print(','.join(courses))
# поставим вместе с запятой и пробел - будет запятая и пробел
print(', '.join(courses))
# поставим *** - будет ***
print(' *** '.join(courses))
# можем соединить какой-нибудь срез из списка
print(' *** '.join(courses[1:4]))
# Задача - посчитать сколько слов в тексте
text_variable = '''Ситуация с - электроснабжением в Одесской области сложная, в городе отключены от света все потребители, кроме критической инфраструктуры, сообщила украинская энергетическая компания ДТЭК '''
print(len(text_variable))
# 185 это считает количество символов
print(len(text_variable.split()))
# 22 это уже количество слов, но будут считаться и тире, если перед и после тире будут пробелы и тогда 23
# можно сначала удалить все знаки препинания
# text_variable_1 = '''Ситуация! с - электроснабжением! в Одесской области сложная!, - в городе отключены от света все потребители, кроме критической инфраструктуры, сообщила - украинская энергетическая компания - ДТЭК '''
# text_variable_1.replace('!', '', -1)
# print(len(text_variable_1.split()))
# text_variable_1.re.sub('!', '')
# print(len(text_variable_1.split()))
# НЕ ПОЛУЧИЛОСЬ заменить(
# Идём далее - к спискам применимо сложение

print(courses + numbers)

# как создать копию списка?
new_courses = courses
new_courses.pop(0)
courses.pop()
# из первого списка выкинул первый элемент, а из второго списка выкинул последний элемент
# а списки получаеются одинаковыми
# т.е. присваивая новой переменной старое значение - мы не делаем копию
# мы говорим, что и там и там одинаковое значение и они связаны между собой
print(new_courses)
print(courses)
# для создания копии нужно добавить метод copy. В этом случае будет новое скопированное значение
new_courses_1 = courses.copy()
new_courses_1.pop(0)
courses.pop()
print(new_courses_1)
print(courses)
