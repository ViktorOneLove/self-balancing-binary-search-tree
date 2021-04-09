from red_black_tree import RedBlackTree
import random
import time
import matplotlib.pyplot as plt


def countTime():
    repetitions = 1000
    num_of_max_elements = 500
    min_possible_value = -100000
    max_possible_value = 100000

    possible_values = list(range(min_possible_value, max_possible_value))
    number_of_elements = [num for num in range(num_of_max_elements)]

    all_times_insert = [0] * num_of_max_elements
    all_times_search = [0] * num_of_max_elements
    for _ in range(repetitions):
        red_black_tree = RedBlackTree()
        for cur_number_of_elements in number_of_elements:

            start_time_insertion = time.perf_counter()
            red_black_tree.insert(random.choice(possible_values))
            end_time_insertion = time.perf_counter()
            all_times_insert[cur_number_of_elements] += end_time_insertion - start_time_insertion

            start_time_search = time.perf_counter()
            red_black_tree.search(random.choice(possible_values))
            end_time_search = time.perf_counter()
            all_times_search[cur_number_of_elements] += end_time_search - start_time_search

    all_times_insert = [time_insert / repetitions for time_insert in all_times_insert]
    all_times_search = [time_search / repetitions for time_search in all_times_search]

    plt.plot(number_of_elements, all_times_insert)
    plt.plot(number_of_elements, all_times_search)
    plt.xlabel("Num of elements")
    plt.ylabel("Time")
    plt.legend(["Insertion", "Search"])
    plt.savefig("time.png")
    plt.show()
