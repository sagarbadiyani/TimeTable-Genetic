from field_operation import field_update


def generate_combinations(field_eg, field_ws, permutation):
    capacity_array_eg, capacity_array_ws, paths_eg, paths_ws = [], [], [], []
    number_of_courses_eg, number_of_courses_ws = len(field_eg), len(field_ws)
    generate_combinations_eg(field_eg, capacity_array_eg, paths_eg, number_of_courses_eg)
    field_update.make_blobs_same_for_common_courses(field_eg, field_ws, permutation)
    generate_combinations_ws(field_ws, capacity_array_ws, paths_ws, number_of_courses_ws)
    return {
        'capacity_array_eg': capacity_array_eg,
        'capacity_array_ws': capacity_array_ws,
        'paths_eg': paths_eg,
        'paths_ws': paths_ws,
        'number_of_students_allotted': sum(capacity_array_eg) + sum(capacity_array_ws)
    }


def generate_combinations_eg(field_eg, capacity_array_eg, paths_eg, number_of_courses_eg):
    create_list(field_eg, capacity_array_eg, paths_eg, number_of_courses_eg)


def generate_combinations_ws(field_ws, capacity_array_ws, paths_ws, number_of_courses_ws):
    create_list(field_ws, capacity_array_ws, paths_ws, number_of_courses_ws)


def create_list(field, capacity_array, paths, number_of_courses):
    stop = True
    while stop:
        stop = rem_part(capacity_array, field, number_of_courses, paths)


def rem_part(capacity_array, field, number_of_courses, paths):
    path = []
    path_build_helper(field, 0, number_of_courses, path)
    if len(path) == 0:
        return False

    minimum_capacity_on_path = min([section.capacity for section in path])
    capacity_array.append(minimum_capacity_on_path)

    blob_index = 0
    for section in path:
        section.capacity -= minimum_capacity_on_path
        if section.capacity == 0:
            idx = field[blob_index].index(section)
            field[blob_index].pop(idx)
        blob_index += 1

    if len(path) > 0:
        paths.append(path)
        return True
    return False


def path_build_helper(field, blob_index, end, path):
    if blob_index == end:
        return is_valid_path(path)

    for sec in field[blob_index]:
        path.append(sec)
        is_valid = is_valid_path(path)
        if is_valid:
            stop = path_build_helper(field, blob_index + 1, end, path)
            if stop:
                return True
        path.pop()


def is_valid_path(path):
    clash_check = set()
    for section in path:
        timings = section.timing
        for time in timings:
            if str(time) in clash_check:
                return False
            clash_check.add(str(time))
    return True
