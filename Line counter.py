def main():
    print(count_lines_in_file("x3.py"))
    # print format

def count_lines_in_file(file_name):
    file_object = open(file_name, 'r')
    lines = file_object.readlines()
    file_object.close()
    number_of_lines = len(lines)
    return number_of_lines


def count_nonblank_in_file(file_name):
    number_of_lines = 0
    file_object = open(file_name, 'r')
    for line in file_object:
        line = line.strip()
        if line != '':
            number_of_lines += 1
    file_object.close()
    number_of_lines = len(lines)
    return number_of_lines


main()
