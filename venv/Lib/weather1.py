import requests, json

class weather1:

	def weather_result(self, city_name):
		api_key = "7fe67bf08c80ded756e598d6f8fedaea"
		url = "http://api.openweathermap.org/data/2.5/weather?"
		complete_url = url + "appid=" + api_key + "&q=" + city_name
		response = requests.get(complete_url)
		response = response.json()
#		print(response)
		if response["cod"] != "404":
			response_out = response["main"]
			current_temperature = response_out["temp"]
			current_pressure = response_out["pressure"]
			current_humidity = response_out["humidity"]
			response_out1 = response["weather"]
			weather_description = response_out1[0]["description"]
			print(" Temperature (in kelvin unit) = " +
					str(current_temperature) +
			"\n atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
			"\n humidity (in percentage) = " +
					str(current_humidity) +
			"\n description = " +
					str(weather_description))
		else:
			print(" City Not Found ")
		return response


#city_name = input("Enter city name : ")

