import os
from Lab2.SymbolTable import SymbolTable
from Lab3Scanner.program_internal_form import ProgramInternalForm
from Utils.utils import read_program, read_tokens, split_with_separators, valid_identifier


def write_results_to_file(filename, lst_of_strings):
    """
    Writes a list of strings to a file.

    :param filename: The name of the output file.
    :param list_of_strings: A list of strings to be written to the file.
    """
    file_name = filename.split("\\")[-1]
    with open(f"Output/out_{file_name}", "w") as write_file:
        for string in lst_of_strings:
            write_file.write(f"{string}\n\n")
    write_file.close()


class Scanner:
    def __init__(self):
        """
        Initializes a Scanner object with symbol tables, internal form, and lexeme dictionaries.
        """
        self.symbol_table = SymbolTable(size=200)
        self.program_internal_form = ProgramInternalForm()

        self.last_scanned_file = ""

        # Dictionaries to store lexemes for operators, separators, reserved words, and other tokens
        self.operators = {}
        self.separators = {}
        self.reserved_words = {}
        self.identifiers = {}
        self.lexic = {}

        # Load lexemes from token files
        self.__read_tokens()

    def get_program_internal_form(self):
        """
        Returns the Program Internal Form (PIF) object containing identifier-constant pairs.

        :return: Program Internal Form object.
        """
        return self.program_internal_form

    def get_symbol_table(self):
        """
        Returns the Symbol Table object containing identifiers.

        :return: Symbol Table object.
        """
        return self.symbol_table

    def __read_tokens(self):
        """
        Reads lexemes from token files and populates dictionaries for operators, separators, reserved words, and others.
        """
        self.operators = read_tokens("Lexic/operators.txt")
        self.reserved_words = read_tokens("Lexic/reserved_words.txt")
        self.separators = read_tokens("Lexic/separators.txt")
        self.lexic = read_tokens("Lexic/tokens.txt")

    def __get_line_for_error(self, token):
        """
        Retrieves the line number in the source file where a given token occurs.

        :param token: The token to be searched in the source file.
        :return: The line number where the token is found.
        """
        if self.last_scanned_file:
            with open(self.last_scanned_file, "r", encoding="utf-8") as f:
                for idx, line in enumerate(f):
                    if token in line:
                        return idx
        return None

    def __raise_lexical_error(self, token):
        """
        Raises a SyntaxError with a descriptive message if an unsupported character is found in the given token.

        :param token: The token to be checked for unsupported characters.
        :raises SyntaxError: If unsupported characters are found in the token.
        """
        line = self.__get_line_for_error(token)
        if line:
            error = f"Error on line - {line}\nNot supported character in {token} !"
            raise SyntaxError(error)
        else:
            raise KeyError("Line not found")

    def __split_into_multiple_tokens(self, token):
        """
         Splits a token into multiple tokens using separators and operators if necessary.
         If the token cannot be split, a SyntaxError is raised.

         :param token: The token to be split.
         :return: A list of tokens obtained by splitting the input token.
         :raises SyntaxError: If the token cannot be split into multiple tokens.
         """
        new_lst_of_tokens = split_with_separators(token, list(self.separators.keys()))
        if len(new_lst_of_tokens) <= 1:
            new_lst_of_tokens = split_with_separators(token, list(self.operators.keys()))
        if len(new_lst_of_tokens) <= 1:
            self.__raise_lexical_error(token)
        return new_lst_of_tokens

    def scan(self, prg_file_name):
        """
        Scans the given source file and generates the Symbol Table and Program Internal Form.

        :param prg_file_name: The path to the source file.
        """
        self.last_scanned_file = prg_file_name  # load last scanned file
        strings_to_print = []  # prepare to store the resulting tokens
        prg_file_tokens = read_program(prg_file_name)  # initial list of tokens
        while prg_file_tokens:  # as long as there are tokens in the list
            token = prg_file_tokens.pop(0)  # extract the first token
            if not self.__recognize_token(token):  # if it could not be recognized
                try:
                    lst_of_new_tokens = self.__split_into_multiple_tokens(token)  # try to split the token
                except SyntaxError as e:
                    strings_to_print.append(e)
                    break
                prg_file_tokens = lst_of_new_tokens + prg_file_tokens  # add to the beginning the new tokens

        if not prg_file_tokens:  # if all the tokens have been parsed -> no lexical error
            strings_to_print.append(str(self.get_symbol_table()))  # add the symbol table repr to the file
            strings_to_print.append(str(self.get_program_internal_form()))  # add the program internal form repr to the file

        write_results_to_file(prg_file_name, strings_to_print)

        return

    def __is_separator_or_operator_or_reserved_word(self, token):
        """
        Checks if the token is a separator, operator, or reserved word.

        :param token: The token to be checked.
        :return: True if the token is a separator, operator, or reserved word, False otherwise.
        """
        return token in self.separators or token in self.operators or token in self.reserved_words

    def __add_to_symbol_table_and_pif(self, token):
        """
        Adds the token to the Symbol Table and Program Internal Form.

        :param token: The token to be added.
        """
        self.symbol_table.add(token)
        pos = self.symbol_table.pos(token)
        self.program_internal_form.addPair(token, pos)

    def __recognize_token(self, token):
        """
        Recognizes a token and adds it to the Symbol Table or Program Internal Form accordingly.
        Returns True if the token is recognized, False otherwise.

        :param token: The token to be recognized.
        :return: True if the token is recognized and processed, False otherwise.
        """
        if self.__is_separator_or_operator_or_reserved_word(token):
            self.program_internal_form.addPair(token, 0)
        elif valid_identifier(token):
            self.__add_to_symbol_table_and_pif(token)
        else:
            return False
        return True


if __name__ == "__main__":
    scanner = Scanner()
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    prg_1_path = os.path.join(curr_dir, "..", "Lab1a", "p2.txt")
    scanner.scan(prg_1_path)
