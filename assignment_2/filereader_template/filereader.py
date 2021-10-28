import random

class FileReader:

    def __init__(self, filename):
        self.__filename = filename
        print("instance of FileReader class created!")
    
    def read_file(self):
        file_as_string = ""
        with open(self.get_filename()) as f: # file automatically closes at the end of with statement
            # we want to skip the first line of the file so we start the loop at index 1
            for i in range(1, len(f)):
                file_as_string += f[i] # append each line to the string 
                file_as_string += ":" # append a : after each line for easy splitting later
        return file_as_string

    def get_line_amount(self):
        with open(self.get_filename()) as f:
            line_amount = len(f)
        return line_amount

    def get_filename(self):
        return self.__filename
    
    def set_filename(self, filename):
        self.__filename = filename
    
    def read_random_range(self):
        with open(self.get_filename()) as f:
            start = 0
            end = 0
            # keep running randint on both variables until all the conditions are met
            while start == end or start >= end or stop > self.get_line_amount() or start < 1:
                start = random.randint(1, self.get_line_amount()-1) # start should be between 1 and the amount of lines - 1
                end = random.randint(2, self.get_line_amount()) # end should be between 2 and the amount of lines
        random_lines = self.read_file()[start:end + 1] # use the start and end variables to slice the string returned from readfile()
        return random_lines

    def get_lines_at(self, line_nums_list):
        lines_as_string = ""
        with open(self.get_filename()) as f:
            for line_num in line_nums_list:
                for line in f:
                    line_as_list = line.split(",") # split the string into a list separated by ,
                    if line_num == line_as_list[0]: # check if the line_num matches the num(0th index) of the line
                        lines_as_string += line # append line
                        lines_as_string += ":" # append : to separate lines
        return lines_as_string               



    

class QuestionFileReader(FileReader):
    
    def __init__(self, filename)):
        pass

    def all_dictionary_questions(self):
        pass

    def random_dictionary_questions(self):
        pass