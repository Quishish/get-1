import matplotlib.pyplot as plt
import numpy as np

def Pressure(N):
    P = 0.099 * N - 7.24
    return P

input_file = 'data_1.txt'  # Имя входного файла

# Считываем данные из файла
data = np.loadtxt(input_file, delimiter=' ')

# Разделяем данные на два массива: значения и время
acp = data[:, 0]
values = []

for i in acp:
    values.append(Pressure(i))

time = data[:, 1]

# Строим график
plt.figure(figsize=(10, 6))
plt.plot(time, values, linestyle='-', color='b')
plt.plot(7.576132535934448, Pressure(343), 'o', color = 'black')
plt.plot(54.503657579422, Pressure(192), 'o', color = 'black')
plt.title('График зависимости значений от времени')
plt.xlabel('Время (секунды)')
plt.ylabel('Значения')
plt.grid(True)
plt.show()

