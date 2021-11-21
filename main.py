import cfg

from file_handling.section_capacity_input import get_course_section_capacity_df


def main():
    cfg.course_section_capacity_df = get_course_section_capacity_df()


if __name__ == "__main__":
    main()
