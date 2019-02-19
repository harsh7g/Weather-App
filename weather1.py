import requests, json 
api_key = "6cab54ad7cf0ed22cc9bd8c2923ddb40"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name : ") 
complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
response = requests.get(complete_url) 
x = response.json() 
if x["cod"] != "404": 
	y = x["main"] 
	current_temperature = y["temp"] 
	current_temperature=current_temperature-273.0
	current_pressure = y["pressure"] 
	current_humidiy = y["humidity"] 
	z = x["weather"] 
	weather_description = z[0]["description"] 
	curr_time = x["sys"]
	print(" Temperature (in Celcius unit) = " +
					str(current_temperature) +
		"\n atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
		"\n humidity = " +
					str(current_humidiy) + " %"
		"\n description = " +
					str(weather_description))
else: 
	print(" City Not Found ") 
