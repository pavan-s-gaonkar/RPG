class ASCII:
    def __init__(self, file_to_read):
        self.number_set = list()
        self.upper_case_char_set = list()
        self.lower_case_char_set = list()
        self.symbol_set = list()

        self.extract_character_set(file_to_read)

    def extract_character_set(self, file_to_read):
        ascii_file = open(file_to_read, 'r')
        lines = ascii_file.readlines()
        for line in lines:
            self.add_data(line)

    def add_data(self, data):
        data_set = data.strip().split(" ")
        if len(data_set) != 3:
            print("Error " + data)
        else:
            if data_set[0] == "1":
                self.number_set.append(data_set[2])
            if data_set[0] == "2":
                self.upper_case_char_set.append(data_set[2])
            if data_set[0] == "3":
                self.lower_case_char_set.append(data_set[2])
            if data_set[0] == "4":
                self.symbol_set.append(data_set[2])

    def print_data(self):
        print(self.number_set)
        print(self.upper_case_char_set)
        print(self.lower_case_char_set)
        print(self.symbol_set)
