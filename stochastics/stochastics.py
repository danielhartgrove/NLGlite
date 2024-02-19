import numpy as np
import random


def generate_number(lower, upper):  # will be replaced with stochastics later
    return random.randint(lower, upper)


def select_word_with_bias(old_vector, lookup_table):
    vector = []
    for i in range(len(old_vector)):
        vector.append(int(old_vector[i]))

    mean = np.mean(vector)
    std_dev = np.std(vector)

    if std_dev == 0:
        ceiling_value = 0
        j = 0
        for i in range(0, len(vector)):
            if vector[i] > ceiling_value:
                ceiling_value = vector[i]
                j = i

        return lookup_table[j]

    std_devs_away = []
    for item in vector:
        std_devs_away.append((item - mean) / std_dev)

    total = np.sum(std_devs_away)

    normalized_vector = []
    for item in std_devs_away:
        normalized_vector.append(item / total)

    for i in range(1, len(normalized_vector)):
        key = normalized_vector[i]
        lookup_key = lookup_table[i]
        j = i - 1
        while j >= 0 and normalized_vector[j] > key:
            lookup_table[j + 1] = lookup_table[j]
            normalized_vector[j + 1] = normalized_vector[j]
            j -= 1
        normalized_vector[j + 1] = key
        lookup_table[j + 1] = lookup_key

    # calculate the frequency of word based on zipfian mathematics
    zipf_vector = [0.0]
    for i in range(0, len(normalized_vector)):
        zipf_vector.append(lambda r, p: 5 / r**p)  # Zipf's law formula

    zipf_vector = zipf_vector.remove(0)
    chosen_item = random.choices(lookup_table, weights=zipf_vector, k=1)[0]

    return chosen_item
