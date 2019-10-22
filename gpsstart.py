#Import of the GPS Lib
import gps
shipjourney_gps = gps.gps("I do not have a Server, it could be 127.0.0.1", "Using the Standartport 2974")
shipjourney_gps.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

while True:
	try:
		tellmewhere = shipjourney_gps.next()
		print tellmewhere
	except KeyError:
		quit()
	except StopIteration:
		shipjourney_gps = None
		print("GPS are not here anymore, please try again")
	