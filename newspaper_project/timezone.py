from django.utils import timezone
import zoneinfo
#print(zoneinfo.available_timezones())
for timezone in zoneinfo.available_timezones():
    #print(timezone)
    time_zone = timezone.split('/')
    if time_zone[-1] == "Tashkent":
        print(timezone) 