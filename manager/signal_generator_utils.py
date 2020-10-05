from typing import List

from model.signal_generator import SignalGenerator


def sort_by_memory_capacity_desc(signal_generators: List[SignalGenerator]) -> List[SignalGenerator]:
    pass


def sort_by_signal_frequency_asc(signal_generators: List[SignalGenerator]) -> List[SignalGenerator]:
    pass


def bubble_sort(list_to_sort: list, ascending: bool = True) -> list:
    list_length = len(list_to_sort)
    comparison_count = 0
    swap_count = 0
    for i in range(0, list_length - 1):
        for j in range(0, list_length - 1 - i):
            comparison_count += 1
            if (ascending and list_to_sort[j] > list_to_sort[j + 1]) \
                    or (not ascending and list_to_sort[j] < list_to_sort[j+1]):
                swap_count += 1
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j+1], list_to_sort[j]
    print(f"[Bubble Sort] Comparisons: {comparison_count}, swaps: {swap_count}")
    return list_to_sort


def heapify(list_to_sort, end, root_index, ascending=True):
    left_index = root_index * 2 + 1
    right_index = root_index * 2 + 2
    new_root_index = root_index

    if left_index < end \
            and (
            (ascending and list_to_sort[new_root_index] < list_to_sort[left_index])
                 or (not ascending and list_to_sort[left_index] < list_to_sort[new_root_index])):
        new_root_index = left_index

    if right_index < end \
            and (
            (ascending and list_to_sort[new_root_index] < list_to_sort[right_index])
                 or (not ascending and list_to_sort[right_index] < list_to_sort[new_root_index])):
        new_root_index = right_index

    if new_root_index != root_index:
        list_to_sort[new_root_index], list_to_sort[root_index] = list_to_sort[root_index], list_to_sort[new_root_index]
        heapify(list_to_sort, end, new_root_index, ascending)


def heap_sort(list_to_sort: list, ascending: bool = True) -> list:
    end = len(list_to_sort)
    start_index = end // 2 - 1
    swap_count = 0

    for current_index in range(start_index, -1, -1):
        heapify(list_to_sort, end, current_index, ascending)
    for current_index in range(end - 1, 0, -1):
        swap_count += 1
        list_to_sort[current_index], list_to_sort[0] = list_to_sort[0], list_to_sort[current_index]
        heapify(list_to_sort, current_index, 0, ascending)

    return list_to_sort
