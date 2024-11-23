print("Hello World!")
print("This is a new file")

# adding api spacex
"https://api.spacexdata.com/v4/"
"https://api.spacexdata.com/v4/capsules"
"https://api.spacexdata.com/v4/cores"

url = "https://api.spacexdata.com/v4/launches/past"
response = requests.get(url)
response.json()

# wrangling data using an API
data = pd.json_normalize(response.json()) 
# json data to flat data form

# webscrape falcon 9 launch records

# raw data to clean data
# wrnaglidng data
  # function, targets, endpoint
  # another endpoint to get specific datas
# sampling
  # how to filter or remove falcon 1 data to get falcon 9 data
# nulling
  # data that contains null value; inside the payload mask
  # calculate mean of payload and replace null with mean

  
  




