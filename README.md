# MPS-Solar-System
University project for "Modelling of Physical Systems" - planetary system simulation.

* Should Sun rotate around center of the mass or not
* Clearly define equations that will be used


## To do
* initial conditions file from which planets are built(separate files for planets/asteroids?)
* class describing planet
	* fields: name, mass, initial velocity (x,y,z), inclination (or speed is enough?) 	
	* method to print current planet position to a file
	* metod to generate new accelerations and velocities
	* method to generate 
* function that calculates center of mass for given list of planets / asteroids
* function / class to show final results
	* scaling of simulation speed
	* scaling simulation size

## Sources:
* https://en.wikipedia.org/wiki/Numerical_model_of_the_Solar_System#Modern_method this one can be useful
* https://en.wikipedia.org/wiki/Orbital_speed#Planets orbital velocity of each planet (initial at least)
* https://rhodesmill.org/skyfield/ some package (can be usefull for obtaining initial positions)
* https://ssd.jpl.nasa.gov/horizons.cgi#top for initial conditions
