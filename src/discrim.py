from NLGlite.NLGlite import NLGlite_ as nlg

model = nlg()

model.set_config_file_path("C:/Users/Danbo/Documents/UoN_CompSci/Year "
                           "3/COMP3003/Project/NLGlite/src/data/config/books/crimeandpunishment.lcfg")
            
total = 0

for i in range(0, 100):

    print(model.generate_sentences(1, False))
    print("is this a valid sentence? Y/N")

    ans = input().lower()
    if ans == "y":
        total += 1

print("" + str(total) + "%")
