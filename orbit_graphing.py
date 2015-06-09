import matplotlib.pyplot as plt
import math
from matplotlib.patches import Ellipse, Circle

def graph_orbit(body_radius = 10, semi_majaxis = 35, eccentricity = 0.1, arg_periapsis = 0, xbounds = (-100, 100) , ybounds = (-100, 100)):
    """
    Graphs an elliptical orbit and a spherical planetary body from semi-major axis, eccentricity, and the argument of periapsis
    """
    #calculate the argument of periapsis in radians to be used in trigonometry
    arg_peri_rad = math.radians(arg_periapsis)
    
    #compute the major axis from the distance between the apoapsis and the periapsis so we have the width for the Ellipse object
    orbit_majaxis = semi_majaxis * 2
    
    #compute the distance between the foci so we can calculate the height of the Ellipse object
    foci_distance = orbit_majaxis * eccentricity
    
    #compute the locations of the orbit foci so we can calculate the orbit's center
    orbit_focus1 = (0, 0)
    orbit_focus2 = (foci_distance * math.cos(arg_peri_rad), foci_distance * math.sin(arg_peri_rad))
        
    #compute the minor axis of the orbit: height of Ellipse
    orbit_minaxis = math.sqrt(orbit_majaxis**2 - foci_distance**2)
    
    #compute the center of the orbit
    orbit_center = (orbit_focus2[0]/2, orbit_focus2[1]/2)
        
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