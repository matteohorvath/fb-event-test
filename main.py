import os
from facebook_business.api import FacebookAdsApi
from dotenv import load_dotenv

load_dotenv()
from facebook_business.adobjects.page import Page

# Replace these with your own credentials
my_app_id = os.getenv('APP_ID')
my_app_secret = os.getenv('APP_SECRET')
my_access_token = os.getenv('ACCESS_TOKEN')
page_id = os.getenv('PAGE_ID')

# Initialize the SDK (this “logs in” your application)
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

# Get the Page object and request events
page = Page(page_id)
fields = ['id', 'name', 'start_time', 'end_time', 'place', 'description']
params = {}  # additional parameters can be added here

events = page.get_events(fields=fields, params=params)
for event in events:
    print(event)
