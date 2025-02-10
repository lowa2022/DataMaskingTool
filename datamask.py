import unicodecsv as cs
from faker import Faker
import random
import configparser
import time
from simpleFunctions import *
from anonymFunctions import *
from driversLicenseFunctions import *


# record start time
start = time.time()  # start time

config = configparser.ConfigParser()  # assign configparser to config
config.read('config.ini')  # read config.ini file

fake = Faker('en_US')  # US
locales = 'en_IN', 'en_US', 'es_ES', 'en_PH'  # list of the locales
faker = Faker(locales)  # Diversified


# faker = Faker(config['General']['Locale']) #not working
def anonymize(sourcefile):
    # Anonymizes the given original data to anonymized form
    with open(sourcefile, 'rb') as f:  # automatically close reldata.csv when it’s not needed anymore
        with open("fakedata_"+sourcefile+".csv", 'wb') as o:
            # Use the DictReader to easily extract fields
            reader = cs.DictReader(f)
            writer = cs.DictWriter(o, reader.fieldnames)
            # write header only if required
            if config["General"]["WriteHeaderInOutput"] == "Yes":
                writer.writeheader()  # writes the headers
            else:
                pass
            
            index = 1 #tracks rows

            for row in reader:  #functions are applied row by row
                if not config['Mappings']['SSN'] in set_of_headers: #if no ssn column do following
                    #gender
                    if not config['Mappings']['Gender'] in set_of_headers: #if no gender column
                        pass #do nothing
                    else: 
                        row[config['Mappings']['Gender']] = fake_gender(row[config['Mappings']['Gender']],config['General']['PreserveNulls']) #call fake gender funciton
                    #first
                    if not config['Mappings']['First'] in set_of_headers:
                        pass
                    else:
                        row[config['Mappings']['First']] = fake_fName(row[config['Mappings']['Gender']],row[config['Mappings']['First']],config['General']['PreserveNulls'])
                    #last
                    if not config['Mappings']['Last'] in set_of_headers:
                        pass
                    else:
                        row[config['Mappings']['Last']] = fake_lName(row[config['Mappings']['Last']],config['General']['PreserveNulls'])
                    #street
                    if not config['Mappings']['Street'] in set_of_headers:
                        pass
                    else:
                        row[config['Mappings']['Street']] = fake_Street(row[config['Mappings']['Street']],config['General']['PreserveNulls'])
                    #phone
                    if not config['Mappings']['Phone'] in set_of_headers:
                        pass
                    else:
                        row[config['Mappings']['Phone']] = fake_Phone(row[config['Mappings']['Phone']],config['General']['PreserveNulls'])
                    #licenseplate
                    if not config['Mappings']['License Plate'] in set_of_headers:
                        pass
                    else:
                        row[config['Mappings']['License Plate']] = fake_licensePlate(row[config['Mappings']['License Plate']],config['General']['PreserveNulls'])
                    #claim number
                    if not config['Mappings']['Claim number'] in set_of_headers:
                        pass
                    else:
                        row[config['Mappings']['Claim number']] = fake_claimNumber(row[config['Mappings']['Claim number']],config['General']['PreserveNulls'])
                    #policy number
                    if not config['Mappings']['Policy Number'] in set_of_headers:
                        pass
                    else:
                        row[config['Mappings']['Policy Number']] = fake_policyNumber(row[config['Mappings']['Policy Number']],config['General']['PreserveNulls'])
                    #vin
                    if not config['Mappings']['VIN'] in set_of_headers:
                        pass
                    else:
                        row[config['Mappings']['VIN']] = fake_VIN(row[config['Mappings']['VIN']],config['General']['PreserveNulls'],config['General']['PreserveVINMakeModel'])
                    #tin
                    if not config['Mappings']['TIN'] in set_of_headers:
                        pass
                    else:
                        row[config['Mappings']['TIN']] =fake_TIN(row[config['Mappings']['TIN']],config['General']['PreserveNulls'])
                    #user id
                    if not config['Mappings']['User ID'] in set_of_headers:
                        pass
                    else:
                        row[config['Mappings']['User ID']] = fake_userID(row[config['Mappings']['User ID']],config['General']['PreserveNulls'])
                    
                    #dob
                    if not config['Mappings']['DOB'] in set_of_headers:
                        pass
                    else:
                        row[config['Mappings']['DOB']] = fake_dob(row[config['Mappings']['DOB']],config['General']['PreserveNulls'])
                    
                    # for fake person's dob
                    if not config['Mappings']['DOB'] in set_of_headers:
                        pass
                    else:
                        if not row[config['Mappings']['DOB']]:
                            pass
                        else:
                            date_str = row[config['Mappings']['DOB']]
                            # getting the fake persons dob to generate new data
                            new_date_obj = datetime.datetime.strptime(date_str, '%m/%d/%Y')  # strip in format
                            new_birthYear = new_date_obj.year  # get year
                            new_birthMonth = new_date_obj.month  # get month
                            new_birthDay = new_date_obj.day  # get day
                    
                    #email
                    if not row[config['Mappings']['Email']]:
                        pass
                    else:
                        if config['General']['PreserveNulls'] == "Yes":
                            pass
                        elif not config['Mappings']['First'] in set_of_headers or not config['Mappings']['Last'] in set_of_headers:
                            row[config['Mappings']['Email']] = fake.email()
                        else:
                            row[config['Mappings']['Email']] = fake_email(row[config['Mappings']['First']],row[config['Mappings']['Last']],index,row[config['Mappings']['Email']],config['General']['PreserveEmailDomain'],config['General']['PreserveNulls'])

                    
                    #license
                    
                    if config['Mappings']['Drivers license'] not in set_of_headers:
                        pass
                    else:
                        if not config['Mappings']['Drivers license'] and config['General']['PreserveNulls']:
                            pass
                        elif not config['Mappings']['First'] in set_of_headers or not config['Mappings']['Last'] in set_of_headers or not config['Mappings']['State'] in set_of_headers:
                            row[config['Mappings']['Drivers License']] = random.choice(licenseForMissingFields) #if first name, last name or state missing, create license anyway
                        else:
                            row[config['Mappings']['Drivers license']] = fake_driverslicense(row[config['Mappings']['Drivers license']],config['General']['PreserveNulls'],row[config['Mappings']['DOB']],index,row[config['Mappings']['First']],row[config['Mappings']['Last']],new_birthMonth,new_birthYear,new_birthDay,row[config['Mappings']['State']])
 
                else: #if it contains ssns
                    if row[config['Mappings']['SSN']] in preSSN and row[config['Mappings']['SSN']] != "":  # if ssn is seen before
                        print(f"Duplicate ssn {row[config['Mappings']['SSN']]} found in row {index+1} and around {preSSN.index(row[config['Mappings']['SSN']])+2}")
                        row[config['Mappings']['SSN']] = ssnDict[row[config['Mappings']['SSN']]]  # fke ssn is the value of the current ssn as key
                        row[config['Mappings']['First']] = fnameDict[row[config['Mappings']['SSN']]]  # first name of current row is the same as the firstname mapped to the current ssn
                        row[config['Mappings']['Last']] = lnameDict[row[config['Mappings']['SSN']]]
                        row[config['Mappings']['Street']] = fake.street_address()
                        row[config['Mappings']['DOB']] = dateDict[row[config['Mappings']['SSN']]]
                        row[config['Mappings']['Gender']] = genderDict[row[config['Mappings']['SSN']]]
                        row[config['Mappings']['Email']] = fake.email()
                        row[config['Mappings']['Phone']] = fake.phone_number()
                        row[config['Mappings']['Drivers license']] = driversLicenseDict[row[config['Mappings']['SSN']]]
                        row[config['Mappings']['Policy Number']] = policy_generator()
                        row[config['Mappings']['Claim Number']] = claimNumberGenerator()
                        row[config['Mappings']['VIN']] = vin_generator()
                        row[config['Mappings']['TIN']] = TIN()
                        row[config['Mappings']['User ID']] = fake.user_name()
                        row[config['Mappings']['License Plate']] = fake.license_plate()
                        
                        

                    else:
                        preSSN.append(row[config['Mappings']['SSN']])  # add original ssn to the list

                        # if gender in list of column names
                        if not config['Mappings']['Gender'] in set_of_headers:
                            pass
                        else:
                            row[config['Mappings']['Gender']] = fake_gender(row[config['Mappings']['Gender']],config['General']['PreserveNulls'])
                        if not config['Mappings']['First'] in set_of_headers:
                            pass
                        else:
                            row[config['Mappings']['First']] = fake_fName(row[config['Mappings']['Gender']],row[config['Mappings']['First']],config['General']['PreserveNulls'])

                        if not config['Mappings']['Last'] in set_of_headers:
                            pass
                        else:
                            row[config['Mappings']['Last']] = fake_lName(row[config['Mappings']['Last']],config['General']['PreserveNulls'])
                    
                        if not config['Mappings']['Street'] in set_of_headers:
                            pass
                        else:
                            row[config['Mappings']['Street']] = fake_Street(row[config['Mappings']['Street']],config['General']['PreserveNulls'])
                    
                        if not config['Mappings']['Phone'] in set_of_headers:
                            pass
                        else:
                            row[config['Mappings']['Phone']] = fake_Phone(row[config['Mappings']['Phone']],config['General']['PreserveNulls'])
                    
                        if not config['Mappings']['License Plate'] in set_of_headers:
                            pass
                        else:
                            row[config['Mappings']['License Plate']] = fake_licensePlate(row[config['Mappings']['License Plate']],config['General']['PreserveNulls'])
                    
                        if not config['Mappings']['Claim number'] in set_of_headers:
                            pass
                        else:
                            row[config['Mappings']['Claim number']] = fake_claimNumber(row[config['Mappings']['Claim number']],config['General']['PreserveNulls'])

                        if not config['Mappings']['Policy Number'] in set_of_headers:
                            pass
                        else:
                            row[config['Mappings']['Policy Number']] = fake_policyNumber(row[config['Mappings']['Policy Number']],config['General']['PreserveNulls'])

                        if not config['Mappings']['VIN'] in set_of_headers:
                            pass
                        else:
                            row[config['Mappings']['VIN']] = fake_VIN(row[config['Mappings']['VIN']],config['General']['PreserveNulls'],config['General']['PreserveVINMakeModel'])

                        if not config['Mappings']['TIN'] in set_of_headers:
                            pass
                        else:
                            row[config['Mappings']['TIN']] =fake_TIN(row[config['Mappings']['TIN']],config['General']['PreserveNulls'])

                        if not config['Mappings']['User ID'] in set_of_headers:
                            pass
                        else:
                            row[config['Mappings']['User ID']] = fake_userID(row[config['Mappings']['User ID']],config['General']['PreserveNulls'])

                        # dates according to users locale
                        if not config['Mappings']['DOB'] in set_of_headers:
                            pass
                        else:
                            row[config['Mappings']['DOB']] = fake_dob(row[config['Mappings']['DOB']],config['General']['PreserveNulls'])

                        # for fake person's dob
                        if not row[config['Mappings']['DOB']]:
                            pass
                        else:
                            date_str = row[config['Mappings']['DOB']]
                            # getting the fake persons dob to generate new data
                            new_date_obj = datetime.datetime.strptime(date_str, '%m/%d/%Y')  # strip in format
                            new_birthYear = new_date_obj.year  # get year
                            new_birthMonth = new_date_obj.month  # get month
                            new_birthDay = new_date_obj.day  # get day

                        # ssn

                        if config['Mappings']['SSN'] not in set_of_headers:
                            pass
                        else:
                            row[config['Mappings']['SSN']] = fake_ssn(row[config['Mappings']['SSN']],config['General']['PreserveNulls'])

                        # email
                        if not row[config['Mappings']['Email']]:
                            pass
                        else:
                            if config['General']['PreserveNulls'] == "Yes":
                                pass
                            elif not config['Mappings']['First'] in set_of_headers or not config['Mappings']['Last'] in set_of_headers:
                                row[config['Mappings']['Email']] = fake.email()
                            else:
                                row[config['Mappings']['Email']] = fake_email(row[config['Mappings']['First']],row[config['Mappings']['Last']],index,row[config['Mappings']['Email']],config['General']['PreserveEmailDomain'],config['General']['PreserveNulls'])

                        if config['Mappings']['Drivers license'] not in set_of_headers:
                            pass
                        else:
                            if not config['Mappings']['Drivers license'] and config['General']['PreserveNulls']:
                                pass
                            elif not config['Mappings']['First'] in set_of_headers or not config['Mappings']['Last'] in set_of_headers or not config['Mappings']['State'] in set_of_headers:
                                row[config['Mappings']['Drivers License']] = random.choice(licenseForMissingFields) #if first name, last name or state missing, create license anyway
                            else:
                                row[config['Mappings']['Drivers license']] = fake_driverslicense(row[config['Mappings']['Drivers license']],config['General']['PreserveNulls'],row[config['Mappings']['DOB']],index,row[config['Mappings']['First']],row[config['Mappings']['Last']],new_birthMonth,new_birthYear,new_birthDay,row[config['Mappings']['State']])

                        postSSN.append(row[config['Mappings']['SSN']])
                        postFName.append(row[config['Mappings']['First']])
                        postLName.append(row[config['Mappings']['Last']])
                        postDate.append(row[config['Mappings']['DOB']])
                        postGender.append(row[config['Mappings']['Gender']])
                        postDriversLicense.append(row[config['Mappings']['Drivers license']])
                        set_of_fake_ssns.add(row[config['Mappings']['SSN']])

                        for i in range(len(preSSN)):  # adding to dictionary
                            ssnDict[preSSN[i]] = postSSN[i]
                            fnameDict[postSSN[i]] = postFName[i]
                            lnameDict[postSSN[i]] = postLName[i]
                            dateDict[postSSN[i]] = postDate[i]
                            genderDict[postSSN[i]] = postGender[i]
                            driversLicenseDict[postSSN[i]] = postDriversLicense[i]
                        
                index += 1

                writer.writerow(row)

# choose the source file

sourcefile = input("Input filename: ")

if sourcefile.endswith(".xlsx"): #if excel file
    xlsxtocsv(sourcefile) #change to csv
    sourcefile = 'sample.csv'
    
elif sourcefile.endswith(".parquet"):
    parquetTocsv(sourcefile) #change to csv
    sourcefile = 'sample.csv'
else:
    pass

list_of_headers(sourcefile) #call function list_of_header which adds headers to a set and generated the list for column names
set_of_headers = list_of_headers(sourcefile) #the set generated above is assigned to variable_set_of_headers

# printing the result
print("List of column names :",list_of_column_names[0])
findZipandPhone(sourcefile) #finds the zip and phone number

# for recording the new fake names that has the same ssn and mapping them.
preSSN, postSSN, postFName, postLName, postDate, postGender, postDriversLicense= [], [], [], [], [], [], [] #list to add pre and post fields
ssnDict, fnameDict, lnameDict, dateDict, genderDict, driversLicenseDict = {}, {}, {}, {}, {}, {} #dictionary for mapping

anonymize(sourcefile)

# record end time

end = time.time()

# print the difference between start
# and end time in secs
print("Execution time :" + str(end - start) + "s.")
