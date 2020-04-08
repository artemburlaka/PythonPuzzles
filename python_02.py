import os.path


def path_to_file():
    path = input("Please enter a path to a file:\n\t")
    if os.path.isfile(path):
        statistic_from_file(path)
    else:
        print("The path is uncorrected!")
        path_to_file()
    if one_more():
        path_to_file()
    return True


def one_more():
    answer_one_more = input("Would you like to analyze one more file? (y/n)\n\t")
    if answer_one_more == "y":
        return True
    elif answer_one_more == "n":
        print("Program has been stopped")
        return False
    else:
        return one_more()


def statistic_from_file(file):
    opened_file = open(file, "r")
    dict_for_statistic = {"num_lines": 0, "empty_lines": 0}
    for line in opened_file:
        dict_for_statistic["num_lines"] += 1
        if line in ['\n', '\r\n']:
            dict_for_statistic["empty_lines"] += 1

    print_statistic(**dict_for_statistic)


def print_statistic(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))
    # print(dict_for_statistic["num_lines"])
    # print(dict_for_statistic["empty_lines"])


if __name__ == '__main__':
    path_to_file()



