from preprocessing.preprocess import preprocess
from field_operation.field_update import get_updated_field_from_permutation
from fitness.fitness import get_fitness


def main():
    preprocess()
    arr = [i for i in range(16)]
    updated_fields = get_updated_field_from_permutation(arr)
    fitness = get_fitness(updated_fields)


if __name__ == "__main__":
    main()
