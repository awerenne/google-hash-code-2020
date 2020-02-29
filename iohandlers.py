
from Library import Library


def read(fname):
    with open(fname, 'r') as reader:
        n_books, n_libraries, n_days = [int(i) for i in reader.readline().split(" ")]
        book_values = [int(i) for i in reader.readline().split(" ")]
        libraries = []
        for id_library in range(n_libraries):
            _, sign_time, ship_speed = [int(i) for i in reader.readline().split(" ")]
            book_indices = [int(i) for i in reader.readline().split(" ")]
            libraries.append(Library(id_library, sign_time, ship_speed, book_values, book_indices))
    return n_books, n_libraries, n_days, book_values, libraries


def write(fname, solution, book_values):
    with open(fname, 'w') as f:
        n_signed_libraries = len(solution)
        f.write(str(n_signed_libraries) + "\n")
        set_indices = set()
        for library in solution:
            if not library: 
            	continue
            shipped_books = library.shipped_books
            f.write(str(library.id) + " " + str(len(shipped_books)) + "\n")
            out = " ".join(map(str, shipped_books))
            f.write(out + '\n')
            set_indices |= set(shipped_books)
        return sum((book_values[idx] for idx in set_indices))









