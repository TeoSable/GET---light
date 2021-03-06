import lightFunctions as j
import matplotlib.pyplot as plt
import numpy as np
from cycler import cycler

# Преобразуем фотографии в векторы интенсивностей и строим на них графики с помощью функции из lightFunctions.py

intensity = []
intensity.append(j.readIntensity("white-mercury.png", "white-mercury.png", "Ртутная лампа", "белый лист"))
print(intensity[0])

colorRu = ["белый", "красный", "жёлтый", "зелёный", "синий"]
colorEn = ["white", "red", "yellow", "green", "blue"]

for i in range(5):
    intensity.append(j.readIntensity(colorEn[i] + "-tungsten.png", colorEn[i] + "-tungsten.png", "Лампа накаливания", colorRu[i] + " лист"))
    print(intensity[i + 1])

# Удаляем вектор интенсивностей ртутной лампы, т.к. он больше не понадобится
intensity.pop(0)

# Строим график зависимости отражённой интенсивности от длины волны излучения

plt.rc('axes', prop_cycle = (cycler('color', ['w', 'r', 'y', 'g', 'b'])))
fig = plt.figure()

plt.title('Отражённая интенсивность\n излучения лампы накаливания')
plt.xlabel('Длина волны излучения, нм')
plt.ylabel('Яркость')

plt.gca().set(facecolor = 'gray')    
plt.minorticks_on()
plt.grid(which = 'major')
plt.grid(which = 'minor', linestyle = '--')

# Зависимость длины волны от относительного номера пикселя: l = 380 + 0.55 * N 
waveLength = np.arange(380, 682.5, 0.55)

labels = ['Белый лист', 'Красный лист', 'Жёлтый лист', 'Зелёный лист', 'Синий лист']
for i in range(5):
    plt.plot(waveLength, intensity[i], label = labels[i])

plt.legend()
    
plt.savefig('intensities.png')

# Строим график альбедо поверхностей

plt.rc('axes', prop_cycle = (cycler('color', ['w', 'r', 'y', 'g', 'b'])))
fig = plt.figure()

plt.title('Альбедо поверхностей')
plt.xlabel('Длина волны излучения, нм')
plt.ylabel('Альбедо')

plt.gca().set(facecolor = 'gray')    
plt.minorticks_on()
plt.grid(which = 'major')
plt.grid(which = 'minor', linestyle = '--')


waveLength = np.arange(380, 682.5, 0.55)

# Рассчитываем значения альбедо с учётом, что они не могут быть больше 1, а при малых значениях интенсивности необходимо делать поправку на погрешность
albedo = []
albedo.append(np.linspace(1, 1, 550))
for k in range(1, 5):
    albedo1 = []
    for i in range(550):
        if intensity[0][i] < 0.25:
            albedo1.append(intensity[k][i] / (intensity[0][i] + 0.5))
        elif intensity[0][i] <= intensity[k][i]:
            albedo1.append(1)
        else:
            albedo1.append(intensity[k][i] / intensity[0][i])
    albedo.append(albedo1)

for i in range(5):
    plt.plot(waveLength, albedo[i], label = labels[i])

plt.legend()
    
plt.savefig('albedos.png')