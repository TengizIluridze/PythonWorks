'''
1)Input birthday

2)Calculate Exact Age

3)Habdle Leap years

4)Different Date formants

1)Next Birthday Calculator

2)Age in Different Units

3)Historical Age Calculation

4)Future Age Calculation

5)Age Comparision
'''
from datetime import date,datetime

class AgeCalculator:
    def __init__(self,Birthday,Today):
        self.Birthday = Birthday
        self.Today = Today
    

    def showAge(self):
        if (self.Today.month,self.Today.day) > (self.Birthday.month,self.Birthday.day):
            total_age = self.Today.year-self.Birthday.year-1
            return total_age
        else:
            total_age = self.Today.year-self.Birthday.year
            return total_age
        

    def nextBirthday(self):
        next_birthday = self.Birthday.replace(year=self.Today.year)
        if next_birthday > self.Today:
            print(f"Your next birthday is in {abs((next_birthday - self.Today).days)} days ")
            return (next_birthday - self.Today).days
        else:
            next_birthday = self.Birthday.replace(year = self.Today.year+1)
            print(f"Your next birthday is in {abs((next_birthday - self.Today).days)} days ")
            return (next_birthday - self.Today).days

    def ageConverter(self,choice):
        #1)hours
        #2)Days
        #3)Months
        if choice == 1:
            print(f"You are : {int(abs(self.Today - self.Birthday).total_seconds()/3600)} hour old")
        elif choice == 2:
            print(f"You are : {int((abs(self.Today - self.Birthday).days))} days old ")
        elif choice == 3:
            print(f"You are : {int(abs(self.Today - self.Birthday).days/29.53)} month old ")
            
    def historicalAgeCalculator(self,Date):
        if Date < self.Today and Date > self.Birthday:
            historical_age = (Date - self.Birthday).days / 365.25
            print(f"on this date: {Date.day}/{Date.month}/{Date.year}, you were {round(historical_age)} years old")
        else:
            print("Please enter the valid date")
    
    def futureAgeCalculator(self,Date):
        if Date > self.Today:
            historical_age = (Date - self.Birthday).days / 365.25
            print(f"on this date: {Date.day}/{Date.month}/{Date.year}, you wil be {round(historical_age)} years old")
        else:
            print("Please enter the valid date")
    
    def ageComparision(self,age):
        if age > self.Birthday:
            difference = (age - self.Birthday).days
            print(f"This person is {round(difference)} days younger than you")
        elif age == self.Birthday:
            print("This person is same age as you")
        else:
            difference = (self.Birthday-age).days
            print(f"This person is {round(difference)} days older than you")
        
        
    
    
def ageInput():
    date_input = input("Enter a date (Day,Month,Year): ")
    real_date = None
    m = None
    formats = ['%d,%m,%Y','%d/%m/%Y','%d-%m-%Y','%d.%m.%Y','%d %m %Y']
    while(real_date == None):
        for i in formats:
            try:
                real_date = datetime.strptime(date_input,i)
                
                
            except ValueError:
                continue
        if(real_date == None):
            print("Please enter the real date")
            date_input = input("Enter a date (DD,MM,YYYY): ")
        else:
            print(f"Chosen date is : {real_date.day}/{real_date.month}/{real_date.year}")    
    return (real_date)
            
def main():
    real_date = ageInput()
    today = datetime.now()

    person = AgeCalculator(real_date,today)
    while(True):
        print(
f'''1)Show your exact age
2)Show your next birthday
3)Turn your age into the different units
4)Historical age calculator
5)Future age calculator
6)Age comparision
7)Exit the program
PLEASE INPUT THE NUMBER:'''
        )
        choice = int(input())
        if  (choice == 1):
            print(person.showAge())

        elif(choice == 2):
            person.nextBirthday()

        elif(choice == 3):
            choice = int(input(
f'''
1. Turn your age into hours
2. Turn your age into days
3. Turn your age into months
Choose number:
'''))
            person.ageConverter(choice)


        elif(choice == 4):
            age = ageInput()
            person.historicalAgeCalculator(age)
            
        

        elif(choice == 5):
            age = ageInput()
            person.futureAgeCalculator(age)

        elif(choice == 6):
            friends_age = ageInput()
            person.ageComparision(friends_age)


        elif(choice == 7):
            print("Have a nice day :)")
            return 0

main()