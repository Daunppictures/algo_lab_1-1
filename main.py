import csv
import sys
from manager import signal_generator_utils
from model.signal_generator import SignalGenerator

if __name__ == '__main__':
    input_file_path = ""
    try:
        input_file_path = sys.argv[1]
    except IndexError:
        print("[Error] Input file path not found")
        exit()

    signal_generators = []
    with open(input_file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            signal_generators.append(SignalGenerator(int(row[0]), int(row[1]), row[2]))

    print("Signal generators sorted by memory descending:")
    sorted_signal_generators_by_memory = signal_generator_utils.sort_by_memory_capacity_desc(signal_generators)
    for signal_generator in sorted_signal_generators_by_memory:
        print(signal_generator)
    print("\n-------------------\n")
    print("Signal generators sorted by frequency ascending:")
    sorted_signal_generators_by_frequency = signal_generator_utils.sort_by_signal_frequency_asc(signal_generators)
    for signal_generator in sorted_signal_generators_by_frequency:
        print(signal_generator)
