import random


def generate_number(lower: int, upper: int):  # will be replaced with stochastics later
    return random.randint(lower, upper)


def select_word_with_bias(old_vector: [int], lookup_table: [str]):
    vector = []
    for i in range(len(old_vector)):
        vector.append(int(old_vector[i]))

    # calculate the frequency of word based on Zipf's law

    zipf_vector = [0.0]
    for i in range(0, len(vector)):
        zipf_vector.append(lambda r, p: 5 / r ** p)  # Zipf's law formula

    zipf_vector = zipf_vector.remove(0)
    chosen_item = random.choices(lookup_table, weights=zipf_vector, k=1)[0]

    return chosen_item
