import collections
import requests
from ics import Calendar, Event

def get_collection_dates(uprn):
    collections = requests.get('https://waste-api.york.gov.uk/api/GetBinCalendarDataForUprn/{}'.format(uprn)).json()

    bins = {}

    for bin in collections['collections']:
        bin_type = bin['roundType'].lower()

        if bin_type in bins:
            bins[bin_type].append(bin['date'])
        else:
            bins[bin_type] = [bin['date']]

    return bins

def create_calendar(bin_dates):
    c = Calendar()

    for bin in bin_dates:
        for date in bin_dates[bin]:
            bin_event = Event(bin.upper(), date, description="Remember to put out your {} bin".format(bin))
            bin_event.make_all_day()
            c.events.add(bin_event)
            print('{} - {}'.format(bin, date))

    with open('my.ics', 'w') as f:
        f.writelines(c)

def main():
    collections = get_collection_dates()
    create_calendar(collections)

main()