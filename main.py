import csv
from manager import signal_generator_utils
from model.signal_generator import SignalGenerator

if __name__ == '__main__':

    signal_generators = []
    with open('input.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            signal_generators.append(SignalGenerator(int(row[0]), int(row[1]), row[2]))

    print("Signal generators sorted by frequency ascending:")
    print(signal_generator_utils.sort_by_signal_frequency_asc(signal_generators))
    print("\n-------------------\n")
    print("Signal generators sorted by memory descending:")
    print(signal_generator_utils.sort_by_memory_capacity_desc(signal_generators))
