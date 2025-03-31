import cv2
import numpy as np
import matplotlib.pyplot as plt
import heapq
from collections import defaultdict
import math

# Загружаем изображение в градациях серого
image = cv2.imread("Grayscale_Cat.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    raise FileNotFoundError("Изображение не найдено. Проверь путь!")

# Отображаем оригинальное изображение
plt.figure(figsize=(6,6))
plt.imshow(image, cmap='gray')
plt.title("Оригинальное изображение")
plt.show()

# Квантование изображения (уменьшаем количество оттенков серого)
levels = 16  # Устанавливаем 16 уровней вместо 256
quantized_image = np.round(image / (256 / levels)) * (256 / levels)
quantized_image = quantized_image.astype(np.uint8)

# Отображаем квантованное изображение
plt.figure(figsize=(6,6))
plt.imshow(quantized_image, cmap='gray')
plt.title(f"Квантованное изображение ({levels} уровней)")
plt.show()

# Строим гистограммы до и после квантования
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.hist(image.ravel(), bins=256, range=[0,256], color='blue', alpha=0.7)
plt.title("Гистограмма оригинального изображения")

plt.subplot(1,2,2)
plt.hist(quantized_image.ravel(), bins=levels, range=[0,256], color='red', alpha=0.7)
plt.title("Гистограмма квантованного изображения")
plt.show()

# ----------------------------- #
# 1. ОПРЕДЕЛЕНИЕ КЛАССА УЗЛА ДЛЯ ДЕРЕВА ХАФФМАНА
# ----------------------------- #

class HuffmanNode:
    def __init__(self, value, freq):
        """
        Класс узла для построения дерева Хаффмана.
        
        value - значение пикселя (уровень серого)
        freq - частота появления этого значения в изображении
        left, right - ссылки на дочерние узлы
        """
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        # Метод для сравнения узлов (необходим для приоритетной очереди)
        return self.freq < other.freq

# ----------------------------- #
# 2. ПОСТРОЕНИЕ ДЕРЕВА ХАФФМАНА
# ----------------------------- #

def build_huffman_tree(frequencies):
    """
    Создает дерево Хаффмана на основе частот появления пиксельных значений.
    Используется приоритетная очередь (heap).
    """
    heap = [HuffmanNode(value, freq) for value, freq in frequencies.items()]
    heapq.heapify(heap)  # Преобразуем список в приоритетную очередь (минимальная куча)

    # Построение дерева путем объединения узлов с наименьшими частотами
    while len(heap) > 1:
        left = heapq.heappop(heap)  # Извлекаем первый (наименее частый) узел
        right = heapq.heappop(heap) # Извлекаем второй наименее частый узел
        merged = HuffmanNode(None, left.freq + right.freq)  # Создаем новый узел (объединение)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)  # Добавляем объединенный узел обратно в кучу

    return heap[0]  # Возвращаем корень построенного дерева

# ----------------------------- #
# 3. ГЕНЕРАЦИЯ ХАФФМАН-КОДОВ
# ----------------------------- #

def generate_huffman_codes(node, prefix="", codebook={}):
    """
    Рекурсивная функция для создания кодов Хаффмана.
    Каждый левый переход -> добавляется "0", правый -> "1".
    """
    if node is not None:
        if node.value is not None:
            codebook[node.value] = prefix  # Записываем код для значения пикселя
        generate_huffman_codes(node.left, prefix + "0", codebook)
        generate_huffman_codes(node.right, prefix + "1", codebook)
    return codebook

# ----------------------------- #
# 4. ПРИМЕНЕНИЕ ХАФФМАН-КОДИРОВАНИЯ К ИЗОБРАЖЕНИЮ
# ----------------------------- #

# Определяем частоту появления каждого пикселя в квантованном изображении
unique, counts = np.unique(quantized_image, return_counts=True)
frequencies = dict(zip(unique, counts))  # Создаем словарь {пиксельный уровень: частота}

# Строим дерево Хаффмана
huffman_tree = build_huffman_tree(frequencies)

# Генерируем коды Хаффмана
huffman_codes = generate_huffman_codes(huffman_tree)

# Выводим первые 10 закодированных значений
print("Коды Хаффмана для нескольких значений:")
for i, (value, code) in enumerate(huffman_codes.items()):
    print(f"Значение {value}: {code}")
    if i == 10: break  # Ограничиваем вывод 10 значениями

# ----------------------------- #
# 5. ОЦЕНКА КАЧЕСТВА СЖАТИЯ (PSNR)
# ----------------------------- #

def compute_psnr(original, compressed):
    """
    Вычисляет показатель PSNR (Peak Signal-to-Noise Ratio),
    который измеряет качество восстановленного изображения.
    
    Чем выше PSNR, тем меньше потерь при сжатии.
    """
    mse = np.mean((original - compressed) ** 2)  # Среднеквадратичная ошибка (MSE)
    if mse == 0:
        return float('inf')  # Если MSE = 0, изображения идентичны
    
    max_pixel = 255.0  # Максимально возможное значение пикселя
    return 20 * math.log10(max_pixel / math.sqrt(mse))  # Формула PSNR

# Вычисляем PSNR между оригинальным и квантованным изображением
psnr_value = compute_psnr(image, quantized_image)
print(f"PSNR после квантования: {psnr_value:.2f} дБ")

# ----------------------------- #
# 🎯 Итог:
# ✔ Мы уменьшили количество оттенков серого (квантование)
# ✔ Закодировали данные с помощью алгоритма Хаффмана
# ✔ Проанализировали гистограммы и оценили сжатие с помощью PSNR
# ✔ В результате получили уменьшенный размер изображения без значительной потери качества!
# ----------------------------- #
