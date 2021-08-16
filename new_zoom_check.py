import re
import report_creator

def create_list_from_table(input_data):
    output_list = []

    for i in input_data:
        #print(("." in i))
        if re.search('\d+', i) and ("." in i):
            output_list.append(i)

    return output_list


def find_new_zoom(table_list, folder_list):

    res_list = []

    for i in folder_list:
        if not report_creator.arrayInStr(table_list, i):
            #print(i)
            res_list.append(i)

    return res_list


