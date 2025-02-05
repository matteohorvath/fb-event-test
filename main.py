from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.page import Page

# Replace these with your own credentials
my_app_id = '1500993981288343'
my_app_secret = '70e019734741ac53a69fa0a497bed38c'
my_access_token = 'EAAVVJWUQj5cBO6Y7ZAZCdetZBIHBf4hf9VeLeOGJOof3rkRip2fJZBIHKOSDKxRzzsPAVZBIpGQDWkZBudTqXLwIMXn05wWTMpmOMI49HZAJAYYUEDdGDcwZCm7blYaqMhLSU4UO9HJwivpc01yyWOOFKMIOZBKjsLKOC5DoHwZCddI9OYVd8cm2UiLZCd8FpPBDXlb1LXJH0smwlJLmgZAXZAxUXnpHXGKUZD'
page_id = "317276771466166"

# Initialize the SDK (this “logs in” your application)
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

# Get the Page object and request events
page = Page(page_id)
fields = ['id', 'name', 'start_time', 'end_time', 'place', 'description']
params = {}  # additional parameters can be added here

events = page.get_events(fields=fields, params=params)
for event in events:
    print(event)
