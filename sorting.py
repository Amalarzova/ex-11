import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]




def selection_sort(values):
    for j in range(len(values)):

        min_index = 0
        min_value = values[min_index]

        for i in range(j + 1, len(values)):
            if values[i] < min_value:
                min_index = j
                min_value = values[i]

        values[j], values[min_index] = values[min_index], values[j]
        print(values)

    return values


if __name__ == "__main__":
    values = random_numbers(10)  # 10 čísel v rozsahu 0–100
   # print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]
    selection_sort(values)

# import random
#
#
# def random_numbers(count):
#     return [random.randint(1, 100) for _ in range(count)]
#
#
# def selection_sort(seznam):
#     data = seznam.copy()
#     n = len(data)
#
#     for i in range(n):
#         min_idx = i
#         for j in range(i + 1, n):
#             if data[j] < data[min_idx]:
#                 min_idx = j
#
#
#         data[i], data[min_idx] = data[min_idx], data[i]
#
#     return data
#
#
# def main():
#
#     cisla = [5, 1, 4, 2, 8]
#     print("Původní:", cisla)
#     print("Seřazený:", selection_sort(cisla))
#
#
#     nahodna = random_numbers(20)
#     print("\nNáhodná čísla:", nahodna)
#     print("Seřazená náhodná:", selection_sort(nahodna))
#
#
# if __name__ == "__main__":
#     main()
#
#

