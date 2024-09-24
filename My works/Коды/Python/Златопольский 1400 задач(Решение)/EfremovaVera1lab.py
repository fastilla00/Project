import pandas as pd
import matplotlib.pyplot as plt

# 1. Чтение данных из CSV файла
df = pd.read_csv('https://www.ncei.noaa.gov/pub/data/cdo/samples/LCD_sample_csv.csv')
print("Первые пять строк данных:")
print(df.head())

# 2. Запись DataFrame в CSV файл
df.to_csv('new_file.csv', index=False)
print("\nДанные записаны в файл 'new_file.csv'")

# 3. Выбор столбца из DataFrame
column = df['HourlyDryBulbTemperature']
print("\nСтолбец 'HourlyDryBulbTemperature':")
print(column)

# 4. Выбор строки по индексу
row = df.iloc[0]
print("\nПервая строка данных:")
print(row)

# 5. Фильтрация данных по условию
filtered_data = df[df['HourlyDryBulbTemperature'] > 50]
print("\nДанные с температурой выше 50:")
print(filtered_data)

# 6. Группировка данных по столбцу
grouped_data = df.groupby('StationName').sum()
print("\nСгруппированные данные по станциям:")
print(grouped_data)

# 7. Объединение двух DataFrame
data1 = {'StationName': ['A', 'B'], 'Value1': [1, 2]}
data2 = {'StationName': ['A', 'B'], 'Value2': [3, 4]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
merged_df = pd.merge(df1, df2, on='StationName')
print("\nОбъединенные данные:")
print(merged_df)

# 8. Расчет основных статистических показателей
print("\nОсновные статистические показатели:")
print(df.describe())

# 9. Сортировка данных
sorted_df = df.sort_values(by='HourlyDryBulbTemperature', ascending=True)
print("\nОтсортированные данные по температуре:")
print(sorted_df)

# 10. Построение простого графика
df['HourlyDryBulbTemperature'].plot(kind='bar')
plt.title('Hourly Dry Bulb Temperature')
plt.xlabel('Index')
plt.ylabel('Temperature')
plt.show()

# 11. Сохранение DataFrame в Excel файл
df.to_excel('output.xlsx', index=False)
print("\nДанные сохранены в файл 'output.xlsx'")
