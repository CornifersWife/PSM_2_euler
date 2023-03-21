from Point import Point
from Force import Force

# create a Point object with mass 1 and initial position (0, 0) and velocity (10, 10)
point = Point(1, vx=10, vy=10)
dt = 0.01
q = 0.10
forces = []
f1 = Force(9.8, 270)
#f2 = Force(1, 45)

final_force = Force.total_force(f1)
fx, fy = final_force.xy_forces()
print(f'fx: {fx}     fy: {fy}')
# simulate the movement for the given forces and time step and plot the trajectory
t = point.simulate_motion(fx, fy, dt, q)

# print the time taken for the object to hit the ground
print(f"The object hit the ground after {t:.2f} seconds.")
