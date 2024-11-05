FILEPATH = "to_do_list.txt"


def get_to_do_list(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        to_do_list_local = file_local.readlines()
    return to_do_list_local

def write_to_do_list(to_do_list_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
            file.writelines(to_do_list_arg)