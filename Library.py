

class Library:
    def __init__(self, id, signup_time, ship_speed, books):
        self.id = id
        self.signup_time = signup_time
        self.shipping_speed = shipping_speed
        self.books = books
        self.sort_books()

    def sort_books(self):
        self.books = self.books.sort(key=lambda x: x[1], reverse=True)

    def compute_score(self, n_days_left):
    	sum_book_values = sum(map(lambda x: x[1], self.get_scanned_books(n_days_left)))
        return sum_book_values + (W*days_left / (self.signup_time+days_left))

    def get_scanned_books(self, n_days_left):
        capacity = min((n_days_left-self.signup_time) * self.ship_speed, len(self.books))
        self.scanned_books = self.books[:capacity]
        return self.scanned_books



















