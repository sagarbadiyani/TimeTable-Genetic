def generate_combinations(field_eg, field_ws):
    capacity_array_eg, capacity_array_ws, paths_eg, paths_ws = [], [], [], []
    number_of_courses_eg, number_of_courses_ws = len(field_eg), len(field_ws)
    generate_combinations_eg(field_eg, capacity_array_eg, paths_eg, number_of_courses_eg)
    generate_combinations_ws(field_ws, capacity_array_ws, paths_ws, number_of_courses_ws)


def generate_combinations_eg(field_eg, capacity_array_eg, paths_eg, number_of_courses_eg):
    create_list(field_eg, capacity_array_eg, paths_eg, number_of_courses_eg)


def generate_combinations_ws(field_ws, capacity_array_ws, paths_ws, number_of_courses_ws):
    create_list(field_ws, capacity_array_ws, paths_ws, number_of_courses_ws)


def create_list(field, capacity_array, paths, number_of_courses):
    pass
