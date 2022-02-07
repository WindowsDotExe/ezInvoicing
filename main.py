# Main Python code for ezInvoicing.
# © Matthew Jacobs - 2022 - All rights reserved.

import reportlab

def generate():
    header = '------- ezInvoicing Generate -------'
    reqCustDetails = True
    while reqCustDetails == True:
        print(header + '\n' + 'First, enter customer details: ')
        custFirstName = input('Customer first name: ')
        custLastName = input('Customer last name: ')
        custPhoneNumber = input('Customer phone number: ')
        print('--- Review Information ---')
        print(('{0} {1} | {2}').format(custFirstName, custLastName, custPhoneNumber))
        confirm = (input('Do the customer details above appear correctly? Enter Y/N: ')).lower()
        if confirm == 'y':
            reqCustDetails = False
        else:
            reqCustDetails = True
    
    print('END OF CUSTOMER DETAILS')


def handleSelection(selection):
    if selection == 1:  # Generate new invoice
        generate()
    else:
        print('Invalid selection.')


def main():
    selection = int(input('Welcome to ezInvoicing. Please select from the following options:' + '\n' + '1) Generate a new invoice' + '\n' + 'Type your numerical choice here: '))
    handleSelection(selection)

main()