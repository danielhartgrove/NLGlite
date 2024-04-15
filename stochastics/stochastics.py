import random


def generate_number(lower: int, upper: int):
    """
    Generates a random number between lower and upper and returns 0 if the parameters are not in the right order. Does
    not allow for negative numbers to be used as this is a wrapper function for the rest of the library.
    :param lower: the lower bound (inclusive) of the generation
    :param upper: the upper bound (inclusive) of the generation
    :return: A random integer between lower and upper or -1
    """
    if -1 < lower <= upper:
        return random.randint(lower, upper)
    else:
        return -1


def select_word_with_bias(old_vector: [int], lookup_table: [str]):
    """
    Creates a vector from an old vector and then selects an appropriate element from the vector based on its probability.
    The vectors should correspond 1:1 and so the same index is chosen from the lookup_table as the selected word.
    :param old_vector: The vector containing the probabilities of the next words. i.e. probability of lookup_table[i]
    :param lookup_table: The vector containing the possible next words.
    :return: The selected word
    """
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

