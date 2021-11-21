import pandas as pd
import math
from sortedcontainers import SortedSet


def get_parsed_tt_df():
    df = pd.read_excel('./data/output_Format1.xlsx')
    s = SortedSet()
    for index, row in df.iterrows():
        temp = {}

        # Check if First Year Course
        if row['Catalog'][1] != '1':
            continue
        row['Section'] = row['Section'][0:-2]
        temp['Course'] = row['Subject'] + ' ' + row['Catalog']
        temp['Section'] = row['Section']
        temp['Type'] = row['Section'][0]
        days = []
        flag = 0
        x = row['Class Pattern']
        if not isinstance(x, str):
            continue
        for i in range(len(x)):
            if x[i] == 'H':
                days[i - 1] = days[i - 1] + "H"
                flag = 1
            else:
                days.append("")
                days[i - flag] = x[i]
        for day in days:
            temp['Day'] = day
            temp['Start'] = row['Mtg Start']
            temp['End'] = row['End time']
            if isinstance(temp['Start'], float) and math.isnan(temp['Start']):
                continue
            else:
                x = temp
                temp_list = list(x.items())
                day = temp_list[-3]
                stime = temp_list[-2]
                etime = temp_list[-1]
                temp_list.remove(day)
                temp_list.remove(stime)
                temp_list.remove(etime)
                temp_list.insert(0, day)
                temp_list.insert(1, stime)
                temp_list.insert(2, etime)

                s.add(tuple(temp_list))

    lst = []
    for x in s:
        lst.append(dict(x))

    inp_df = pd.DataFrame(lst)
    return inp_df

