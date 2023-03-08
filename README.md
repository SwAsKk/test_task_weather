# test_task_weather
This code retrieves the current weather information for the specified location (in this case, Moscow) using the M3O weather API. It uses the requests library to make an HTTP GET request to the API endpoint and passes along an API key in the headers.

The response from the API is expected to be in JSON format, which is parsed into a custom object called WeatherDTO that stores the temperature, feels-like temperature, and condition of the weather.

The get_current_weather() function is the main entry point of the code and returns a WeatherDTO object with the current weather information. If the API call fails or returns a non-200 status code, the function returns None.

This code can be used as a starting point to build weather-related applications or to retrieve weather information for various use cases.
