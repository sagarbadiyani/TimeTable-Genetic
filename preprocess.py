import cfg

from file_handling.section_capacity_parser import get_course_section_capacity_df
from file_handling.tt_data_parser import get_parsed_tt_df
from utils.section_map import create_section_map


def preprocess():
    cfg.course_section_capacity_df = get_course_section_capacity_df()
    cfg.tt_parsed_df = get_parsed_tt_df()
    create_section_map()
