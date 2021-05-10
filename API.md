# API
## Endpoints
### Postcode Lookup
#### Endpoint
`https://addresses.york.gov.uk/api/address/lookupbypostcode/<POSTCODE>` 
- The postcode element has no space.
#### Response
A list of addresses belonging to that postcode. With associated metadata of their addresses.  
`https://addresses.york.gov.uk/api/address/lookupbypostcode/YO17DP`
```json
[
  {
    "county": "York",
    "department": null,
    "easting": 460013,
    "locality": null,
    "northing": 451947,
    "organisation": "Circles Cafe York Ltd",
    "paoDescription": "East Lodge",
    "parish": null,
    "poBox": null,
    "postcode": "YO1 7DP",
    "saoDescription": null,
    "shortAddress": "Circles Cafe York Ltd, East Lodge, Museum Street, York, YO1 7DP",
    "street": "Museum Street",
    "town": "York",
    "uprn": "010007240884",
    "ward": "Guildhall"
  }
]
```
There are several values however the important one is the `uprn` (unique property resource number). I will eventually write a script that allows you to input your postcode in order to get your `uprn`.
### Next Waste Lookup 
#### Endpoint
This endpoint returns the two **next** dates that waste will be collected.  
`https://waste-api.york.gov.uk/api/GetBinCollectionDataForUprn/<uprn>`
#### Response
```json
{
  "services": [
    {
      "service": "REFUSE",
      "lastCollected": "2021-05-10T00:00:00",
      "nextCollection": "2021-05-24T00:00:00",
      "frequency": "Every alternate Mon",
      "binDescription": "60L GREY RUBBISH SACK x3",
      "wasteType": "General domestic",
      "collectedBy": "City of York Council"
    },
    {
      "service": "RECYCLING",
      "lastCollected": "2021-05-03T00:00:00",
      "nextCollection": "2021-05-17T00:00:00",
      "frequency": "",
      "binDescription": "55L BLACK RECYCLING BOX x3",
      "wasteType": "Paper/card, plastic/cans, glass",
      "collectedBy": "City of York Council"
    }
  ]
}
```
As you can see the timezones are nicely parsed in the ISO-8601 standard which makes them very easy to understand.
### Calendar Waste Lookup
#### Endpoint
This endpoint returns much more inadvance collections. When performing this request on 2021-05-10 it had requests stretching to 2021-11-29.  
`https://waste-api.york.gov.uk/api/GetBinCalendarDataForUprn/<uprn>`
#### Response
Some responses have been omitted.
```json
{
  "collections": [
    {
      "roundType": "REFUSE",
      "date": "2020-12-07T00:00:00"
    },
    {
      "roundType": "RECYCLING",
      "date": "2020-12-14T00:00:00"
    },
    {
      "roundType": "REFUSE",
      "date": "2020-12-19T00:00:00"
    },
    {
      "roundType": "RECYCLING",
      "date": "2020-12-28T00:00:00"
    }
  ]
}
```