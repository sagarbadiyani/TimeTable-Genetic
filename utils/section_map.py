from config.cfg import course_list_all
from utils.time_slot import get_time
from config import cfg


def create_section_map():
    for idx, row in cfg.course_section_capacity_df.iterrows():
        course_name = row['Course'] + " " + row['Section'][0]
        if course_name in course_list_all:
            section_name = row['Course'] + " " + row['Section']
            timing = get_time(row['Course'], row['Section'])
            cfg.section_time_map[section_name] = timing
