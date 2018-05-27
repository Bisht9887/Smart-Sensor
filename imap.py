import smtplib
from email.mime.text import MIMEText
import pyowm
import RPi.GPIO as GPIO
import time
import first as ts

owm = pyowm.OWM('3f2e277436e1af4fce323dffc90ac5f6')  


GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Will it be sunny tomorrow at this time in Orlando ?
forecast = owm.daily_forecast("kissimmee,usa")
tomorrow = pyowm.timeutils.tomorrow()
forecast.will_be_sunny_at(tomorrow)

# Search for current weather in Orlando
observation = owm.weather_at_place('kissimmee,usa')
w = observation.get_weather()
                    # <Weather - reference time=2013-12-18 09:20,
                              # status=Clouds>

# Weather details
wind= w.get_wind()                  # {'speed': 4.6, 'deg': 330}
humidity= w.get_humidity()              # 87
temperature= w.get_temperature('fahrenheit')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
tomorrow = pyowm.timeutils.tomorrow() 
hist_ht = (0.0, 0.0)

while True:
	recent_ht = ts.get_local()
	faku= ts.get_dist()

	if not recent_ht:
		H, T = hist_ht
	else:
		H, T = recent_ht
		hist_ht = recent_ht
        

	delta_T= T-temperature.get('temp')
#        time.sleep(1)
        
        print("press button to send email")
        
        
	if(GPIO.input(18)==False):
		print("Email Sent")
		if delta_T < 0:
                        message = "Inside Measured Temperature: {0} \n Current Outside temperature: {1} \n It's {2} cooler inside \n distance is {3} cm".format(abs(T), abs(temperature.get('temp')), abs(delta_T), abs(faku))
                else:
                        message = "Inside Measured Temperature: {0} \n Current Outside temperature: {1} \n It's {2} hotter inside \n distance is {3} cm".format(abs(T), abs(temperature.get('temp')), abs(delta_T), abs(faku))
                msg = MIMEText(message)
                msg['subject'] = 'Sensor Report'
                msg['from'] = 'ankitsinghbisht90@gmail.com'
                msg['to'] = 'ankit_bisht90@yahoo.com'
                
                s = smtplib.SMTP('smtp.gmail.com',  587)
                s.ehlo()
                s.starttls()
                s.ehlo()
                s.login("ankitsinghbisht90@gmail.com", "girish94120")
                s.sendmail(msg['From'], msg['To'], msg.as_string())
                s.quit()
