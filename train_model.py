from trainer import reader


def __main__():
    path = input("Please enter a file path to read from, or a folder if you want to read multiple files: ")
    data = reader.readFile(path)
    if(data != None):
        combined_data = []
        for item in data:
            combined_data += item
    else:
        print("Error reading file.")
        return None
    print("File read successfully.")
    
    reader.scrape(combined_data, "test.txt")

__main__()