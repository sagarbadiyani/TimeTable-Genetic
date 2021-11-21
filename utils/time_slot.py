from cfg import tt_parsed_df
from cfg import Slot


def get_time(course, section):
    lst = []
    for idx, row in tt_parsed_df.iterrows():
        if row['Course'] == course and row['Section'] == section:
            st = int(row['Start'][0:2])
            en = int(row['End'][0:2])

            if en - st == 1:
                lst += [Slot(row['Day'], st)]

            elif en - st == 2:
                lst += [Slot(row['Day'], st), Slot(row['Day'], st + 1)]

            elif en - st == 3:
                lst += [Slot(row['Day'], st), Slot(row['Day'], st + 1), Slot(row['Day'], st + 2)]

    return lst
