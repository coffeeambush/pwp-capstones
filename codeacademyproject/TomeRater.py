class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        return print("User" + self.name + "  has been updated to email: "+self.email)

    def __repr__(self):
        return self.name + ", email:" + self.email + ", books read " + str(len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        return False

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        average = 0
        ratingsbook = 0
        for i in self.books.values():
            if i:
                average += i
                ratingsbook += 1
        average = average/ratingsbook
        return average

class Book(object):
    def __init__(self,title,isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self,isbn):
        self.isbn = isbn
        print("The book " + self.title + " has an updated ISBN of: "+str(self.isbn))

    def add_rating(self,rating):
        if rating and rating > 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, book2):
        if self.title == book2.title and self.isbn == book2.isbn:
            return True
        else:
            return False
    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_average_rating(self):
        average = 0
        for rating in self.ratings:
            average += rating
        average = average/len(self.ratings)
        return average

class Fiction(Book):
    def __init__(self, title, author, isbn):
        Book.__init__(self,title,isbn)
        self.author = author
    def get_author(self):
        return self.author
    def __repr__(self):
        return self.title + " by :" + self.author

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        Book.__init__(self, title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return self.title + ", a " + self.level + " manual on " + self.subject

class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self,title,isbn):
        newbook = Book(title, isbn)
        return newbook

    def create_novel(self,title,author,isbn):
        newbook = Fiction(title, author, isbn)
        return newbook

    def create_non_fiction(self,title,subject,level,isbn):
        newbook = Non_Fiction(title,subject,level,isbn)
        return newbook

    def add_book_to_user(self,book,email,rating=None):
        user = self.users.get(email, None)
        if user:
            user.read_book(book, rating)
            if book not in self.books:
                self.books[book] = 0
            self.books[book] += 1
            book.add_rating(rating)
        else:
            print("No user with address " + email + " !")

    def add_user(self, name, email, user_books=None):
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        maxread = float("-inf")
        read_most = None
        for book in self.books:
            reads = self.books[book]
            if reads > maxread:
                maxread = reads
                read_most = book
        return read_most

    def highest_rated_book(self):
        max_read = float("-inf")
        most = None
        for book in self.books:
            average = book.get_average_rating()
            if average > max_read:
                max_read = average
                best = book
        return best

    def most_positive_user(self):
        maxrating = float("-inf")
        mostpositive = None
        for user in self.users.values():
            average = user.get_average_rating()
            if average > maxrating:
                maxrating = average
                mostpositive = user
        return mostpositive

    def print_catalog(self):
        for book in self.books:
            print(book)