#imports
import random #randomize info
import datetime  #find the current-year and time
from time import sleep # let the program wait if anyone wants to view some info
import webbrowser # this is triggered when the amount of cards is less than or equal to 0

#meraj-rashidi ccgenerator advanced
#github account: https://www.github.com/merajrashidi69

url = 'https://www.github.com/merajrashidi69' 

#file which is opened and ready to write cards being generated from main() function
file = open('credit_cards.txt','w')

#main_function
def main():

    ccnumber = ''
    fullname = ''
    fix_day = '0'
    fix_month = '0'
    now = datetime.datetime.now()
    current_year = now.year
    random_year_number = random.randint(1,6)
    year = current_year + random_year_number
    american_express_ccstartnums = ['34','37']
    mastercard_ccstartnums = ['51','55']
    maestro_nums = ['5','6']
    month = random.randint(1,12)

    #non-hardcoded-setting
    if month < 10:
        fix_month += str(month)
    else:
        fix_month = ''
        fix_month += str(month)

    day = random.randint(1,31)

    if day < 10:
        fix_day += str(day)
    else:
        fix_day = ''
        fix_day += str(day)


    #types of cards
    card_types = ['VISA','MasterCard','American Express','JCB','Discover']
    cardtype = random.choice(card_types)#random_selection

    #card-types&card-digits/numbers
    if cardtype == 'VISA':
        random_digits = random.randint(100000000000000,999999999999999)
        ccnumber += '4'
        ccnumber += str(random_digits)

    elif cardtype == 'MasterCard':
        random_digits = random.randint(100000000000000,999999999999999)
        ccnumber += random.choice(mastercard_ccstartnums)
        ccnumber += str(random_digits)


    elif cardtype == 'American Express': #15 digits
        random_digits = random.randint(1000000000000,9999999999999)
        ccnumber += random.choice(american_express_ccstartnums)
        ccnumber += str(random_digits)

    elif cardtype == 'JCB': #16 digits
        random_digits = random.randint(10000000000000,99999999999999)
        ccnumber += '35'
        ccnumber += str(random_digits)

    elif cardtype == 'Discover':#16 digits
        random_digits = random.randint(100000000000,999999999999)
        ccnumber += '6011'
        ccnumber += str(random_digits)
        

    #file-collection-start
    fnames = open('fnames.txt','r')
    fname = random.choice(fnames.readlines())
    fnames.close()

    lnames = open('lnames.txt','r')
    lname = random.choice(lnames.readlines())
    lnames.close()

    fullname = fname.rstrip('\n') + ' ' + lname.rstrip('\n')

    countries = open('countries.txt','r')
    country = random.choice(countries.readlines())
    countries.close()

    addresses = open('streetnames.txt','r')
    street_name = random.choice(addresses.readlines())
    addresses.close()

    street_types = open('streetsuffix.txt','r')
    street_type = random.choice(street_types.readlines())
    street_types.close()
    #file-collection-end


    #data-collection
    zipcode = random.randint(1000,9999)
    street_number = random.randint(1,99999)
    cvv = random.randint(100,999)
    address = str(street_number) + ' ' + street_name.rstrip('\n') + ' ' + street_type.rstrip('\n')

    #print(f'Card type: {cardtype}\nCard Number: {ccnumber}\nExpire Date: {fix_day}/{fix_month}/{year}\nCVV: {cvv}\nName: {fullname}\nAddress: {address}\nZip: {zipcode}\nCountry: {country}')
    file.write(f'\n\nCard type: {cardtype}\nCard Number: {ccnumber}\nExpire Date: {fix_day}/{fix_month}/{year}\nCVV: {cvv}\nName: {fullname}\nAddress: {address}\nZip: {zipcode}\nCountry: {country}')

#tell the user for an amount of cards
amount = int(input('How many cards? '))

if amount<=0:
    webbrowser.open(url)

for x in range(0,amount):
    main()
    #continue
file.close() #at the end, close the file
#line 116, end!

#credits

print('''
Author: Meraj-Rashidi
Github: https://www.github.com/merajrashidi69
Thanks!
''')

sleep(10)
#line: 133, end!








