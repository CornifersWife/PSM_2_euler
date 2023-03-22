import numpy as np
import matplotlib.pyplot as plt


class Point:
    def __init__(self, mass, x=0, y=0, vx=0, vy=0, ax=0, ay=0, q=0):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay
        self.q = q

    """
    def calc_x(self, dt):
        return self.x + self.vy

    def calc_y(self, dt):
        return self.y + self.vy * dt

    def calc_vx(self, dt):

        return self.vx + self.ax * dt

    def calc_vy(self, dt):
        return self.vy + self.ay * dt

    def calc_ax(self, dt, q):

        return self.ax + (self.mass * self.ax - (q * self.calc_vx(dt)) / self.mass)

    def calc_ay(self, dt, q):
        return self.ay + (self.mass * self.ay - (q * self.calc_vy(dt)) / self.mass)
    """

    def calc_x(self, dt, improved):
        self.x += self.calc_vx(improved * dt, 0) * dt
        return self.x

    def calc_y(self, dt, improved):
        self.y += self.calc_vy(improved * dt, 0) * dt
        return self.y

    def calc_vx(self, dt, improved):
        return self.vx + self.calc_ax(improved * dt, self.q) * dt

    def calc_vy(self, dt, improved):
        return self.vy + self.calc_ay(improved * dt, self.q) * dt

    def calc_ax(self, dt, q):
        return (self.mass * self.ax - (q * self.vx)) / self.mass

    def calc_ay(self, dt, q):
        return (self.mass * self.ay - (q * self.vy)) / self.mass


    def euler_formula(self, fx, fy, dt, time, q):
        x, vx, ax, y, vy, ay = self.x, self.vx, self.ax, self.y, self.vy, self.ay
        # improved = red
        improved = 1 / 2

        steps = time / dt
        self.q = q
        self.ax = fx / self.mass
        self.ay = fy / self.mass
        times = [0]
        x_positions = [self.x]
        y_positions = [self.y]

        for moment in range(int(steps)):
            #print(f'x:{self.x}\tvx:{self.vx}\tax:{self.ax}\n'
            #     f'y:{self.y}\tvy:{self.vy}\tay:{self.ay}\n')
            times.append((times[-1] + dt))
            self.x = self.calc_x(dt, improved)
            self.y = self.calc_y(dt, improved)
            self.vx = self.calc_vx(dt, improved)
            self.vy = self.calc_vy(dt, improved)
            x_positions.append(self.x)
            y_positions.append(self.y)

        interp_t = np.linspace(0, times[-1], len(x_positions))
        interp_x_positions = np.interp(interp_t, times, x_positions)
        interp_y_positions = np.interp(interp_t, times, y_positions)
        plt.plot(interp_x_positions, interp_y_positions, color='#F5A9B8', alpha=0.8)

        self.x, self.vx, self.ax, self.y, self.vy, self.ay = x, vx, ax, y, vy, ay

        # not improved = blue
        improved = 0

        steps = time / dt
        self.q = q
        self.ax = fx / self.mass
        self.ay = fy / self.mass
        times = [0]
        x_positions = [self.x]
        y_positions = [self.y]

        for moment in range(int(steps)):
            #print(f'x:{self.x}\tvx:{self.vx}\tax:{self.ax}\n'
            #      f'y:{self.y}\tvy:{self.vy}\tay:{self.ay}\n')
            times.append((times[-1] + dt))
            self.x = self.calc_x(dt, improved)
            self.y = self.calc_y(dt, improved)
            self.vx = self.calc_vx(dt, improved)
            self.vy = self.calc_vy(dt, improved)

            x_positions.append(self.x)
            y_positions.append(self.y)

        interp_t = np.linspace(0, times[-1], len(x_positions))
        interp_x_positions = np.interp(interp_t, times, x_positions)
        interp_y_positions = np.interp(interp_t, times, y_positions)
        plt.plot(interp_x_positions, interp_y_positions, color='#5BCEFA', alpha=0.8)

        plt.xlabel('X Position')
        plt.ylabel('Y Position')
        plt.title('Projectile Trajectory')
        plt.show()


"""
    def update_euler_improved(self, x, y, vx, vy, ax, ay, dt):
        # calculate intermediate position and velocity values using Euler's method
        x_intermediate = x + vx * dt / 2
        y_intermediate = y + vy * dt / 2
        vx_intermediate = vx + ax * dt / 2
        vy_intermediate = vy + ay * dt / 2

        # calculate the updated position and velocity values using the intermediate values
        x = x + vx_intermediate * dt
        y = y + vy_intermediate * dt
        vx = vx + ax * dt
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
"""
