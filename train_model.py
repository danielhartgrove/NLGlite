from trainer import reader as reader


def __main__():
    path = input("Please enter a txt file path to read from: ")
    data = reader.read_file(path)
    out_path = input("Please enter a lcfg file path to write to:")
    if out_path == "":
        out_path = "training_data.lcfg"  # training data liteconfig
    genre = input("Would you like to use POS or BLOB?\n -POS (Default) \n -BLOB\n")
    if genre == "BLOB":
        reader.scrape(data, out_path, 2)
    else:
        reader.scrape(data, out_path, 1)

    print("Model has been trained for the file: " + path + " and the data has been written to training_data.lcfg")


__main__()
