import requests

# Enter the city you want to check the weather for
city = "India"

# base URL for GoWeather API
url = f"https://goweather.herokuapp.com/weather/{city}"

# send GET request to GoWeather API
response = requests.get(url)

# check if the request was successful
if response.status_code == 200:
    # get the JSON data from the response
    data = response.json()

    # extract the relevant information from the data
    temperature = data["temperature"]
    wind = data["wind"]
    description = data["description"]

    # print the weather information
    print(f"The temperature in {city} is {temperature}.")
    print(f"The wind is {wind}.")
    print(f"The weather is {description}.")
else:
    # print the error message
    print(f"Error: {response.status_code}")
