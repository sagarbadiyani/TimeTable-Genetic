import time

from field_operation import field_update
from fitness import fitness


class FieldState:
    def __init__(self, arr):
        self.arr = arr
        self.fitness = self.get_fitness()

    def get_fitness(self):
        updated_fields = field_update.get_updated_field_from_permutation(self.arr)
        fitness_score = fitness.get_fitness(updated_fields)
        return fitness_score
