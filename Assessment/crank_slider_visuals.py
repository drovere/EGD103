# module to assist with visualising pendulum
import matplotlib.pyplot as plt

def plot_turning_points(times, positions, turning_times, turning_positions):
    x_coords = [x[0] for x in positions]
    x_turning = [x[0] for x in turning_positions]
    fig, ax = plt.subplots()
    ax.set_xlabel('time')
    ax.set_ylabel('x position')
    ax.plot(times, x_coords, label='Slider motion')
    ax.scatter(turning_times, x_turning, color='r', label='Turning points')
    ax.legend()


def animate_crank_slider(times, pin_positions, slider_positions):
    import matplotlib.animation as animation
    import IPython.display

    fig = plt.figure(figsize=(5, 4))
    ax = fig.add_subplot(autoscale_on=False, xlim=(-10, 10), ylim=(-10, 10))
    ax.set_aspect('equal')
    ax.grid()

    line, = ax.plot([], [], 'o-', lw=2)
    time_template = 'time = %.1fs'
    time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
    time_step = times[1] - times[0]

    def animate(i):
        thisx = [0, pin_positions[i][0], slider_positions[i][0]]
        thisy = [0, pin_positions[i][1], slider_positions[i][1]]
        line.set_data(thisx, thisy)
        return line


    ani = animation.FuncAnimation(fig, animate, len(pin_positions), interval=(time_step)*100, blit=False)
    #ani.save('Pendulum simulation 1.gif', fps=1/time_step)
    plt.close(fig)
    video = ani.to_jshtml()
    html = IPython.display.HTML(video)
    IPython.display.display(html)