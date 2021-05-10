import requests
import json

from requests.api import options, post

def get_postcode():
    postcode = input("Please enter your postcode: ")

    postcode.replace(' ', '') # Removes spaces in postcode
    return postcode

def get_addresses(postcode):
    addresses = requests.get('https://addresses.york.gov.uk/api/address/lookupbypostcode/{}'.format(postcode)).json()

    return addresses

def select_address(addresses):
    for i in range(1, len(addresses)):
        print("[{0:03d}] - {1}".format(i, addresses[i]['shortAddress']))
    
    try:
        option = int(input("Please enter the number of your address: "))
    except ValueError:
        print("You must specify an integer value of number.")
        select_address(addresses)

    if option > len(addresses) - 1:
        print("You have picked an option not in range. Please try again.")
        select_address(addresses)
    
    return addresses[option]
    

def main():
    print("Hello; this script will attempt to locate your UPRN (Unique Property Resource Number).")
    
    postcode = get_postcode()

    addresses = get_addresses(postcode)

    house = select_address(addresses)
    
    print("Your UPRN is {}".format(house['uprn']))

main()