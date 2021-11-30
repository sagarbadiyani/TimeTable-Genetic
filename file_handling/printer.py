import pandas as pd
from combinations_generator import computation_wrapper
from field_operation import field_update
from matplotlib import pyplot as plt


def print_results(generations, path):
    updated_fields = field_update.get_updated_field_from_permutation(path.arr)
    results = computation_wrapper.get_results(updated_fields)
    print_combination(results.get('paths_eg'), results.get('capacity_array_eg'),
                      results.get('paths_ws'), results.get('capacity_array_ws'),
                      path)
    print_graph(generations)


def print_graph(generations):
    plt.plot(generations, 'blue')
    plt.xlabel("Generations")
    plt.ylabel("Cost")
    plt.legend(['Standard'])
    plt.title('Genetic Algorithm')
    plt.savefig('./results/genetic_algorithm_results/graph.png')


def print_combination(paths_eg, capacity_array_eg, paths_ws, capacity_array_ws, path):
    print(f'The best path is {path.arr} and its fitness is {path.fitness}')
    print_combination_helper(data=paths_eg, capacity=capacity_array_eg,
                             filename="./results/combinations/EG_Combinations.xlsx")
    print_combination_helper(data=paths_ws, capacity=capacity_array_ws,
                             filename="./results/combinations/WS_Combinations.xlsx")


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
