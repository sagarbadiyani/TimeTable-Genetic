import pandas as pd


def get_course_section_capacity_df():
    course_section_capacity_df = pd.DataFrame()
    df = pd.read_excel('../data/first.xlsx')
    for index, row in df.iterrows():
        temp = row['COURSE SEC'].split(' ')
        temp_row = {'Course': temp[0] + ' ' + temp[1], 'Section': temp[2], 'Capacity': row['TOT SEC CAP']}
        course_section_capacity_df.append(temp_row, ignore_index=True)

    return course_section_capacity_df
