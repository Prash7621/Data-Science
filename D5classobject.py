class car:
    def __init__(self , model , year):
        self.model=model
        self.year=year

    def display_car_info (self):
       print(f"Car : {self.model} , {self.year}" )
    def display_car_into2(self):
        print("Model of the car : " + self.model)
        print("Year of the car : " + self.year)

model="Thar"
year=2015
C1=car(model , year)
C1.display_car_info()
C2=car(model="Safari" , year=2009)
C2.display_car_info()




class book:
    def __init__(self , title , author):
        self.title=title
        self.author=author

    def book_detailed (self):
       print("Title of the book : " + self.title)
       print("author of the book : " +self.author)
title="msdhoni"
author="Ezekiel gulu"
B1=book(title , author)
B1.book_detailed()

     
        