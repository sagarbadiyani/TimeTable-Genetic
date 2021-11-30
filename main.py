import time

from file_handling import printer
from genetic import genetic_algorithm
from preprocessing.preprocess import preprocess


def main():
    start_time = time.time()
    preprocess()
    generations, path = genetic_algorithm.start(epochs=500)
    printer.print_results(generations, path)
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time} seconds")


if __name__ == "__main__":
    main()
