import cfg

from file_handling.section_capacity_parser import get_course_section_capacity_df
from file_handling.tt_data_parser import get_parsed_tt_df


def main():
    cfg.course_section_capacity_df = get_course_section_capacity_df()
    cfg.tt_parsed_df = get_parsed_tt_df()


if __name__ == "__main__":
    main()
