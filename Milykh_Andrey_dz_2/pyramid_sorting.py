#
# Пирамидальная сортировка
#


def heapify(array: list, heap_size: int, root_index: int):
    largest = root_index  # инициализируем наибольший элемент как корень
    left_child = 2 * root_index + 1  # левый = 2*root_index + 1
    right_child = 2 * root_index + 2  # правый = 2*root_index + 2

    # Если левый дочерний элемент больше корня
    if left_child < heap_size and array[left_child] > array[largest]:
        largest = left_child

    # Если правый дочерний элемент больше, чем самый большой
    # элемент на данный момент
    if right_child < heap_size and array[right_child] > array[largest]:
        largest = right_child
    # Если самый большой элемент не корень
    if largest != root_index:
        temp = array[root_index]
        array[root_index] = array[largest]
        array[largest] = temp

        # Рекурсивно преобразуем в двоичную кучу затронутое поддерево
        heapify(array, heap_size, largest)


def heap_sort(array: list):
    # Построение кучи (перегруппируем массив)
    start_index = len(array) // 2 - 1  # середина массива, которая будт корнем
    stop_index = -1
    step = -1
    for i in range(start_index, stop_index, step):
        heapify(array, len(array), i)  # запускаем просеивание от середины
        # до самого начала
    # Самый большой элемент окажентся на нулевой позиции

    # Один за другим извлекаем элементы из кучи (с конца до начала)
    start_index = len(array) - 1
    stop_index = -1
    step = -1
    for i in range(start_index,  stop_index, step):
        # Перемещаем текущий корень в конец
        temp = array[0]
        array[0] = array[i]
        array[i] = temp

        # Вызываем процедуру heapify на уменьшеной куче
        heapify(array, i, 0)


mas = [4, 2, 5, 8, 1, 9, 3, 6, 7, 0]
print(mas)
heap_sort(mas)
print(mas)
mas = [4, 16, 2, 9, 19, 5, 13, 8, 21, 1, 9, 4, 3, 6, 7, 0, 17, 30]
print(mas)
heap_sort(mas)
print(mas)
