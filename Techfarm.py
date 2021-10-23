import serial
import time
import requests

sp = serial.Serial('/dev/ttyUSB0',9600)
print(sp.name)
while 1:
       rdata = sp.readline()
       print(rdata)
       fdata = rdata.decode().split(',', 8)
       for x in range(0,7):
           print(fdata[x])
           
       sensor_type = fdata[1]
       #print(sensor_type)
       sensor_no = fdata[2]
       #print(sensor_no)
       sensor_data1 = fdata[4]
       #print(sensor_data1)
       sensor_data2 = fdata[5]
       #print(sensor_data2)
       
       if (sensor_type == 1):
           print("hello1")
           data={'sensor Type': 'Soil Moisture','Sensor No': sensor_no, 'Soil Moisture Level':sensor_data1}
       
       elif (sensor_type == 2):
             print("hello2")
             data={'sensor Type': 'DHT11','Sensor No': sensor_no, 'Temperature':sensor_data1,'Humidity':sensor_data2}
       
       data={'sensor Type': 'Soil Moisture','Sensor No': sensor_no, 'Soil Moisture Level':sensor_data1}
       requests.put('http://esdserver:3000/api/c520d388d3438a8b12053f62c0deef6f/data',json=data)
       r=requests.get('http://esdserver:3000/api/c520d388d3438a8b12053f62c0deef6f/data')
       print(r.json())
    
       #requests.delete('http://esdserver:3000/api/c520d388d3438a8b12053f62c0deef6f/data')
       #r=requests.get('http://esdserver:3000/api/c520d388d3438a8b12053f62c0deef6f/data')
       #print(r.json())    
       
       