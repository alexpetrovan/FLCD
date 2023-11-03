import re


def read_lines(file):
    """
    Reads lines from a file and returns a list of strings, removing leading and trailing whitespaces.

    :param file: The path to the input file.
    :return: A list of strings containing the lines from the file.
    """
    result = []
    try:
        with open(file, "r", encoding="utf-8") as opened_file:
            for line in opened_file:
                result.append(line.strip())
    except FileNotFoundError:
        print(f"File {file} was not found !")
    except Exception as e:
        print(f"An error has occurred - {e}")
    return result


def read_tokens(file):
    """
    Reads tokens from a file and returns them as a dictionary where tokens are keys, and values are set to True.

    :param file: The path to the input file containing tokens.
    :return: A dictionary containing tokens as keys.
    """
    result = {}
    try:
        with open(file, "r", encoding="utf-8") as opened_file:
            for line in opened_file:
                result[line.strip("\n")] = True
    except FileNotFoundError:
        print(f"File {file} was not found !")
    except Exception as e:
        print(f"An error has occurred - {e}")
    return result


def read_program(file):
    """
    Reads a program from a file and returns a list of tokens extracted from lines starting with "prg".

    :param file: The path to the input file containing the program.
    :return: A list of tokens extracted from the program lines.
    """
    program = read_lines(file)
    while program and "prg" not in program[0]:
        program.pop(0)
    result_list = []
    [result_list.extend(element.split()) for element in program]
    return result_list


def split_with_separators(input_string, separators):
    """
    Splits an input string into tokens using specified separators and returns a list of tokens.

    :param input_string: The input string to be split.
    :param separators: A list of separator strings.
    :return: A list of tokens obtained by splitting the input string.
    """
    pattern = f'({"|".join(re.escape(separator) for separator in separators)})'
    return [part.strip() for part in re.split(pattern, input_string) if part]


def valid_identifier(input_string):
    """
    Validates if the input string is a valid identifier, constant number, or string.

    :param input_string: The input string to be validated.
    :return: True if the input string is a valid identifier, constant, or string, False otherwise.
    """
    id_pattern = r'^[a-zA-Z][a-zA-Z0-9]*$'
    const_pattern = r'^-?\d+$'
    string_pattern = r'^"([^"]+)"$'
    return bool(re.search(id_pattern, input_string) or re.search(const_pattern, input_string) or re.search(string_pattern, input_string))


if __name__ == "__main__":
    str = "in(a);"
    print(split_with_separators(str, ["(", ")", ";"]))
