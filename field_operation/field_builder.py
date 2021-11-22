from config import cfg
from utils.time_slot import get_time
from config.cfg import Section


def build_field(field, course_list):
    for idx, row in cfg.course_section_capacity_df.iterrows():
        course_name_type = row['Course'] + " " + row['Section'][0]
        section_name = row['Course'] + " " + row['Section']
        if course_name_type in course_list:
            index = course_list.index(course_name_type)
            section = Section(section_name, int(row['Capacity']), get_time(row['Course'], row['Section']))
            field[index].append(section)
    return field[:len(course_list)]


def build_eg_field():
    cfg.field_eg = build_field(cfg.field_eg, cfg.course_list_eg)


def build_ws_field():
    cfg.field_ws = build_field(cfg.field_ws, cfg.course_list_ws)
