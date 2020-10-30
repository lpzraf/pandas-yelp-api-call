import pandas as pd
import requests

api_url = "https://api.yelp.com/v3/businesses/search"


# Param dict according to the APIs documentation
params = {"term": "bookstore",
          "location": "San Francisco"}


# header dict w/API key according to documentation
headers = {"Authorization": "Bearer {}".format(api_key)}  

# Call the API
response = requests.get(api_url, 
                        headers=headers, 
                        params=params)

# Extract JSON data from the response
data = response.json()

# Load data to a data frame
cafes = pd.DataFrame(data['businesses'])

# View the data's dtypes
print(cafes.dtypes)