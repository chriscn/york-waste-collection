# York Waste Collection
[York Council](https://www.york.gov.uk/HouseholdWaste) provide an online calendar to see the next time your waste should be collected. On the backend they use an API. This GitHub project aims to document a few of their APIs and how to use them.  
Details of which can be found in the [API](./API.md) document.
## Project
### `get-uprn.py`
Simple python script that will get your uprn, has some safety checks implemented.
### API
The API provided isn't great, and I would want to add some more endpoints that are much easier to implement in your projects. This will serve as the backend for the website that I may develop.
### Calendar
The main idea behind this project is to allow a front end user to create two types of calendar for their bin collections. 
#### iCS Subscription
This is a subscription that will automatically update as and when the York API will update. I am wanting to also implement some caching involved so that they don't get loads of requests from my IP and me being blocked :-(  
After doing some research it does look like you can add [alerts](https://stackoverflow.com/questions/14892422/ics-with-alert); Apple Calendar has the option of removing them, this would require some more extensive code as users might want customisable alerts.
#### iCal Calendar
A simple downloadable calendar that you can import into your Calendar app of choice, I think the advantage of this is it would allow you to add alerts before. More customisable.