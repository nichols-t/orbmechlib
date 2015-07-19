#!/usr/bin/python
import orbit_graphing as orbg
import math

def open_config(config_file):
    """
    opens the configuration file for values of CONST_G, CONST_M, and others
    """
    #open the file with the specified name
    config = open(config_file, 'r')
    
    #split the file into an array of values so we can take each value as a separate constant
    config_values = config.read().split(',')
    
    #declare the global constants and set them equal to the values in the config file
    global CONST_G, CONST_M, CONST_BODY_RADIUS
    
    CONST_G = float(config_values[1])#The numbers are odd and offset because the config file contains descriptions
    CONST_M = float(config_values[3])    #In between the values
    CONST_BODY_RADIUS = float(config_values[5])
    
    #compute CONST_MU for the body's mass
    compute_std_grav_param()
    
    #print the values of the constants
    print CONST_G, ' is the gravitational constant in N m2 kg-2'
    print CONST_M, ' is the mass of the planet in kg'
    print CONST_MU, ' is the standard gravitational parameter'
    print CONST_BODY_RADIUS, ' is the radius of', config_file.split('.')[0]

def compute_orbital_properties(semi_majaxis, orbital_eccentricity, arg_P):
    """
    Computes many properties of an orbit based on the six orbital elements and properties of the planetary body
    """
    
    #define the orbital elements as global variables
    global CONST_MU, a, e
    a = float(semi_majaxis)
    e = orbital_eccentricity
    
    #compute the orbital period
    compute_orbital_period(a)
    
    #compute the radii of the apoapsis and periapsis and the velocities at each
    compute_apsides()
    
    #graph the orbit using the orbit_graphing function
    orbg.graph_orbit(CONST_BODY_RADIUS, a, e, arg_P, (-2 * Ra, 2 * Ra), (-2 * Ra, 2 * Ra))
    
def compute_std_grav_param():
    """
    Compute the standard gravitational parameter by using CONST_G as defined above and the mass of the body in kg
    """
    
    #define the standard gravitational parameter as a global variable for use in the other functions
    global CONST_MU
    CONST_MU = CONST_G * CONST_M
    
    #print CONST_MU
    print 'The standard gravitational parameter is: ', CONST_MU, 'm3/s2'
    
    
def compute_orbital_period(semi_majaxis):
    """
    Computes the period of a circular or elliptical orbit given the semi-major axis in meters and the mass of the planetary body
    """
    
    #compute the orbital formula
    global orbital_period
    orbital_period = math.sqrt(4 * (math.pi**2) * (a**3) / CONST_MU)
    
    #print the orbital period in seconds
    print 'The orbital period is: ', orbital_period, ' seconds'
    
def compute_apsides():
    """
    calculates the radii of the apsides and the velocity at the apsides based upon the other orbital quantities
    """
    
    #declare the radii and velocities of the apsides as global variables
    global Ra, Rp, Va, Vp
    
    #calculate the radii and velocities at the apsides
    Ra = a * (1 + e)
    Rp = a * (1 - e)
    Va = math.sqrt((2 * CONST_MU * Rp) / (Ra * (Ra + Rp)))
    Vp = math.sqrt((2 * CONST_MU * Ra) / (Rp * (Ra + Rp)))
    
    #determine if the orbit will intersect the body (which means periapsis is too low)
    if(Rp <= CONST_BODY_RADIUS):
        print 'The orbit is too low! It will collide with the surface!'
    else:
        print 'The radius of the apoapsis is: ', Ra, ' m'
        print 'The velocity at apoapsis is: ', Va, 'm/s'
        print 'The radius of the periapsis is: ', Rp, ' m'
        print 'The velocity at periapsis is: ', Vp, ' m/s'