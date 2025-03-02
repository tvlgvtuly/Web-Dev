import cv2
import numpy as np
import matplotlib.pyplot as plt
import heapq
from collections import defaultdict
import math


image = cv2.imread("Grayscale_Cat.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    raise FileNotFoundError("Изображение не найдено. Проверь путь!")

plt.figure(figsize=(6,6))
plt.imshow(image, cmap='gray')
plt.title("Оригинальное изображение")
plt.show()


levels = 16  
quantized_image = np.round(image / (256 / levels)) * (256 / levels)
quantized_image = quantized_image.astype(np.uint8)

plt.figure(figsize=(6,6))
plt.imshow(quantized_image, cmap='gray')
plt.title(f"Квантованное изображение ({levels} уровней)")
plt.show()

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.hist(image.ravel(), bins=256, range=[0,256], color='blue', alpha=0.7)
plt.title("Гистограмма оригинального изображения")

plt.subplot(1,2,2)
plt.hist(quantized_image.ravel(), bins=levels, range=[0,256], color='red', alpha=0.7)
plt.title("Гистограмма квантованного изображения")
plt.show()

class HuffmanNode:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    heap = [HuffmanNode(value, freq) for value, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def generate_huffman_codes(node, prefix="", codebook={}):
    if node is not None:
        if node.value is not None:
            codebook[node.value] = prefix
        generate_huffman_codes(node.left, prefix + "0", codebook)
        generate_huffman_codes(node.right, prefix + "1", codebook)
    return codebook

unique, counts = np.unique(quantized_image, return_counts=True)
frequencies = dict(zip(unique, counts))

huffman_tree = build_huffman_tree(frequencies)
huffman_codes = generate_huffman_codes(huffman_tree)

print("Коды Хаффмана для нескольких значений:")
for i, (value, code) in enumerate(huffman_codes.items()):
    print(f"Значение {value}: {code}")
    if i == 10: break  

def compute_psnr(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if mse == 0:
        return float('inf')  
    max_pixel = 255.0
    return 20 * math.log10(max_pixel / math.sqrt(mse))

psnr_value = compute_psnr(image, quantized_image)
print(f"PSNR после квантования: {psnr_value:.2f} дБ")

