from typing import List

from model.signal_generator import SignalGenerator


def sort_by_memory_capacity_desc(signal_generators: List[SignalGenerator]) -> List[SignalGenerator]:
    pass


def sort_by_signal_frequency_asc(signal_generators: List[SignalGenerator]) -> List[SignalGenerator]:
    pass


def swap(first_val, second_val):
    first_val, second_val = second_val, first_val


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
                list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j]
    print(f"[Bubble Sort] Comparisons: {comparison_count}, swaps: {swap_count}")
    return list_to_sort
