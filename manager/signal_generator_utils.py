from typing import List
from model.signal_generator import SignalGenerator

swap_count = 0
comparison_count = 0


def sort_by_memory_capacity_desc(signal_generators: List[SignalGenerator]) -> List[SignalGenerator]:
    pass


def sort_by_signal_frequency_asc(signal_generators: List[SignalGenerator]) -> List[SignalGenerator]:
    pass


def bubble_sort(list_to_sort: list, key=None, ascending: bool = True) -> list:
    global swap_count
    global comparison_count
    swap_count = 0
    comparison_count = 0
    if key is None:
        key = lambda x: x

    list_length = len(list_to_sort)
    for i in range(0, list_length - 1):
        for j in range(0, list_length - 1 - i):
            comparison_count += 1
            if (ascending and key(list_to_sort[j]) > key(list_to_sort[j + 1])) \
                    or (not ascending and key(list_to_sort[j]) < key(list_to_sort[j+1])):
                swap_count += 1
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j+1], list_to_sort[j]
    print(f"[Bubble Sort] Comparisons: {comparison_count}, swaps: {swap_count}")
    return list_to_sort


def heapify(list_to_sort, end, root_index, key, ascending):
    global swap_count
    global comparison_count

    left_index = root_index * 2 + 1
    right_index = root_index * 2 + 2
    new_root_index = root_index

    comparison_count += 3
    if left_index < end \
            and (
            (ascending and key(list_to_sort[new_root_index]) < key(list_to_sort[left_index]))
                 or (not ascending and key(list_to_sort[left_index]) < key(list_to_sort[new_root_index]))):
        new_root_index = left_index

    if right_index < end \
            and (
            (ascending and key(list_to_sort[new_root_index]) < key(list_to_sort[right_index]))
                 or (not ascending and key(list_to_sort[right_index]) < key(list_to_sort[new_root_index]))):
        new_root_index = right_index

    if new_root_index != root_index:
        swap_count += 1
        list_to_sort[new_root_index], list_to_sort[root_index] = list_to_sort[root_index], list_to_sort[new_root_index]
        heapify(list_to_sort, end, new_root_index, ascending)


def heap_sort(list_to_sort: list, key=None, ascending: bool = True) -> list:
    global swap_count
    global comparison_count
    swap_count = 0
    comparison_count = 0
    if key is None:
        key = lambda x: x

    end = len(list_to_sort)
    start_index = end // 2 - 1

    for current_index in range(start_index, -1, -1):
        heapify(list_to_sort, end, current_index, key, ascending)
    for current_index in range(end - 1, 0, -1):
        swap_count += 1
        list_to_sort[current_index], list_to_sort[0] = list_to_sort[0], list_to_sort[current_index]
        heapify(list_to_sort, current_index, 0, key, ascending)

    print(f"[Heap Sort] Comparisons: {comparison_count}, swaps: {swap_count}")
    return list_to_sort
