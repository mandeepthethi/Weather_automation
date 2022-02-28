*** settings ***
Resource         ../main_resource.robot
Library           ../../Lib/weather1.py
Library           ../../Lib/weather2.py
#Library           ../../Lib/api/weather_api.py

*** Variables ***
${api_key}         7fe67bf08c80ded756e598d6f8fedaea
${URL}          https://accuweather.com/
${BROWSER}      Chrome


*** keywords ***