from preprocessing.preprocess import preprocess
from field_operation.field_update import get_updated_field_from_permutation
from fitness.fitness import get_fitness


def main():
    preprocess()
    arr = [15, 13, 12, 14, 11, 0, 6, 8, 7, 9, 5, 4, 3, 2, 1, 10]
    # arr[::-1]
    updated_fields = get_updated_field_from_permutation(arr)
    fitness = get_fitness(updated_fields)


if __name__ == "__main__":
    main()
