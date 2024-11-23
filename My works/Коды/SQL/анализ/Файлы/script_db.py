# Данный python-скрипт имитирует запрос к БД
# Напишите ваш SQL-запрос в query и запустите данный python-скрипт для получения результата
# Перед запуском скрипта установите библиотеку duckdb

# Установка библиотеки duckdb
# pip install duckdb duckdb-engine

# Импорт библиотек
import pandas as pd
import duckdb

# Задание таблиц БД
users = pd.read_csv('users.csv')
course_users = pd.read_csv('course_users.csv')
courses = pd.read_csv('courses.csv')
course_types = pd.read_csv('course_types.csv')
lessons = pd.read_csv('lessons.csv')
subjects = pd.read_csv('subjects.csv')
cities = pd.read_csv('cities.csv')
homework_done = pd.read_csv('homework_done.csv')
homework = pd.read_csv('homework.csv')
homework_lessons = pd.read_csv('homework_lessons.csv')
user_roles = pd.read_csv('user_roles.csv') 

# Создание DuckDB и регистрация DataFrame как таблиц
con = duckdb.connect()
con.register('users', users)
con.register('cities', cities)
con.register('user_roles', user_roles)
con.register('courses', courses)
con.register('course_types', course_types)
con.register('subjects', subjects)
con.register('course_users', course_users)
con.register('homework_done', homework_done)
con.register('homework', homework)
con.register('homework_lessons', homework_lessons)
con.register('lessons', lessons)

# SQL-запрос для получения информации о пользователях на годовых курсах
query = """
-- Запрос для извлечения информации о пользователях на годовых курсах

WITH homework_count AS (
    SELECT 
        homework_done.user_id,
        lessons.course_id,
        COUNT(homework_done.id) AS homework_completed
    FROM 
        homework_done
    JOIN 
        homework ON homework_done.homework_id = homework.id
    JOIN 
        homework_lessons ON homework.id = homework_lessons.homework_id
    JOIN 
        lessons ON homework_lessons.lesson_id = lessons.id
    GROUP BY 
        homework_done.user_id, lessons.course_id
)

SELECT 
    courses.id AS course_id,                              -- ID курса
    courses.name AS course_name,                          -- Название курса
    subjects.name AS subject_name,                        -- Название предмета
    course_types.name AS course_type,                     -- Тип курса
    courses.starts_at AS course_start_date,               -- Дата старта курса
    users.id AS user_id,                                  -- ID ученика
    users.last_name AS user_last_name,                    -- Фамилия ученика
    cities.name AS city_name,                             -- Город ученика
    course_users.active AS is_active,                     -- Ученик не отчислен с курса
    course_users.created_at AS course_open_date,          -- Дата открытия курса ученику
    course_users.available_lessons AS available_lessons,  -- Количество доступных уроков в месяц
    COALESCE(homework_count.homework_completed, 0) AS homework_completed -- Число сданных ДЗ ученика на курсе
FROM 
    course_users
JOIN 
    users ON course_users.user_id = users.id               -- Присоединение таблицы пользователей
JOIN 
    courses ON course_users.course_id = courses.id         -- Присоединение таблицы курсов
JOIN 
    course_types ON courses.course_type_id = course_types.id -- Присоединение таблицы типов курсов
JOIN 
    subjects ON courses.subject_id = subjects.id           -- Присоединение таблицы предметов
JOIN 
    cities ON users.city_id = cities.id                    -- Присоединение таблицы городов
LEFT JOIN 
    homework_count ON homework_count.user_id = users.id 
    AND homework_count.course_id = courses.id              -- Присоединение с количеством сданных домашних заданий
WHERE 
    course_users.active = TRUE                            -- Только активные ученики
GROUP BY 
    courses.id, courses.name, subjects.name, course_types.name, courses.starts_at,
    users.id, users.last_name, cities.name, course_users.active, 
    course_users.created_at, course_users.available_lessons, homework_count.homework_completed;
"""

# Выполнение SQL-запроса
df_result = con.execute(query).fetchdf()

# Вывод результата
print(df_result)