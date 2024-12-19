# TODO Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.
def sort_list_imperarive(numbers):
    for i in range(len(numbers) - 1):
        for j in range(i, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]


if __name__ == '__main__':
    numbers = [8, 4, 2, 7, 4, 6, 8, 1, 2]
    sort_list_imperarive(numbers)
    print(numbers)
