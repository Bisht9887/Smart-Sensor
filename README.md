## Smart-Sensor
In this project the demo of two sensors: Humiture Sensor and Ultra Sonic Range Sensor has been shown. The code has been written in Python.
### Requirements: 
 1)Humiture Sensor,
 2)Ultra Sonic Range Sensor
 3)Bread board
 4)Push button
 5)Display screen
 6)Internet connection
 7) pyowm- A python libray used for calculating the temperature of a location based on zip code or area name
 
Connect the Humiture Sensor and Ultra Sonic Range Sensor with the Raspberry Pi. A bread board would be required for the connection.

On pressing the push button, the python script will run:
The Humiture Sensor will measure the temperature of the place where it has been kept and send this as an input to the python script. The python script is will use this value and will compare this temperature value with the outside temperature value using the internet connection.
The Ultra Sonic Range Sensor on the other hand will also get activated when the push button would be pressed. As it's functionality it will tell the distance of an object from it.
### Results:
We have put an email id in the python code. The result of both the sensors will come as an email.

### Applications:
1) Deciding if the outer temperature is higher or lower than the inside temperature.
2) Autonomous cars.
