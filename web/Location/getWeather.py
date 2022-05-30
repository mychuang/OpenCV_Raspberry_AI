"""
Refer: https://pypi.org/project/WeatherData/?fbclid=IwAR1K8N5EYz2dE7UOrzivivgYufGNHraI18cz2DknIcCEuEuFRpbf8yTkz4c
"""
import WeatherData as wd
from datetime import datetime

times = "2022-05-30"
newTimes = times.split('-', 2)
print(newTimes)
print(type(newTimes[0]))
print(newTimes[1])
print(newTimes[2])

result = wd.obs.get(lat=24.8493676, lon=120.999921, dtime=datetime(int(newTimes[0]), int(newTimes[1]), int(newTimes[2])))
print(result)
print(type(result))

#result = wd.fcst.get(lat=21., lon=124.)
#print(result)
#print(type(result))

