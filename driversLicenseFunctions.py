import random
import string

def fake_driverslicense(license,preserveNulls,dob,index,fakefirst,fakelast,new_birthMonth,new_birthYear,new_birthDay,state):
    if not license and preserveNulls == 'Yes':
        pass
    else:
        if not dob: #if no dob, no license generated
            print(f"No drivers license generated for row {index+1} because of missing DOB")
            license = None
        else:
            # declare to use out of the function for fake drivers license
            # we need these variables to generate license for the fake value
            global firstname, lastname, year, day, month
            firstname = fakefirst  # updated fake names and variables
            lastname = fakelast
            if new_birthMonth < 10:
            # adding 0 in front of one digit month or day
                month = f"0{str(new_birthMonth)}"
            else:
                month = str(new_birthMonth)
                                        
            year = str(new_birthYear)
            if new_birthDay < 10:
                day = f"0{str(new_birthDay)}"
            else:
                day = str(new_birthDay)
                                    
            if not state:
                stateUsed = random.choice(list(license_rules))
            else:
                stateUsed = state  # assign state for drivers license

            license = random.choice(license_rules[stateUsed])(month, firstname, lastname, year,day)  # apply function

    return license

def rule1(*args):  # 7 digits #this format
    license_number = str(random.randint(1000000, 9999999))
    return license_number


def rule2(*args):  # 9 digits #this format
    license_number = str(random.randint(100000000, 999999999))
    return license_number


def rule3(*args):  # 1 Letter followed by 8 numbers #this format
    license_number = random.choice(string.ascii_uppercase) + str(
        random.randint(10000000, 99999999))
    return license_number


def rule4(*args):  # 9 digits beginning with 9 #this format
    license_number = str(random.randint(900000000, 999999999))
    return license_number


def rule5(*args):  # 1 Letter followed by 7 numbers #this format
    license_number = random.choice(string.ascii_uppercase) + str(random.randint(1000000, 9999999))
    return license_number


def rule6(*args):  # ##-###-#### #this format
    license_number = f"{str(random.randint(10,99))}-{str(random.randint(100,999))}-{str(random.randint(1000,9999))}"
    return license_number


def rule7(*args):  # 1 Letter followed by 12numbers #this format
    license_number = random.choice(string.ascii_uppercase) + str(random.randint(100000000000, 999999999999))
    return license_number


def rule8(*args):  # L##-###-##-###-# #this format
    license_number = f"{random.choice(string.ascii_uppercase)}{str(random.randint(10,99))}-{str(random.randint(100,999))}-{str(random.randint(10,99))}-{str(random.randint(100,999))}-{str(random.randint(1,9))}"
    return license_number


def rule9(*args):  # 2L6N1L #this format
    license_number = f"{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{str(random.randint(100000,999999))}{random.choice(string.ascii_uppercase)}"
    return license_number


def rule10(*args):  # L###-####-#### #this format
    license_number = f"{random.choice(string.ascii_uppercase)}{str(random.randint(100,999))}-{str(random.randint(1000,9999))}-{str(random.randint(1000,9999))}"
    return license_number


def rule11(*args):  # -##-####  #this format
    license_number = f"{str(random.randint(1000,9999))}-{str(random.randint(10,99))}-{str(random.randint(1000,9999))}"
    return license_number


def rule12(*args):  # 3N2L4N
    license_number = f"{str(random.randint(100,999))}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{str(random.randint(1000,9999))}"
    return license_number


def rule13(*args):  # L##-###-####
    license_number = f"{random.choice(string.ascii_uppercase)}{str(random.randint(10,99))}-{str(random.randint(10,99))}-{str(random.randint(1000,9999))}"
    return license_number


def rule14(*args):  # L##-###-###
    license_number = f"{random.choice(string.ascii_uppercase)}{str(random.randint(10,99))}-{str(random.randint(100,999))}-{str(random.randint(100,999))}"
    return license_number


def rule15(*args):  # L-###-###-###-###
    license_number = f"{random.choice(string.ascii_uppercase)}-{str(random.randint(100,999))}-{str(random.randint(100,999))}-{str(random.randint(100,999))}-{str(random.randint(100,999))}"
    return license_number


def rule16(*args):  # 1 Letter followed by 9 numbers
    license_number = random.choice(string.ascii_uppercase) + str(random.randint(100000000, 999999999))
    return license_number


def rule17(*args):
    license_number = f"{str(random.randint(10,99))} {str(random.randint(100,999))} {str(random.randint(100,999))}"
    return license_number


# rule18 reqquires the license issued number


def rule19(*args):
    license_number = str(random.randint(10000000, 99999999))
    return license_number


def rule20(*args):  # 7 numbers followed by 1 Letter
    license_number = str(random.randint(1000000, 9999999)) + random.choice(string.ascii_uppercase)
    return license_number


def rule21(*args):  # 3L ** 2L3N1l1N
    license_number = f"{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}**{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{str(random.randint(100,999))}{random.choice(string.ascii_uppercase)}{str(random.randint(1,9))}"
    return license_number


def rule22(*args):  # 1 Letter followed by 6 numbers
    license_number = random.choice(string.ascii_uppercase) + str(random.randint(100000, 999999))
    return license_number


def rule23(*args):  # L###-####-####-##
    license_number = f"{random.choice(string.ascii_uppercase)}{str(random.randint(100,999))}-{str(random.randint(1000,9999))}-{str(random.randint(1000,9999))}-{str(random.randint(10,99))}"
    return license_number


def rule24(*args):  # ######-###
    license_number = f"{str(random.randint(100000,999999))}-{str(random.randint(100,999))}"
    return license_number


def rule25(*args):  # social security
    license_number = f"{str(random.randint(100,999))}-{str(random.randint(10,99))}-{str(random.randint(1000,9999))}"
    return license_number


def rule26(*args):
    birthmonth = month
    firstandlastoflastname = f"{lastname[0].capitalize()}{lastname[-1].capitalize()}{firstname[0].capitalize()}"
    birthyear = year[-2:]
    birthday = day

    license_number = f"{birthmonth}{firstandlastoflastname}{birthyear}{birthday}{random.randint(0,9)}"
    return license_number


def rule27(*args):  # L####-#####-#####
    license_number = f"{random.choice(string.ascii_uppercase)}{str(random.randint(1000,9999))}-{str(random.randint(10000,99999))}-{str(random.randint(10000,99999))}"
    return license_number


def rule28(*args):  # ### ### ###
    license_number = f"{str(random.randint(100,999))} {str(random.randint(100,999))} {str(random.randint(100,999))}"
    return license_number


def rule29(*args):  # 12 numbers
    license_number = str(random.randint(100000000000, 999999999999))
    return license_number


def rule30(*args):  # North Dakota
    if len(lastname) <= 2:
        first3last = f"{lastname[0].capitalize()}{lastname[1].capitalize()}X"
    else:
        first3last = f"{lastname[0].capitalize()}{lastname[1].capitalize()}{lastname[2].capitalize()}"
    birthyear = year[-2:]
    license_number = f"{first3last}{birthyear}{random.randint(1000,9999)}"
    return license_number


def rule31(*args):  # 2L6N
    license_number = f"{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{str(random.randint(100000,999999))}"
    return license_number


def rule32(*args):  # 2L9N
    license_number = f"{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{str(random.randint(100000000,999999999))}"
    return license_number


def rule33(*args):  # L ### ### ### ###
    license_number = f"{random.choice(string.ascii_uppercase)} {str(random.randint(100,999))} {str(random.randint(100,999))} {str(random.randint(100,999))} {str(random.randint(100,999))}"
    return license_number


def rule34(*args):
    birthmonth = month
    birthyear = year[-2:]
    birthday = day

    license_number = f"{birthmonth}{random.randint(100,999)}{birthyear}41{birthday}"
    return license_number


def rule35(*args):  # 10 digits #this format
    license_number = str(random.randint(1000000000, 9999999999))
    return license_number


license_rules = {  #if the state is "key" apply key "function" to generate drivers license
    "AL": [rule1],
    "AK": [rule1],
    "DE": [rule1],
    "ME": [rule1],
    "OR": [rule1],
    "DC": [rule1],
    "WV": [rule1, rule22],
    "RI": [rule1],
    "AZ": [rule2, rule3],
    "CT": [rule2],
    "GA": [rule2],
    "IA": [rule2, rule12],
    "LA": [rule2],
    "MT": [rule2, rule34],
    "NM": [rule2],
    "SC": [rule2],
    "UT": [rule2],
    "TN": [rule2, rule19],
    "HI": [rule3],
    "NE": [rule3],
    "VA": [rule3, rule13],
    "AR": [rule4],
    "CA": [rule5],
    "CO": [rule6],
    "FL": [rule7, rule8],
    "ID": [rule9],
    "IL": [rule10],
    "IN": [rule11],
    "KS": [rule13],
    "KY": [rule14],
    "MD": [rule15],
    "MA": [rule16],
    "MO": [rule16],
    "OK": [rule16],
    "PA": [rule17],
    "SD": [rule19],
    "TX": [rule19],
    "VT": [rule19, rule20],
    "WA": [rule21],
    "WI": [rule23],
    "WY": [rule24],
    "MS": [rule25],
    "NH": [rule26],
    "NJ": [rule27],
    "NY": [rule28],
    "NC": [rule29],
    "ND": [rule30],
    "OH": [rule31],
    "MI": [rule7, rule33],
    "MN": [rule7],
    "NV": [rule35]
}

licenseForMissingFields = [rule2(), rule3(), rule6(), rule8(), rule9(), rule21(), rule33()] #license rule to apply for the cases of no name, dob, state colum