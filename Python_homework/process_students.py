import os #os: Импортирует модуль work с файлами компа
import csv #sv: Импортирует модуль 
import json #json: Импортирует модуль 
from collections import defaultdict #Импортирует класс defaultdict из модуля collections.
#defaultdict - это подкласс словаря, который позволяет установить значение по умолчанию для отсутствующих ключей.

def load_json(file_path): #Определение функции `load_json`, которая принимает путь к файлу `file_path` в качестве аргумента.
    with open(file_path, 'r') as json_file: #Открывает файл, указанный в `file_path`,
      #в режиме чтения (`'r'`) с использованием конструкции `with`, что гарантирует, что файл будет правильно закрыт после использования.
        data = json.load(json_file) #Загружает данные из JSON-файла с использованием метода `load` модуля `json`. Результат сохраняется в переменной `data`.
    return data #Возвращает загруженные данные.

def save_to_csv(file_path, data, fieldnames): #Определение функции `save_to_csv`, которая сохраняет данные в CSV-файл.
    with open(file_path, 'w', newline='', encoding='utf-8') as csv_file: #Открывает файл для записи (`'w'`) в режиме текстового файла (`'t'`) с указанием кодировки UTF-8.
       #`newline=''` используется для предотвращения автоматической вставки дополнительных символов новой строки.
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames) #Создает объект `DictWriter` для записи словарей в CSV-файл. `fieldnames` - это список заголовков столбцов.
        writer.writeheader() #Записывает заголовки столбцов в CSV-файл.
        writer.writerows(data) #Записывает строки данных в CSV-файл.

def calculate_stipend(score, stip_rules, default_stip): #расчёт стпинендии по правилам
    for threshold, stip_amount in sorted(stip_rules.items(), key=lambda x: int(x[0]), reverse=True): #проход по элементам словаря
        if score >= int(threshold): #проверка превышает ли балл студента
            return stip_amount #Возвращает значение стипендии, если балл студента удовлетворяет условиям.
    return default_stip #Возвращает значение стипендии по умолчанию, если не найдено соответствие.

def process_expulsion_and_next_semester(input_dir, output_dir): #):: Определение функции с двумя параметрами(путь к входным данным и для сохрана резов)
    # Load komission_rules.json
    komission_rules = load_json(os.path.join(input_dir, 'komission_rules.json')) # Загрузка правил из файла 

    # Load student data
    student_data = []
    with open(os.path.join(input_dir, 'semester_result', 'student.csv'), 'r', encoding='utf-8') as student_file:
        student_reader = csv.DictReader(student_file)
        student_data = list(student_reader)

    # Load assessment data
    assessment_data = []
    with open(os.path.join(input_dir, 'semester_result', 'assessment.csv'), 'r', encoding='utf-8') as assessment_file:
        assessment_reader = csv.DictReader(assessment_file)
        assessment_data = list(assessment_reader)

    # Load group data
    group_data = []
    with open(os.path.join(input_dir, 'semester_result', 'group.csv'), 'r', encoding='utf-8') as group_file:
        group_reader = csv.DictReader(group_file)
        group_data = list(group_reader)

    # Load new_student data
    new_student_data = []
    with open(os.path.join(input_dir, 'semester_result', 'new_student.csv'), 'r', encoding='utf-8') as new_student_file:
        new_student_reader = csv.DictReader(new_student_file)
        new_student_data = list(new_student_reader)

    # Process data and generate expulsion list
    expulsion_list = [] # Инициализация пустого списка для хранения данных об исключении студентов.
    for student in student_data: # Цикл по студентам.
        stud_id = student['stud_id'] # Получение идентификатора студента.
        points = sum(int(assessment['points']) for assessment in assessment_data if assessment['stud_id'] == stud_id) # Вычисление суммы баллов для данного студента.
        if points < 51: #проверка
            expulsion_list.append(student) #Добавление студента в список исключенных.

    # Save expulsion list to expulsion_student.csv сохран
    expulsion_file_path = os.path.join(output_dir, 'expulsion_student.csv') #Формирование пути для файла с данными об исключенных студентах.
    save_to_csv(expulsion_file_path, expulsion_list, ['group_id', 'stud_id', 'fio', 'country', 'payment', 'stip'])

    # Process data and generate next semester list
    next_semester_list = [] #для хранения данных о студентах следующего семестра
    for student in new_student_data: #Цикл по новым студентам.
        stip_rules = komission_rules['stip_rules'] #Получение правил
        default_stip = komission_rules['default_stip'] #Получение значения стипендии по умолчанию.
        student['stip'] = calculate_stipend(100, stip_rules, default_stip) #Вычисление стипендии для студента и добавление значения в данные студента.
        next_semester_list.append(student) #Добавление студента в список для следующего семестра.

    # Save next semester list to next_semester_student.csv
    next_semester_file_path = os.path.join(output_dir, 'next_semester_student.csv')
    save_to_csv(next_semester_file_path, next_semester_list,
                ['stud_id', 'fio', 'country', 'payment', 'direction_of_study', 'stip'])

    # Save new group list to next_semester_group.csv
    next_semester_group_file_path = os.path.join(output_dir, 'next_semester_group.csv')
    save_to_csv(next_semester_group_file_path, group_data, ['group_id', 'direction_of_study'])

    # Task 1: Find selected students based on different criteria 4.4
    selected_students = defaultdict(list) #Создание словаря в котором будут студенты по разным критериям
    for student in student_data: #проходка по данным студентов (итерация)
        stud_id = int(student['stud_id']) #извлекаем индентификатор
        
        
        score = sum(int(assessment['points']) for assessment in assessment_data if assessment['stud_id'] == str(stud_id))
        score /= len(set(assessment['course'] for assessment in assessment_data if assessment['stud_id'] == str(stud_id)))

        stip_before = int(student['stip']) #извлекаем размер стипендии перед изменением
        #score=total_points/len(assessment_data)
        stip_after = calculate_stipend(score, stip_rules, default_stip) #вычисляем новую стипуху

        if stip_before > stip_after: #проверка на боль студента(понижение стипухи)
            selected_students['stip_down'].append(stud_id) #добавляем ид студента в список

# Save selected students to selected_student.json
    selected_student_file_path = os.path.join(output_dir, 'selected_student.json') #формируем путь
    with open(selected_student_file_path, 'w', encoding='utf-8') as selected_student_file:
        json.dump(selected_students, selected_student_file, indent=2) #запись с отступами

    # Task 2: Find the worst courses
    courses_points = defaultdict(int) #создаём для подсчёта неудач по каждому курсу
    for assessment in assessment_data: #мощная проходка по данным об оценкам
        course = assessment['course']
        points = int(assessment['points'])
        if points < 51:
            courses_points[course] += 1 #увеличиваем счётчик если балллы меньше 51

    worst_courses = [course for course, _ in sorted(courses_points.items(), key=lambda x: x[1], reverse=True)] #формируем список по количеству неудач

    # Save worst courses to selected_course.json #создание и запись в файл
    selected_course_file_path = os.path.join(output_dir, 'selected_course.json')
    with open(selected_course_file_path, 'w', encoding='utf-8') as selected_course_file:
        json.dump({'worst': worst_courses}, selected_course_file, indent=2)

    # Task 3: Find the group with the minimum total stipend
    group_stip_sum = defaultdict(int) #MMM для подсчёта общей стипендии по каждой группе
    for student in student_data: #проход по данным
        group_id = student['group_id']
        stip_before = int(student['stip'])
        group_stip_sum[group_id] += stip_before

    min_stip_groups = [group for group, _ in sorted(group_stip_sum.items(), key=lambda x: x[1])] #список с минимальной общей стипухой в возрастающем порядке

    # Save groups with the minimum total stipend to selected_group.json запись в файл
    selected_group_file_path = os.path.join(output_dir, 'selected_group.json')
    with open(selected_group_file_path, 'w', encoding='utf-8') as selected_group_file:
        json.dump({'min_stip': min_stip_groups}, selected_group_file, indent=2)

if __name__ == "__main__": #":: Проверяет, запущен ли скрипт напрямую (а не импортирован как модуль)
    working_directory = input("Введите путь к рабочей директории: ") #запрос
    output_directory = os.path.join(working_directory, 'next_semester_output') #формирование путя к подпапке
    os.makedirs(output_directory, exist_ok=True) #создаёт папку, если её нет
    process_expulsion_and_next_semester(working_directory, output_directory) #Вызывает функцию для обработки данных и сохранения результатов в указанную подпапку.
