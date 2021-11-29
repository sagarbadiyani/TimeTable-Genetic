import pandas as pd


def print_combination(paths_eg, capacity_array_eg, paths_ws, capacity_array_ws):
    print_combination_helper(data=paths_eg, capacity=capacity_array_eg, filename="./data/out/EG_Combinations.xlsx")
    print_combination_helper(data=paths_ws, capacity=capacity_array_ws, filename="./data/out/WS_Combinations.xlsx")


def print_combination_helper(data, capacity, filename):
    header = get_header(data)
    export_to_excel(header, data, capacity, filename)


def get_header(data):
    header = ["Sr No.", "Capacity"]
    for d in data[0]:
        row_arr = d.name.split()
        header.append("{} {} {}".format(row_arr[0], row_arr[1], row_arr[2][0]))
    return header


def export_to_excel(header, data, capacity, filename):
    final_list = []
    for idx, path in enumerate(data):
        temp_arr = [idx+1, capacity[idx]]

        for section in path:
            section_string = section.name.split()
            temp_arr.append(section_string[2][1:])
        final_list.append(temp_arr)

    df = pd.DataFrame(final_list, columns=header)
    writer = pd.ExcelWriter(filename, engine='xlsxwriter')
    df.to_excel(writer, sheet_name="Sheet 1", index=False)
    writer.save()
