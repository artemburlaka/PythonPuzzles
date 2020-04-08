import sys


def my_sum(a, b):
    res = int(a) + int(b)
    return res


def only_int(full_list):
    int_list = []
    for i in full_list:
        try:
            is_integer = int(i)
            int_list.append(is_integer)
        except ValueError:
            continue
    return int_list


def main(parameters):
    result = ""
    if parameters:
        int_list = only_int(parameters)
        if len(int_list) > 1:
            i = 0
            while i < len(int_list):
                if int_list[i] not in int_list[:i]:
                    j = i + 1
                    while j < len(int_list):
                        if int_list[j] not in int_list[j+1:]:
                            if my_sum(int_list[i], int_list[j]) == 10:
                                result = result + str(int_list[i]) + " + " + str(int_list[j]) + "\n"
                                break
                            else:
                                j += 1
                        else:
                            j += 1
                    i += 1
                else:
                    i += 1
        else:
            result = "Please enter more digits as parameters"
    else:
        result = "Please enter some digits as parameters"
    return result


if __name__ == '__main__':
    print(main(sys.argv[1:]))