from preprocessing.preprocess import preprocess
from field_operation.field_update import get_updated_field
from fitness.fitness import get_fitness


def main():
    preprocess()
    arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    updated_fields = get_updated_field(arr)
    fitness = get_fitness(updated_fields)


if __name__ == "__main__":
    main()
