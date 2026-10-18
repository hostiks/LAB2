import csv
import random
import xml.etree.ElementTree as ET

file_books = open("books.csv", encoding="cp1251") #преобразуем строки в байты
reader = csv.reader(file_books, delimiter=";") #читаем файл, учитывая что столбцы разделены ;
all_rows = list(reader) #получаем матрицу
file_books.close()

header = all_rows[0]
books = all_rows[1:]
COL_TITLE = 1
COL_AUTHOR = 3
COL_DATE = 6
COL_PRICE = 7

print("Задание №1")

count_long = 0 #счетчик

for book in books:
    title = book[COL_TITLE]
    if len(title) > 30:
        count_long +=1

print("Записей с названием длиннее 30 символов:", count_long)
print()


print("Задание №2")

def search_by_author(query, min_price): #объявляем функцию
    found = []
    for book in books:
        author = book[COL_AUTHOR]
        price = float(book[COL_PRICE])
        if query in author and price >= min_price:
            found.append(book) #добавляем подходящие элементы в список
    return found

user_author = input("Введите автора: ")
result = search_by_author(user_author, 200)
print("Найдено записей:", len(result))

shown = 0
for book in result:
    print("-", book[COL_AUTHOR], "|", book[COL_TITLE], "| цена:", book[COL_PRICE])
    shown +=1
print()


print("Задание №3")

def make_reference(book):
    author = book[COL_AUTHOR]
    title = book[COL_TITLE]
    date_part = book[COL_DATE].split(" ")[0] #делим строку по пробелу и берем первую часть
    year = date_part.split(".")[-1] #делим строку по точке и берем последний элемент
    return author + ". " + title + " - " + year

books_with_author = []
for book in books:
    if book[COL_AUTHOR] != "":
        books_with_author.append(book)

chosen = random.sample(books_with_author, 20) #выбираем рандомные элементы
out_file = open("references.txt", "w") #создаем список в файле
number = 1  # номер строки
for book in chosen:
    reference = make_reference(book)
    line = str(number) + ". " + reference #преобразуем номер в строку и добавляем ссылку
    out_file.write(line + "\n")
    print(line)
    number +=1

out_file.close()
print("Список сохранён в файл references.txt")
print()


print("Задание №4")

tree = ET.parse("currency.xml") #строим дерево
root = tree.getroot() #берем верхний элемент (корень)
num_codes = []
char_codes = []

for valute in root.findall("Valute"): #ищем все элементы Valute
    num_text = valute.find("NumCode").text
    char_text = valute.find("CharCode").text
    num_codes.append(int(num_text))
    char_codes.append(char_text)

print("NumCode :", num_codes)
print("CharCode:", char_codes)