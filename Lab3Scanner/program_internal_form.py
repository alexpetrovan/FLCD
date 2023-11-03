class ProgramInternalForm:
    def __init__(self):
        """
        Initializes a new ProgramInternalForm object with an empty internal form list.
        """
        self.internal_form_list = []

    def __str__(self):
        """
        Returns a string representation of the Program Internal Form.

        :return: String representation of the Program Internal Form.
        """
        res = "___PIF___"
        for identifier, const in self.internal_form_list:
            res += f"\n{identifier} | {const}"
        return res

    def addPair(self, identifier, constant):
        """
        Adds a pair of identifier and constant to the internal form list.

        :param identifier: The identifier to be added to the internal form list.
        :param constant: The constant associated with the identifier.
        """
        self.internal_form_list.append((identifier, constant))