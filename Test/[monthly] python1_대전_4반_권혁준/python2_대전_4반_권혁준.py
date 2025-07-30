class Book:
    book_count = 0  #craete class variable
    def __init__(self, title, author, year, price):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        Book.book_count += 1 #when create a book instance, add 1 to variable

    def get_info(self): #definition instance method
        return f"{self.title} - {self.author}, {self.year}, {self.price}"
    
    @staticmethod   #indicate static method
    def is_expensive(price): #def static method
        if price >= 30000:      #setting condition
            return True
        else:
            return False
        
    @classmethod
    def get_book_count(cls):    #def class method
        return Book.book_count  # return current book's count
    
    @classmethod
    def from_string(cls, info_str): #def class method
        info_str = info_str.split('/')   # make string to string list
        return Book(info_str[0],info_str[1],info_str[2],info_str[3])  #convert info_str to instance format

# 아래 코드는 수정 할 수 없음
book1 = Book("파이썬 완벽 가이드", "홍길동", 2023, 35000)
book2 = Book.from_string("자료구조의 이해/이순신/2021/28000")

print(book1.get_info())
# [파이썬 완벽 가이드 - 홍길동, 2023년, 35000원]
print(Book.is_expensive(35000))  # True
print(Book.get_book_count())     # 2
