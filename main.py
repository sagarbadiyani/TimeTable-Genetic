from genetic import genetic_algorithm
from preprocessing.preprocess import preprocess


def main():
    preprocess()
    genetic_algorithm.start()


if __name__ == "__main__":
    main()
