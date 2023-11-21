class FiniteAutomaton:
    def __init__(self):
        # Initialize the FA attributes
        self.states = []
        self.alphabet = []
        self.initial_state = None
        self.final_states = set()
        self.transitions = {}

        self.is_dfa = True  # Assume it's a DFA by default

    def __check_dfa(self):
        # Method to check if the FA is deterministic
        return self.is_dfa

    def read_FA_from_file(self, filename):
        # Read the FA from the input file
        with open(filename, "r") as file:
            # Take its attributes
            self.states = file.readline().strip().split()
            self.alphabet = file.readline().strip().split()
            self.initial_state = file.readline().strip()
            self.final_states = set(file.readline().strip().split())

            # Process transitions from the file
            for line in file:
                parts = line.strip().split()
                if len(parts) == 3:
                    current_state, input_symbol, next_state = parts

                    # Check at any point if the conditions for a DFA do not hold
                    if self.is_dfa:
                        if current_state in self.transitions and input_symbol in self.transitions[current_state]:
                            self.is_dfa = False

                        if input_symbol == "ε":
                            self.is_dfa = False

                    # Create transitions for the FA
                    if current_state not in self.transitions:
                        self.transitions[current_state] = {}
                    self.transitions[current_state][input_symbol] = next_state

    def __print_menu(self):
        print("What would you like to display?")
        print("0. Cancel")
        print("1. Set of States")
        print("2. Alphabet")
        print("3. Transitions")
        print("4. Initial State")
        print("5. Set of Final States")

    def display_elements(self):
        self.__print_menu()
        while True:
            try:
                option = int(input("Select an option - "))
                if option == 0:
                    return
                elif option == 1:
                    print("Set of States:", self.states)
                elif option == 2:
                    print("Alphabet:", self.alphabet)
                elif option == 3:
                    print("Transitions:")
                    for state, transitions in self.transitions.items():
                        for symbol, next_state in transitions.items():
                            print(f"   {state} -- {symbol} --> {next_state}")
                elif option == 4:
                    print("Initial State:", self.initial_state)
                elif option == 5:
                    print("Set of Final States:", self.final_states)
                else:
                    print("Not a valid option")
            except Exception as e:
                print(e)

    def verify_dfa_sequence(self, sequence):
        # Check if the input sequence is accepted by FA (only works for DFA)
        if not self.__check_dfa():
            return "Automaton is not a DFA."

        invalid_sequence = "Sequence is not accepted by the FA"

        current_state = self.initial_state

        # Process each symbol in the input sequence
        for symbol in sequence:
            if current_state not in self.transitions or symbol not in self.transitions[current_state]:
                return invalid_sequence
            current_state = self.transitions[current_state][symbol]

        return "Sequence accepted" if current_state in self.final_states else invalid_sequence


fa = FiniteAutomaton()
fa.read_FA_from_file("dfa_input.txt")
fa.display_elements()

print(fa.verify_dfa_sequence("baaab"))
print(fa.verify_dfa_sequence("ababa"))

