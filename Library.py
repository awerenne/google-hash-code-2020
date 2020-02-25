

class Library:
    def __init__(self, id, signup_time, ship_speed, book_values, book_indices):
        self.id = id
        self.sign_time = sign_time
        self.ship_speed = ship_speed
        self.book_values = book_values
        self.book_indices = book_indices
        self.sort_books()

    def sort_books(self):
        self.book_indices.sort(key=lambda idx: book_indices[idx], reverse=True)

    def compute_score(self, n_days_left):
    	sum_book_values = sum(map(lambda x: x[1], self.get_shipped_books(n_days_left)))
        return sum_book_values + (W*days_left / (self.signup_time+days_left))

    def get_shipped_books(self, n_days_left):
        capacity = min((n_days_left-self.sign_time) * self.ship_speed, len(self.books))
        self.shipped_books = self.book_indices[:capacity]
        return self.shipped_books



















