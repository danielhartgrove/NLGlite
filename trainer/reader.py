# read a file and return the contents
def readFile(filepath):
    data = []
    if(filepath.endswith(".txt")):
        try:
            f = open(filepath,"r")
            data.append(file.load(f))
            file.close(f)  
            return data
        except:
            print("File not found.")
            return None
    elif(filepath.endswith("/")):
        try:
            contents = os.listdir(directory)
            for item in contents:
                data.append(readFile(item))
            return data
        except:
            print("Directory not found.")
            return None
    else:
        print("Invalid file path.")
        return None

def scrape(text, output_file_path):
    f = open(output_file, "w")
    wordlist = text.split(" ")
    for i in range(1, len(wordlist)):                           # write all word pairs to a file
        f.write(wordlist[i-1] + " " + wordlist[i] + "\n")