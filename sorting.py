import random
import matplotlib.pyplot as plt

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

def bubble_sort(numbers):
    numbers = numbers.copy()
    delka = len(numbers)

    plt.ion()
    plt.show()

    for i in range(delka):
        for j in range(0, delka - i - 1):
            index_highlight1 = j
            index_highlight2 = j + 1
            colors = ["steelblue"] * len(numbers)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(numbers)), numbers, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)

            if numbers  [j] > numbers[j+1]:
                numbers[j], numbers [j+1] = numbers [j+1], numbers[j]

    plt.ioff()
    plt.show()

    return numbers


if __name__ == "__main__":
    values = random_numbers(10)  # 10 čísel v rozsahu 0–100
    numbers = random_numbers(20)
   # print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]
    selection_sort(values)
    bubble_sort(numbers)
