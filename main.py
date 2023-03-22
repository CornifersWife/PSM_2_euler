#s24435 Maciej Łatosz

from Point import Point
from Force import Force

point = Point(1, vx=10, vy=10)
dt = 0.01
q = 0.05
forces = []
forces.append(Force(10, 270))
forces.append(Force(1, 45))
final_force = Force.total_force(*forces)
fx, fy = final_force.xy_forces()

print(f'fx: {fx}     fy: {fy}')
point.euler_formula(fx, fy, dt, 2, q)
#euler = blue, ulepszony euler = pink
