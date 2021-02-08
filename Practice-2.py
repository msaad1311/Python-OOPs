class bankAccount():
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def display(self):
        print(f'The name is {self.name}')
        print(f'The balance is {self.balance}')
    def withdraw(self,amount):
        self.balance-=amount
    def deposit(self,amount):
        self.balance+=amount

class Book():
    def __init__(self,isbn,title,author,publisher,pages,price,copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.price = price
        self.copies = copies
    def display(self):
        print('ISBN: \t', self.isbn)
        print('Title: \t', self.title)
        print('Author: \t', self.author)
        print('publisher: \t', self.publisher)
        print('pages: \t', self.pages)
        print('price: \t', self.price)
        print('copies: \t', self.copies)
    def in_stock(self):
        if self.copies >0:
            return True
        else:
            return False
    def sell(self):
        if self.in_stock():
            self.copies-=1
        else:
            print('The book is out of stock')    
    

book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200,0)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)

print(f'The number of books are {book1.copies}')
book1.sell()
print(f'The number of books after sell are {book1.copies}')