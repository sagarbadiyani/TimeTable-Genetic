from field_operation import field_update
from combinations_generator import computation_wrapper


class FieldState:
    def __init__(self, arr):
        self.arr = arr
        self.fitness = self.get_fitness_score()

    def get_fitness_score(self):
        updated_fields = field_update.get_updated_field_from_permutation(self.arr)
        fitness_score = computation_wrapper.get_results(updated_fields).get('number_of_students_allotted')
        return fitness_score
