import numpy as np
import matplotlib.pyplot as plt


class Point:
    def __init__(self, mass, x=0, y=0, vx=0, vy=0):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def apply_forces(self, fx, fy, dt, q):
        ax = (fx - (q * self.vx)) / self.mass
        ay = (fy - (q * self.vy)) / self.mass
        self.vx += ax * dt
        self.vy += ay * dt
        self.x += self.vx * dt
        self.y += self.vy * dt

    def update_position(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

    def update_euler_improved(self, x, y, vx, vy, ax, ay, dt):
        # calculate intermediate position and velocity values using Euler's method
        x_intermediate = x + vx * dt / 2
        y_intermediate = y + vy * dt / 2
        vx_intermediate = vx + ax * dt / 2
        vy_intermediate = vy + ay * dt / 2

        # calculate the updated position and velocity values using the intermediate values
        x = x + vx_intermediate * dt
        y = y + vy_intermediate * dt
        vx= vx + ax * dt
        vy = vy + ay * dt
    def simulate_motion(self, fx, fy, dt, q):
        t = 0
        positions = [(self.x, self.y)]
        times = [0]
        vxs = [self.vx]
        vys = [self.vy]

        while self.y >= 0:
            # apply the given forces to the object
            self.apply_forces(fx, fy, dt, q)

            # update the object's position and velocity using Euler's improved method
            self.update_position(dt)

            # increment the time and append the object's position and time to the lists
            t += dt
            positions.append((self.x, self.y))
            times.append(t)
            vxs.append(self.vx)
            vys.append(self.vy)

        # plot the object's trajectory using linear interpolation
        x_coords, y_coords = zip(*positions)
        t_interp = np.linspace(0, t, len(x_coords))
        print(f'{len(times)}    {len(x_coords)}')
        interp_x_coords = np.interp(t_interp, times, x_coords)
        interp_y_coords = np.interp(t_interp, times, y_coords)
        fp = interp_y_coords  # only include y-coordinates in fp
        xp = t_interp
        plt.plot(interp_x_coords, interp_y_coords, color='red')
        plt.xlabel('X Position')
        plt.ylabel('Y Position')
        plt.title('Projectile Trajectory')
        plt.show()
        # return the time taken for the object to hit the ground
        return t

