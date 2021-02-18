# Задание 2.
# Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

with open('lesson5_task2.txt', encoding='utf-8') as f_obj:
    lines = f_obj.readlines()
print('Количество строк в файле: ' + str(len(lines)))
for num_line, line in enumerate(lines, start=1):
    print('В строке {} содержится {} слов'.format(num_line, len(line.split())))
