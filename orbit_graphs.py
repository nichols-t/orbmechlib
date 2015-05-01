import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle
import math

#the graviational constant. Note this is in km3 to facilitate the calculation of the standard gravitational parameter
G = 0.0000000000667384

def graph_orbit(body_radius = 10, semi_majaxis = 35, eccentricity = 0.1, arg_periapsis = 0, xbounds = (-100, 100) , ybounds = (-100, 100)):
    """
    Graphs an elliptical orbit and a spherical planetary body from semi-major axis, eccentricity, and the argument of periapsis
    """
    #calculate the argument of periapsis in radians
    arg_peri_rad = math.radians(arg_periapsis)
    
    #compute the major axis from the distance between the apoapsis and the periapsis
    orbit_majaxis = semi_majaxis * 2
    
    #compute the distance between the foci
    foci_distance = orbit_majaxis * eccentricity
    
    #compute the locations of the orbit foci
    orbit_focus1 = (0, 0)
    orbit_focus2 = (foci_distance * math.cos(arg_peri_rad), foci_distance * math.sin(arg_peri_rad))
        
    #compute the minor axis of the orbit
    orbit_minaxis = math.sqrt(orbit_majaxis**2 - foci_distance**2)
    
    #compute the center of the orbit
    orbit_center = (orbit_focus2[0]/2, orbit_focus2[1]/2)
    
    #print the center for debugging
    
    #graph the ellipse
    orbit = Ellipse(orbit_center, orbit_majaxis, orbit_minaxis, angle = arg_periapsis, fill = False)
    
    #instantiate the graph, set the aspect ratio to equal, add the celestial body and the orbit, and set the bounds of the graph
    fig = plt.figure()
    ax = fig.gca()
    ax.axis('equal')
    ax.add_patch(Circle((0, 0), body_radius, color = 'g'))
    ax.add_patch(orbit)
    ax.set_xlim(xbounds[0], xbounds[1])
    ax.set_ylim(ybounds[0], ybounds[1])

def compute_orbital_properties(body_mass, semi_majaxis, orbital_eccentricity):
    """
    Computes many properties of an orbit based on the six orbital elements and properties of the planetary body
    """
    
    #define the orbital elements as global variables
    global M, mu, a, e
    M = body_mass
    a = semi_majaxis
    e = orbital_eccentricity
    
    #compute mu for the body's mass
    compute_std_grav_param(M)
    
    #compute the orbital period
    compute_orbital_period(a)
    
    #compute the radii of the apoapsis and periapsis
    compute_apsides()
    
def compute_std_grav_param(body_mass):
    """
    Compute the standard gravitational parameter by using G as defined above and the mass of the body in kg
    """
    
    #set the body's mass to a global variable
    global M
    M = body_mass
    
    #define the standard gravitational parameter as a global variable for use in the other functions
    global mu
    mu = G * body_mass
    
    #print mu
    print 'The standard gravitational parameter is: ', mu
    
    
def compute_orbital_period(semi_majaxis):
    """
    Computes the period of a circular or elliptical orbit given the semi-major axis in meters and the mass of the planetary body
    """
    
    #compute the orbital formula
    global orbital_period
    orbital_period = 2 * math.pi * math.sqrt(semi_majaxis**3 / mu)
    
    print orbital_period, ' seconds'
    
def compute_apsides():
    """
    calculates the radii of the apsides based upon the other orbital quantities
    """
    global Ra, Rp
    Ra = a * (1 + e)
    Rp = a * (1 - e)
    
    print 'The radius of the apoapsis is: ', Ra
    print 'The radius of the periapsis is: ', Rp