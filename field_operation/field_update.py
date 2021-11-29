import copy
from config import cfg

from config.cfg import course_list_all, course_list_pure_eg, course_list_pure_ws, course_list_eg, course_list_ws


def _get_updated_indices_list(arr):
    updated_eg_course_list = []
    updated_eg_course_indices_list = []
    updated_ws_course_list = []
    updated_ws_course_indices_list = []

    for i in arr:
        course = course_list_all[i]
        if course not in course_list_pure_ws:
            updated_eg_course_list.append(course)
            updated_eg_course_indices_list.append(i)
        if course not in course_list_pure_eg:
            updated_ws_course_list.append(course)
            updated_ws_course_indices_list.append(i)

    return updated_eg_course_list, updated_eg_course_indices_list, updated_ws_course_list, updated_ws_course_indices_list


def get_updated_field_from_permutation(arr):
    updated_eg_course_list, updated_eg_course_indices_list, updated_ws_course_list, updated_ws_course_indices_list = _get_updated_indices_list(arr)

    copied_field_eg = copy.deepcopy(cfg.field_eg)
    copied_field_ws = copy.deepcopy(cfg.field_ws)
    updated_field_eg = copy.deepcopy(cfg.field_eg)
    updated_field_ws = copy.deepcopy(cfg.field_ws)

    for idx, course in enumerate(updated_eg_course_list):
        index = course_list_eg.index(course)
        blob = copied_field_eg[index]
        updated_field_eg[idx] = copy.deepcopy(blob)

    for idx, course in enumerate(updated_ws_course_list):
        index = course_list_ws.index(course)
        blob = copied_field_ws[index]
        updated_field_ws[idx] = copy.deepcopy(blob)

    return {
        "course_list_eg": updated_eg_course_list,
        "course_list_ws": updated_ws_course_list,
        "field_eg": updated_field_eg,
        "field_ws": updated_field_ws,
        "permutation": arr
    }


def make_blobs_same_for_common_courses(field_eg, field_ws, permutation):
    common_course_blob_indices = [i for i in range(len(cfg.course_list_common))]
    _, eg_course_indices_list, _, ws_course_indices_list = _get_updated_indices_list(permutation)

    for index in common_course_blob_indices:
        index_in_ws = ws_course_indices_list.index(index)
        index_in_eg = eg_course_indices_list.index(index)
        field_ws[index_in_ws] = copy.deepcopy(field_eg[index_in_eg])
