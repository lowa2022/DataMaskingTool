import random
from datetime import date
from dateutil.relativedelta import relativedelta
import datetime
from faker import Faker
from simpleFunctions import TIN,vin_generator,policy_generator,vinWithModel,claimNumberGenerator,GetValidDob,firstnameemail,lastnameemail,fLastNameemail,lastNameEmailDomain,firstNameEmailDomain,fLastNameEmailDomain
fake = Faker('en_US')  # US
locales = 'en_IN', 'en_US', 'es_ES', 'en_PH'  # list of the locales
faker = Faker(locales)  # Diversified

set_of_fake_ssns = set() #set to check if the ssn is already used

def fake_ssn(ssn,preserveNulls):
    if not ssn and preserveNulls == 'Yes': #if no ssn value and preseve null is on, leave it as it is
        pass
    else:
        if '-' in ssn: # only dases if the original had dashes, otherwise empty spaces
            while True:
                fakeSocial = fake.ssn()
                if fakeSocial not in set_of_fake_ssns:
                    break
            ssn = fakeSocial
                                    
        else:
            while True:
                fakeSocial = fake.ssn()
                if fakeSocial not in set_of_fake_ssns:
                    break
            ssn = fakeSocial.translate({ord("-"): None})  # dont use dashes
    return ssn

def fake_gender(gender,preserveNull):
    if not gender and preserveNull == 'No':
        genderList = ['Male','Female','Other']
        gender = random.choice(genderList)
    else:
        gender = gender.strip(' ')
        gender = gender.capitalize()
    return gender

def fake_fName(gender,fName,preserveNull):
    if not fName and preserveNull == "Yes":
        pass
    else:
        if gender == "Male" or "M":
            fName = faker.first_name_male()
        elif gender == 'Female' or 'F':
            fName = faker.first_name_female()  # female names for females
        else:
            fName = faker.first_name()
    return fName

def fake_lName(lName, preserveNull):
    if not lName and preserveNull == 'Yes':
        pass
    else:
        lName = faker.last_name()
    return lName

def fake_Street(street, preserveNull):
    if not street and preserveNull == 'Yes':
        pass
    else:
        street = fake.street_address()
    return street

def fake_Phone(phone,preserveNull):
    if not phone and preserveNull == 'Yes':  # for empty cells
        pass
    else:
        phone = fake.phone_number()
    return phone

def fake_licensePlate(licensePlate,preserveNull):
    if not licensePlate and preserveNull == 'Yes':  # for empty cells
        pass
    else:
        licensePlate = fake.license_plate()
    return licensePlate

def fake_claimNumber(claimNumber,preserveNull):
    if not claimNumber and preserveNull == 'Yes':  # for empty cells
        pass
    else:
        claimNumber = claimNumberGenerator()
    return claimNumber

def fake_policyNumber(policyNumber,preserveNull):
    if not policyNumber and preserveNull == 'Yes':  # for empty cells
        pass
    else:
        policyNumber = policy_generator()
    return policyNumber

def fake_VIN(vinNumber,preserveNull,preserveVINModel):
    if not vinNumber and preserveNull == 'Yes':
        pass
    elif not vinNumber and preserveNull == 'No':
        vinNumber = vin_generator()
    else:
        if preserveVINModel == 'Yes':
            vinMakeModel = vinNumber[9]
            vinNumber = vinWithModel(vinMakeModel)
        else:
            vinNumber = vin_generator()
    return vinNumber

def fake_TIN(tinNumber,preserveNull):
    if not tinNumber and preserveNull == 'Yes':  # for empty cells
        pass
    else:
        tinNumber = TIN()
    return tinNumber

def fake_userID(userID,preserveNull):
    if not userID and preserveNull == 'Yes':  # for empty cells
        pass
    else:
        userID = fake.user_name()
    return userID

def fake_dob(dob,preserveNulls):
    if not dob and preserveNulls == 'Yes':
        pass
    elif not dob and preserveNulls == 'No': #generate fake dob in case of preserve null off
        current_date = date.today()  #todays date
        fake_date = current_date - relativedelta(years=30) #minus thirty years
        fake_year = fake_date.year #get the yea
        dob = GetValidDob(fake_year) #generate dob
    else:
        date_str = dob  # get the person's dob
        date_obj = datetime.datetime.strptime(date_str,'%m/%d/%Y')  # strip the time in format
        birthYear = date_obj.year  # get the birth year
        dob = GetValidDob(birthYear)  # using get Birth year function, generate new valid DOB
    return dob


def fake_email(first_name,last_name,index,email,preserveEmailDomain,preserveNulls):
    
    preEmail = email  # get original email
    if not "@" in preEmail: #incase there is an email but the domain is missing
        print(f"No fake Email generated for row {index+1} because of missing domain")
        emailDomain = "missing"                    
    else:
        emailDomain = preEmail[preEmail.index('@') +1:]  # strip the domain for preservation
    print(emailDomain)       
    emailfunctions = [
        firstnameemail(first_name,last_name),
        lastnameemail(first_name,last_name),
        fLastNameemail(first_name,last_name)
    ]  # use from these fucntions
                    
    emailFunctionsDomain = [
        firstNameEmailDomain(first_name,last_name,emailDomain),
        lastNameEmailDomain(first_name,last_name,emailDomain),
        fLastNameEmailDomain(first_name,last_name,emailDomain)
    ]  # list of functions for generating emails with the same domain:

    if preserveEmailDomain == 'Yes':  # incase the domainpreservation is on
        
        if emailDomain == "missing": #if emailDomain is missing
            email = None
        elif not first_name or not last_name:
            email = fake.email() 
        else:
            email = random.choice(emailFunctionsDomain)  # choose from the functions
    else:
        email = random.choice(emailfunctions)

    return email

