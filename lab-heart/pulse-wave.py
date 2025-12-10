import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

# Калибровочные коэффициенты
# P = k * x + b, где x - условные единицы, P - давление в мм рт ст
k = 0.343789
b = -7.301247

# Загрузка данных из выбранного файла
input_file = 'data_3.txt'
data = np.loadtxt(input_file, delimiter=' ')

# Разделение данных
units = data[:, 0]  # Условные единицы
time = data[:, 1]   # Время в секундах

# Перевод в мм рт ст
pressure = k * units + b

# Сглаживание данных фильтром Савицкого-Голея
# window_length должен быть нечетным числом
# polyorder - степень полинома для сглаживания
window_length = 51  # Окно сглаживания
polyorder = 3       # Порядок полинома

pressure_smooth = savgol_filter(pressure, window_length, polyorder)

# Построение графика
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))

# График 1: Исходные и сглаженные данные (полная запись)
ax1.plot(time, pressure, 'b-', alpha=0.3, linewidth=0.5, label='Исходные данные')
ax1.plot(time, pressure_smooth, 'r-', linewidth=2, label='Сглаженные данные')
ax1.set_xlabel('Время (секунды)', fontsize=12)
ax1.set_ylabel('Давление (мм рт ст)', fontsize=12)
ax1.set_title('Пульсовая волна - полная запись', fontsize=14, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.legend(fontsize=10)

# График 2: Увеличенный фрагмент (первые 3 секунды для лучшей видимости пульсаций)
time_limit = 3.0
mask = time <= time_limit
ax2.plot(time[mask], pressure[mask], 'b-', alpha=0.3, linewidth=0.5, label='Исходные данные')
ax2.plot(time[mask], pressure_smooth[mask], 'r-', linewidth=2, label='Сглаженные данные')
ax2.set_xlabel('Время (секунды)', fontsize=12)
ax2.set_ylabel('Давление (мм рт ст)', fontsize=12)
ax2.set_title(f'Пульсовая волна - увеличенный фрагмент (0-{time_limit} сек)', fontsize=14, fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.legend(fontsize=10)

plt.tight_layout()
plt.savefig('pulse_wave.png', dpi=300, bbox_inches='tight')
print(f"График сохранен как 'pulse_wave.png'")
plt.show()

# Дополнительная информация
print(f"\nИспользован файл: {input_file}")
print(f"Среднее давление: {pressure_smooth.mean():.1f} мм рт ст")
print(f"Систолическое (макс): {pressure_smooth.max():.1f} мм рт ст")
print(f"Диастолическое (мин): {pressure_smooth.min():.1f} мм рт ст")
print(f"Пульсовое давление: {pressure_smooth.max() - pressure_smooth.min():.1f} мм рт ст")
