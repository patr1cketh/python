class FileReader:

    def __init__(self, filename):
        self.__filename = filename
        print("instance of FileReader class created!")
    
    def read_file(self):
        file_1 = open(self.__filename)
        return file_1
    

class QuestionFileReader(FileReader):
    pass