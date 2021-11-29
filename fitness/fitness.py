from combinations_generator import combinations_generator


def get_fitness(updated_fields):
    field_eg, field_ws = updated_fields.get('field_eg'), updated_fields.get('field_ws')
    permutation = updated_fields.get('permutation')
    result = combinations_generator.generate_combinations(field_eg, field_ws, permutation)
    print(result.get('capacity_array_eg'))
    print(result.get('capacity_array_ws'))
    print(result.get('number_of_students_allotted'))
