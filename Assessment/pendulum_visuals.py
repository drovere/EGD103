# module to assist with visualising pendulum
import matplotlib.pyplot as plt

def plot_pendulum_angles(times, angles):
    fig, ax = plt.subplots()
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Angle (rad)')
    ax.plot(times, angles)


def plot_turning_points(times, angles, turning_times, turning_angles):
    fig, ax = plt.subplots()
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Angle (rad)')
    ax.plot(times, angles, label='Pendulum motion')
    ax.scatter(turning_times, turning_angles, color='r', label='Turning points')
    ax.legend()


def animate_pendulum(length, times, positions):
    import matplotlib.animation as animation
    import IPython.display

    fig = plt.figure(figsize=(5, 4))
    ax = fig.add_subplot(autoscale_on=False, xlim=(-length, length), ylim=(-length, length))
    ax.set_aspect('equal')
    ax.grid()

    line, = ax.plot([], [], 'o-', lw=2)
    time_template = 'time = %.1fs'
    time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
    time_step = times[1] - times[0]

    def animate(i):
        thisx = [0, positions[i][0]]
        thisy = [0, positions[i][1]]
        line.set_data(thisx, thisy)
        time_text.set_text(time_template % (i*time_step))
        return line, time_text


    ani = animation.FuncAnimation(fig, animate, len(positions), interval=(time_step)*1000, blit=True)
    plt.close(fig)
    video = ani.to_jshtml()
    html = IPython.display.HTML(video)
    IPython.display.display(html)

