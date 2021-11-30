from file_handling import printer
from genetic import genetic_algorithm
from preprocessing.preprocess import preprocess


def main():
    preprocess()
    generations, path = genetic_algorithm.start(epochs=5)
    printer.print_results(generations, path)


if __name__ == "__main__":
    main()
