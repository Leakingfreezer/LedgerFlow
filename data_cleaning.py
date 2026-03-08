"""
Usage Case: After text is extracted from the OCR method and in the Raw_text.txt document, text
will go through data cleaning, aggreation methods, etc and text file will be deleted.
"""

class RawTextProcessor: 
    '''textFile class represents the OCR raw text file'''

    def __init__(self, file_path = 'Raw_text.txt', text_list = []): 
        self.file_path = file_path
        self.text_list = text_list

    def text_to_list(self):
    #Data read from the text file and stored as a string is first cleaned with Python string methods
        try: 
            with open(self.file_path, 'r') as file:
                for line in file: 
                    self.text_list.append(line.strip().split("\n"))
        except FileNotFoundError: 
            print(f"Error: The file '{self.file_path}' was not found.")
            