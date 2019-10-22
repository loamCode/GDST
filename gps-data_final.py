import gps 
import time 
session = gps.gps("127.0.0.1", "2947") 
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
 
while True:
    try:
	time.sleep(10.0)
        ship_journey = session.next()
	if ship_journey['class'] == 'TPV':
		if ship_journey_atrr(ship_journey, 'lat'):
        		print ("Latitude is = ") +str(ship_journey.lat)
	if ship_journey['class'] == 'TPV':
		if ship_journey_atrr(ship_journey,'lon'):
			print ("Longitude is = ") +str(ship_journey.lon)
	if ship_journey['class'] =='TPV':
		if ship_journey_atrr(ship_journey,'speed'):
			print ("ship is moving at = ") +str(ship_journey.speed)+" KPH"
	if ship_journey['class'] =='TPV':
		if ship_journey_atrr(ship_journey,'alt'):
			print ("The altitude is = ") +str(ship_journey.alt)+" m"
	if ship_journey['class'] == 'TPV':
		if ship_journey_atrr(ship_journey,'time'):
			print ("The current date and time is = ") +str(ship_journey.time)+"\n"
		
    except KeyError:
		quit()
	except StopIteration:
		shipjourney_gps = None
		print("GPS are not here anymore, please try again")


# Not my, but usefull for understanding, why we need math
#------------------------------------------------------------------------------+
#
#   Nathan A. Rooy
#   2016-SEP-30
#   Solve the inverse Vincenty's formulae
#   https://en.wikipedia.org/wiki/Vincenty%27s_formulae
#
#------------------------------------------------------------------------------+

#--- IMPORT DEPENDENCIES ------------------------------------------------------+

# from __future__ import division
# from math import atan
# from math import atan2
# from math import cos
# from math import radians
# from math import sin
# from math import sqrt
# from math import tan

#--- MAIN ---------------------------------------------------------------------+

# class vincenty_inverse:
    # def __init__(self,coord1,coord2,maxIter=200,tol=10**-12):

        # #--- CONSTANTS ------------------------------------+
        
        # a=6378137.0                             # radius at equator in meters (WGS-84)
        # f=1/298.257223563                       # flattening of the ellipsoid (WGS-84)
        # b=(1-f)*a

        # phi_1,L_1,=coord1                       # (lat=L_?,lon=phi_?)
        # phi_2,L_2,=coord2                  

        # u_1=atan((1-f)*tan(radians(phi_1)))
        # u_2=atan((1-f)*tan(radians(phi_2)))

        # L=radians(L_2-L_1)

        # Lambda=L                                # set initial value of lambda to L

        # sin_u1=sin(u_1)
        # cos_u1=cos(u_1)
        # sin_u2=sin(u_2)
        # cos_u2=cos(u_2)

        # #--- BEGIN ITERATIONS -----------------------------+
        # self.iters=0
        # for i in range(0,maxIter):
            # self.iters+=1
            
            # cos_lambda=cos(Lambda)
            # sin_lambda=sin(Lambda)
            # sin_sigma=sqrt((cos_u2*sin(Lambda))**2+(cos_u1*sin_u2-sin_u1*cos_u2*cos_lambda)**2)
            # cos_sigma=sin_u1*sin_u2+cos_u1*cos_u2*cos_lambda
            # sigma=atan2(sin_sigma,cos_sigma)
            # sin_alpha=(cos_u1*cos_u2*sin_lambda)/sin_sigma
            # cos_sq_alpha=1-sin_alpha**2
            # cos2_sigma_m=cos_sigma-((2*sin_u1*sin_u2)/cos_sq_alpha)
            # C=(f/16)*cos_sq_alpha*(4+f*(4-3*cos_sq_alpha))
            # Lambda_prev=Lambda
            # Lambda=L+(1-C)*f*sin_alpha*(sigma+C*sin_sigma*(cos2_sigma_m+C*cos_sigma*(-1+2*cos2_sigma_m**2)))

            # # successful convergence
            # diff=abs(Lambda_prev-Lambda)
            # if diff<=tol:
                # break
            
        # u_sq=cos_sq_alpha*((a**2-b**2)/b**2)
        # A=1+(u_sq/16384)*(4096+u_sq*(-768+u_sq*(320-175*u_sq)))
        # B=(u_sq/1024)*(256+u_sq*(-128+u_sq*(74-47*u_sq)))
        # delta_sig=B*sin_sigma*(cos2_sigma_m+0.25*B*(cos_sigma*(-1+2*cos2_sigma_m**2)-(1/6)*B*cos2_sigma_m*(-3+4*sin_sigma**2)*(-3+4*cos2_sigma_m**2)))

        # self.m=b*A*(sigma-delta_sig)                 # output distance in meters     
        # #self.km=self.meters/1000                    # output distance in kilometers
        # #self.mm=self.meters*1000                    # output distance in millimeters
        # #self.miles=self.meters*0.000621371          # output distance in miles
        # #self.n_miles=self.miles*(6080.20/5280)      # output distance in nautical miles
        # #self.ft=self.miles*5280                     # output distance in feet
        # #self.inches=self.feet*12                    # output distance in inches
        # #self.yards=self.feet/3                      # output distance in yards

# if __name__ == "__vincenty_inverse__":
    # main()

#--- EXAMPLE ------------------------------------------------------------------+
        
# print vincenty_inverse([39.152501,-84.412977],[39.152505,-84.412946]).m
          
#--- END ----------------------------------------------------------------------+