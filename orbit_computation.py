#!/usr/bin/python
import orbit_graphing as orbg
import math

def open_config(config_file):
    """
    opens the configuration file for values of G, M, and others
    """
    #open the file with the specified name
    config = open(config_file, 'r')
    
    #split the file into an array of values so we can take each value as a separate constant
    config_values = config.read().split(',')
    
    #declare the global constants and set them equal to the values in the config file
    global G, M, body_radius
    
    G = float(config_values[1])
    M = float(config_values[3])
    body_radius = float(config_values[5])
    
    #compute mu for the body's mass
    compute_std_grav_param()
    
    #print the values of the constants
    print G, ' is the gravitational constant in N m2 kg-2'
    print M, ' is the mass of the planet in kg'
    print mu, ' is the standard gravitational parameter'
    print body_radius, ' is the radius of', config_file.split('.')[0]

def compute_orbital_properties(semi_majaxis, orbital_eccentricity, arg_P):
    """
    Computes many properties of an orbit based on the six orbital elements and properties of the planetary body
    """
    
    #define the orbital elements as global variables
    global mu, a, e
    a = float(semi_majaxis)
    e = orbital_eccentricity
    
    #compute the orbital period
    compute_orbital_period(a)
    
    #compute the radii of the apoapsis and periapsis and the velocities at each
    compute_apsides()
    
    #graph the orbit using the orbit_graphing function
    orbg.graph_orbit(body_radius, a, e, arg_P, (-2 * Ra, 2 * Ra), (-2 * Ra, 2 * Ra))
    
def compute_std_grav_param():
    """
    Compute the standard gravitational parameter by using G as defined above and the mass of the body in kg
    """
    
    #define the standard gravitational parameter as a global variable for use in the other functions
    global mu
    mu = G * M
    
    #print mu
    print 'The standard gravitational parameter is: ', mu, 'm3/s2'
    
    
def compute_orbital_period(semi_majaxis):
    """
    Computes the period of a circular or elliptical orbit given the semi-major axis in meters and the mass of the planetary body
    """
    
    #compute the orbital formula
    global orbital_period
    orbital_period = math.sqrt(4 * (math.pi**2) * (a**3) / mu)
    
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
    Va = math.sqrt((2 * mu * Rp) / (Ra * (Ra + Rp)))
    Vp = math.sqrt((2 * mu * Ra) / (Rp * (Ra + Rp)))
    
    #determine if the orbit will intersect the body (which means periapsis is too low)
    if(Rp <= body_radius):
        print 'The orbit is too low! It will collide with the surface!'
    else:
        print 'The radius of the apoapsis is: ', Ra, ' m'
        print 'The velocity at apoapsis is: ', Va, 'm/s'
        print 'The radius of the periapsis is: ', Rp, ' m'
        print 'The velocity at periapsis is: ', Vp, ' m/s'