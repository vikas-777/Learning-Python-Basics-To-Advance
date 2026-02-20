class Book:
    def __init__(self, book_id, book_name, author):
     self.book_id = book_id
     self.book_name = book_name
     self.author = author
    def show_book(self):
        return f"{self.book_id} - {self.book_name} by {self.author}"
class Member:
    def __init__(self, member_id, name):
         self.member_id = member_id
         self.name = name
         self.issued_books = []
    def issue_book(self, book):
        self.issued_books.append(book)
    def show_member(self):
         return f'''
        Member ID : {self.member_id}
        Name : {self.name}
        Books : {[book.book_name for book in self.issued_books]}
        '''
book1 = Book(201, "Python Basics", "Guido")
book2 = Book(202, "Data Science Intro", "Andrew")
book3 = Book(203,"Java", "Vikas")
book4 = Book(204,"Data structures","Azad farooq")
book5 = Book(205,"SQl","Data with Bara")
member1 = Member(1, "Rahul")
member2 = Member(2, "Anjali")
member3 = Member(3,"Vikas")
member1.issue_book(book1)
member1.issue_book(book2)
member2.issue_book(book1)
member3.issue_book(book5)
members = [member1, member2,member3]
for member in members:
 print(member.show_member())