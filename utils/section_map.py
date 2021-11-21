from cfg import course_section_capacity_df
from cfg import course_list_all
from utils.time_slot import get_time
import cfg


def create_section_map():
    for idx, row in course_section_capacity_df.iterrows():
        course_name = row['Course'] + " " + row['Section'][0]
        if course_name in course_list_all:
            section_name = row['Course'] + " " + row['Section']
            timing = get_time(row['Course'], row['Section'])
            cfg.section_time_map[section_name] = timing
