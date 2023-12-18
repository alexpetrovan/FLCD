from Grammar.grammar import Grammar
from Parser.parser import Parser
from Parser.parser_output import ParserOutput


def main():
    while True:
        print("Choose an option:")
        print("1. Using Sequence w = aacbc")
        print("2. Using program p1.txt")
        print("0. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            grammar_file = "Grammar/g1.txt"
            sequence_file = "seq1.txt"
            output_file = "out/out1.txt"
            execute_parser(grammar_file, sequence_file, output_file)
        elif choice == '2':
            print("Not implemented yet")
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please select a valid option.")
            continue


def execute_parser(grammar_file, sequence_file, output_file):
    grammar = Grammar()
    grammar.read_from_file(grammar_file)

    parser = Parser(grammar, sequence_file, output_file)
    parser.run()

    parser_output = ParserOutput(grammar, sequence_file, output_file)
    parser_output.create_parsing_tree(parser.working)
    parser_output.write_parsing_tree(parser.state, parser.working)


if __name__ == "__main__":
    main()