import pandas as pd
import cfg

df = pd.read_excel('../Data/first.xlsx')
for index, row in df.iterrows():
    temp = row['COURSE SEC'].split(' ')
    tempRow = {'Course': temp[0] + ' ' + temp[1], 'Section': temp[2], 'Capacity': row['TOT SEC CAP']}
    cfg.course_section_capacity_df = cfg.course_section_capacity_df.append(tempRow, ignore_index=True)
