
import Library


def read(fname):
    with open(fname, 'r') as reader:
        n_books, n_libraries, n_days = [int(i) for i in reader.readline().split(" ")]
        book_values = [int(i) for i in reader.readline().split(" ")]
        libraries = []
        for id_library in range(n_libraries):
            _, sign_time, ship_speed = [int(i) for i in reader.readline().split(" ")]
            books_indices = [int(i) for i in reader.readline().split(" ")]
            books = [(book_index, book_values[book_index]) for book_index in books_indices]
            libraries.append(Library(id_library, signup_time, ship_speed, books))
        return n_books, n_libraries, n_days, book_values, libraries


def write(fname, solution, book_values):
    with open(fname, 'w') as f:
    	n_signed_libraries = len(solution)
        f.write(str(n_signed_libraries) + "\n")
        shipped_books = set()
        for library in solution:
            if not library: 
            	continue
            shipped_books = library.shipped_books
            f.write(str(library.id) + " " + str(len(shipped_books)) + "\n")
            shipped_books_indices = (book[0] for book in shipped_books)
            out = ""
            for idx in shipped_books_indices:
                shipped_books.add(idx)
                out += str(idx) + " "
            f.write(out + '\n')
        return sum((book_values[idx] for idx in shipped_books))









