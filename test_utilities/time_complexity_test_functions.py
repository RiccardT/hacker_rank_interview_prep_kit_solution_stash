import time


def process_test_file_where_lines_are_int_arrays(test_file_path: str, exclude_index: int = -1) -> list:
    processed_data: list = []

    with open(test_file_path, "r") as f:
        for index, line in enumerate(f):
            if index > exclude_index:
                line = convert_line_into_integer_list(line)
                processed_data.append(line)

    if len(processed_data) == 1:
        lines = processed_data[0]

    return processed_data


def process_test_file_where_lines_are_str_arrays(test_file_path: str, exclude_index: int = -1) -> list:
    processed_data: list = []

    with open(test_file_path, "r") as f:
        for index, line in enumerate(f):
            if index > exclude_index:
                line = convert_line_into_str_list(line)
                processed_data.append(line)

    if len(processed_data) == 1:
        lines = processed_data[0]

    return processed_data


def process_test_file_where_lines_are_int_elements(test_file_path: str, exclude_index: int = -1) -> list:
    processed_data: list = []

    with open(test_file_path, "r") as f:
        for index, line in enumerate(f):
            if index > exclude_index:
                processed_line = convert_line_into_int(line)
                processed_data.append(processed_line)

    if len(processed_data) == 1:
        processed_data = processed_data[0]

    return processed_data


def process_test_file_where_lines_are_str_elements(test_file_path: str, exclude_index: int = -1) -> list:
    processed_data: list = []

    with open(test_file_path, "r") as f:
        for index, line in enumerate(f):
            if index > exclude_index:
                processed_line = convert_line_into_str(line)
                processed_data.append(processed_line)

    if len(processed_data) == 1:
        processed_data = processed_data[0]

    return processed_data


def get_console_time_logged_result_of(function, *function_args):
    tic = time.perf_counter()
    actual: int = function(*function_args)
    tock = time.perf_counter()
    time_log = f'\n{function.__name__}() finished in {tock - tic:0.10f} seconds'
    print(time_log)
    return actual


def convert_line_into_integer_list(line: str) -> list:
    line = line.strip("\n")
    line = line.split(" ")
    line = [int(element) for element in line]
    return line


def convert_line_into_str_list(line: str) -> list:
    line = line.strip("\n")
    line = line.split(" ")
    return line


def convert_line_into_int(line: str) -> int:
    line = line.strip("\n")
    return int(line)


def convert_line_into_str(line: str) -> str:
    line = line.strip("\n")
    return line