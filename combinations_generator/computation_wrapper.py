from combinations_generator.combinations_generator import generate_combinations


def get_results(updated_fields):
    field_eg, field_ws = updated_fields.get('field_eg'), updated_fields.get('field_ws')
    permutation = updated_fields.get('permutation')
    result = generate_combinations(field_eg, field_ws, permutation)
    return result
