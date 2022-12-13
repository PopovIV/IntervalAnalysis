import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as opt
from scipy import stats as st
import numpy as np
import heapq
from matplotlib.patches import Rectangle

data1 = pd.read_csv('data/Channel_1_900nm_2mm.csv', sep=';', encoding='cp1251')
data2 = pd.read_csv('data/Channel_2_900nm_2mm.csv', sep=';', encoding='cp1251')

data1 = data1['мВ']
data2 = data2['мВ']

eps = 1e-4
plt.vlines(data1.index + 1, data1 - eps, data1 + eps, color = "steelblue")
plt.xlabel('n')
plt.ylabel('мВ')
plt.title('Исходные интервальные данные')
plt.savefig('data1_interval.png', dpi = 1000)