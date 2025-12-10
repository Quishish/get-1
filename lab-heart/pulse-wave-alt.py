import numpy as np
import matplotlib.pyplot as plt

# Калибровочные коэффициенты
k = 0.343789
b = -7.301247

# Загрузка данных
input_file = 'data_3.txt'
data = np.loadtxt(input_file, delimiter=' ')

units = data[:, 0]
time = data[:, 1]
pressure = k * units + b

# ПРОСТОЕ СГЛАЖИВАНИЕ - Скользящее среднее
window_size = 25  # Размер окна (чем больше - тем сильнее сглаживание)

# Метод 1: Через np.convolve (самый простой)
pressure_smooth = np.convolve(pressure, np.ones(window_size)/window_size, mode='same')

# Метод 2: Через pandas (еще проще, если pandas установлен)
# import pandas as pd
# pressure_smooth = pd.Series(pressure).rolling(window=window_size, center=True).mean().values

# Построение графика
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))

# График 1: Полная запись
ax1.plot(time, pressure, 'b-', alpha=0.3, linewidth=0.5, label='Исходные данные')
ax1.plot(time, pressure_smooth, 'r-', linewidth=2, label='Сглаженные данные')
ax1.set_xlabel('Время (секунды)', fontsize=12)
ax1.set_ylabel('Давление (мм рт ст)', fontsize=12)
ax1.set_title('Пульсовая волна - полная запись', fontsize=14, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.legend(fontsize=10)

# График 2: Увеличенный фрагмент
time_limit = 3.0
mask = time <= time_limit
ax2.plot(time[mask], pressure[mask], 'b-', alpha=0.3, linewidth=0.5, label='Исходные данные')
ax2.plot(time[mask], pressure_smooth[mask], 'r-', linewidth=2, label='Сглаженные данные')
ax2.set_xlabel('Время (секунды)', fontsize=12)
ax2.set_ylabel('Давление (мм рт ст)', fontsize=12)
ax2.set_title(f'Пульсовая волна - фрагмент (0-{time_limit} сек)', fontsize=14, fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.legend(fontsize=10)

plt.tight_layout()
plt.show()

print(f"Размер окна сглаживания: {window_size} точек")
print(f"Среднее давление: {pressure_smooth[~np.isnan(pressure_smooth)].mean():.1f} мм рт ст")
