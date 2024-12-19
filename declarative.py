# TODO Задача №2
# Написать точно такую же процедуру, но в декларативном стиле

def sort_list_imperarive(numbers):
    return sorted(numbers)


if __name__ == '__main__':
    numbers = [8, 4, 2, 7, 4, 6, 8, 1, 2]
    numbers = sort_list_imperarive(numbers)
    print(numbers)
