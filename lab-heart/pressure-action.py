import matplotlib.pyplot as plt
import numpy as np


def Pressure(x):
    P = 0.417329 * x - 15.098481
    return P


input_file = 'data_2.txt'  # Имя входного файла


# Считываем данные из файла
data = np.loadtxt(input_file, delimiter=' ')


# Разделяем данные на два массива: значения и время
acp = data[:, 0]
values = []


for i in acp:
    values.append(Pressure(i))


time = data[:, 1]

# Вычисляем и выводим среднее значение первого столбца
average_acp = np.mean(acp)
print(f"Среднее значение первого столбца: {average_acp}")


# Строим график
plt.figure(figsize=(10, 6))
plt.plot(time, values, linestyle='-', color='b')
plt.plot(10.23682427406311, Pressure(393), 'o', color = 'black') 
plt.plot(51.66168189048767, Pressure(234), 'o', color = 'black')
plt.title('Артериальное давление после нагрузки')
plt.xlabel('Время (секунды)')
plt.ylabel('мм рт ст')
plt.grid(True)
plt.show()
