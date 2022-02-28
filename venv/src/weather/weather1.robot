*** settings ***
#Suite Setup
#Suite Teandown
Force Tags     odg
Resource        weatherresource.robot


*** test cases ***
Weather details.
    [TAGS]   test
    weather result  Delhi
    weather result  Noida
    weather result  Mumbai
    weather result  Moscow

UI weather information
    [TAGS]   test1
    open_browser