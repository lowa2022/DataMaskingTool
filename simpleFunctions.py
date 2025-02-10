from faker import Faker
from datetime import date
import datetime
import random
import string
import re
import pandas as pd
import csv
import unicodecsv as cs
from fastparquet import ParquetFile
import faker


fake = Faker('en_US')  # US
locales = 'en_IN', 'en_US', 'es_ES', 'en_PH'  # list of the locales
faker = Faker(locales)  # Diversified

def isZipCode(number):
    test_string = number
    matched = re.match("^[0-9]{5}$", test_string) or re.match("^[0-9]{10}$", test_string)
    is_match = bool(matched)
    return is_match


def isPhoneNumber(number):
    test_string = number
    matched = re.match("^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$",test_string)
    is_match = bool(matched)
    return is_match

def claimNumberGenerator():
    claim_number = f"{random.randint(0,9)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.randint(10000000,99999999)}"
    return claim_number

def vin_generator():
    return f"{''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(17))}{random.randint(100000,999999)}"

def policy_generator():
    return f"{''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(8,12)))}{random.randint(100000,999999)}"


def vinWithModel(char):
    return f"{''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(9))}{char}{''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))}"
    
    
def TIN():  # like social security
    tin = f"9{str(random.randint(10,99))}-{str(random.randint(10,99))}-{str(random.randint(1000,9999))}"
    return tin


def firstnameemail(firstname,lastname):  # generstes email with firstname in the beginning
    if firstname == "" or lastname == "":
        email = fake.email()
    else:
        email = f"{firstname}.{lastname}{random.randint(1,99)}@{faker.domain_name()}"
    return email


def lastnameemail(firstname,lastname):  # generstes email with lastname in the beginning
    if firstname == "" or lastname == "":
        email = fake.email()
    else:
        email = f"{lastname}.{firstname}{random.randint(1,99)}@{faker.domain_name()}"
    return email


def fLastNameemail(firstname,lastname):  # generstes email with lastname in the beginning
    if firstname == "" or lastname == "":
        email = fake.email()
    else:
        email = f"{firstname[0]}.{lastname}{random.randint(1,99)}@{faker.domain_name()}"
    return email


def firstNameEmailDomain(firstname, lastname,domain):  # generstes email with firstname in the beginning
    if firstname == "" or lastname == "":
        email = fake.email()
    else:
        email = f"{firstname}.{lastname}{random.randint(1,99)}@{domain}"
    return email


def lastNameEmailDomain(firstname, lastname, domain):  # generstes email with lastname in the beginning
    if firstname == "" or lastname == "":
        email = fake.email()
    else:
        email = f"{lastname}.{firstname}{random.randint(1,99)}@{domain}"
    return email


def fLastNameEmailDomain(firstname, lastname, domain):  # generstes email with lastname in the beginning
    if firstname == "" or lastname == "":
        email = fake.email()
    else:
        email = f"{firstname[0]}.{lastname}{random.randint(1,99)}@{domain}"
    return email


def GetValidDob(birthYear):
    todays_date = date.today() #get todayts date
    start_date = datetime.date(todays_date.year, 1, 1) #starting date is this new year
    fakedate = fake.date_between_dates(date_start=start_date,
                                       date_end=todays_date) #generate fake date between this new year and today
    dob = datetime.date(birthYear, fakedate.month, fakedate.day) #generate fake dob
    birthday = dob.strftime('%m/%d/%Y')
    return birthday

def xlsxtocsv(file): #function to change excel to csv format
    read_file = pd.read_excel (file)
    read_file.to_csv('sample.csv', index = None, header=True, date_format='%m/%d/%Y')
# rule dictionary to be applied in the program

def parquetTocsv(file):
    #fake.factories
    pf = ParquetFile(file)

    # Converting data in to pandas dataFrame
    dataFrame = pf.to_pandas()

    # Converting to CSV
    dataFrame.to_csv('sample.csv', index = None, header=True, date_format='%m/%d/%Y')
    

def list_of_headers(file):
    with open(file) as csv_file:
    # creating an object of csv reader
    # with the delimiter as ,
        csv_reader = csv.reader(csv_file, delimiter=',')

    # loop to iterate through the rows of csv
        for row in csv_reader:

        # adding the first row
            list_of_column_names.append(row)

        # breaking the loop after the
        # first iteration itself
            break
        
        set_of_column_names = set(list_of_column_names[0])
        return set_of_column_names
    
list_of_column_names = []
list_of_possible_phone = [
    "Phone", "number", "contact", "phone", "Phone number"
]
def findZipandPhone (file):
    with open(file, 'rb') as f:
        reader = cs.DictReader(f)
        flag = False
        for row in reader:  # loop through each rows
            if flag:
                break
            for phoneIndex in range(len(list_of_column_names[0])):  # loop through each items in the row
                if isPhoneNumber(
                        str(row[list_of_column_names[0][phoneIndex]])) == True and list_of_column_names[0][
                        phoneIndex] in list_of_possible_phone:  # if the item matches phonenumber test and its column title is phone number or number or phone or etc
                    flag = True
                    #print(row[list_of_column_names[0][phoneIndex]])  #print that item
                    break
            for zipIndex in range(len(list_of_column_names[0])):  # loop through each items in the row
                if isZipCode(str(row[list_of_column_names[0][zipIndex]])) == True:  # if the item matches phonenumber test and its column title is phone number or number or phone or etc
                    flag = True
                    #print(row[list_of_column_names[0][zipIndex]])  #print that item
                    break

    print(f"Column {zipIndex + 1} look like its for zip codes")

    print(f"Column {phoneIndex + 1} look like its for phone numbers")
    