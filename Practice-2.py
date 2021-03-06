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
        self._price = price
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
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,new_price):
        if self.new_price<50 | self.new_price>1000:      
            raise ValueError('The price should be between 50 and 1000')     
        else:
            self_price = new_price
       
class Fraction():
    def __init__(self,nr,dr=1):
        self.nr = nr
        self.dr = dr
        if self.dr<0:
            self.nr*=-1
            self.dr*=-1
    def show(self):
        print(f'{self.nr}/{self.dr}')
    def multiply(self,other):
        if isinstance(other,int):
            other = Fraction(other)
        return Fraction(self.nr*other.nr,self.dr*other.dr)
    def add(self,other):
        if isinstance(other,int):
            other = Fraction(other)
        return Fraction(self.nr * other.dr + self.dr * other.nr,self.dr*other.dr)
        
class Product():
    def __init__(self, id, marked_price, discount):
        self.id = id
        self.marked_price = marked_price
        self._discount = discount
    
    def display(self):
        print(self.id,  self.marked_price,  self.discount)
        
    @property
    def selling_price(self):
        selling_price1 = self.marked_price * (1-self.discount*0.01)
        return selling_price1
    @property
    def discount(self):
        if self.marked_price>500:
            return self._discount+2
        else:
            return self._discount
    @discount.setter
    def discount(self,other_discount):
        self._discount = other_discount
 
 
class Circle():
    def __init__(self,radius):
        self.radius = radius
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self,new_radius):
        if new_radius < 0:
            raise ValueError('The radius can not be less than zero')
        else:
            self._radius=new_radius
    
    def area(self):
        return 3.14*self.radius*self.radius
    @property
    def dia(self):
        self._diameter = 2*self.radius
        return self._diameter
    @property
    def circum(self):
        self.circumference = 2*3.14*self.radius
        return self.circumference
              
c1 = Circle(7)
print( c1.radius, c1.dia, c1.circum, c1.area() )
  
# p1 = Product('A234', 100, 5)
# p2 = Product('X879', 400, 6)
# p3 = Product('B987', 990, 4)
# p4 = Product('H456', 800, 6)
 
# print(p1.id, p1.selling_price)
# print(p2.id, p2.selling_price)
# print(p3.id, p3.selling_price)
# print(p4.id, p4.selling_price)
 
# p4.discount = 10
# print(p4.id, p4.selling_price)    


# f1 = Fraction(2,3)
# f1.show()
# f2 = Fraction(3,4)
# f2.show()
# f3 = f1.multiply(f2)
# f3.show()
# f3 = f1.add(f2)
# f3.show()
# f3 = f1.add(5) 
# f3.show()
# f3 = f1.multiply(5) 
# f3.show()
         
       


# book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200,0)
# book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
# book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
# book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)

# # print(f'The number of books are {book1.copies}')
# # book1.sell()
# # print(f'The number of books after sell are {book1.copies}')

# # Answering the question 4

# books = [book1,book2,book3,book4]

# # print([books[i].display() for i in range(len(books))])
# titles = [book.title for book in books if book.author=='Jack']
# print(titles)