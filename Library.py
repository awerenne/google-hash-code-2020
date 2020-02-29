
W = 1000000

class Library:
    def __init__(self, id, sign_time, ship_speed, book_values, book_indices):
        self.id = id
        self.sign_time = sign_time
        self.ship_speed = ship_speed
        self.book_values = book_values
        self.book_indices = book_indices
        self.sort_books()

    def sort_books(self):
        self.book_indices.sort(key=lambda idx: self.book_values[idx], reverse=True)

    def compute_score(self, n_remaining_days):
        sum_book_values = sum(map(lambda idx: self.book_values[idx], self.get_shipped_books(n_remaining_days)))
        return sum_book_values + (W*n_remaining_days / (self.sign_time+n_remaining_days))

    def get_shipped_books(self, n_remaining_days):
        capacity = min((n_remaining_days-self.sign_time) * self.ship_speed, len(self.book_indices))
        self.shipped_books = self.book_indices[:capacity]
        return self.shipped_books



















