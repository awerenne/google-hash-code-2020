
import time
from io import *


def place_value(number): 
    return "{:,}".format(number)


def solve(fname):
    _, _, n_days, book_values, libraries = read("input/" + fname + ".txt")
    solution = compute_greedy(list(book_values), libraries, n_days)
    score = write("output/" + fname + ".txt", solution, book_values)
    return score


def remove_books(book_values, book_indices):
    for idx in book_indices:
        book_values[idx] = 0


def compute_greedy(book_values, libraries, n_days):
    day = 0
    solution = []
    while day < n_days and libraries:
        index, library = find_best_library(libraries) 
        remove_books(library.shipped_books)
        solution.append(book_values, library)
        libraries.pop(index)
        day += library.signup_time
    return solution


def find_best_library(libraries):
    max_score = -float("Inf")
    for index, library in enumerate(libraries):
        library.sort_books()
        score = library.get_score(n_days - day)
        if score > max_score:
            max_score = score
            max_library = library
            max_index = idx
    return max_index, max_library


if __name__ == "__main__":
    W = 1000000
    files = ["a_example", "b_read_on", "c_incunabula", "d_tough_choices", "e_so_many_books", "f_libraries_of_the_world"]
    total_score = 0
    for i, fname in enumerate(files):
        start_time = time.time()
        score = solve(fname)
        total_score += score
        print("File %s" % (fname))
        print("\t score: %s" % (place_value(score)))
        print("\t runtime: %.2f" % (time.time() - start_time))
        print(score)
    print("\nTotal score: %s" % (place_value(total_score)))






















