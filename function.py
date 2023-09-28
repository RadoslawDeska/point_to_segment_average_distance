import numpy as np
from scipy import integrate

#####################
## Define geometry ##
#####################
segment_length = 0.1

# point coordinates
point_xy = (0, 0.2)

############################
## integration definition ##
############################

def integrand(x,a,b):
    return np.sqrt(b**2+(x-a)**2) / segment_length

# integration boundaries
lower_bound=0
upper_bound=segment_length

################################
## integrate and show results ##
################################

integral = integrate.quad(integrand, lower_bound, upper_bound, args=(point_xy[0],point_xy[1]), full_output=0)

average_distance = integral[0]

print(average_distance)
