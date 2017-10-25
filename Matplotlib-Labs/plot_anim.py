import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig, ax = plt.subplots()

x = np.arange(0, 2 * np.pi, 0.01)
line, = ax.plot(x, np.sin(x))  # return [], as use first to write 'line,'


def animate(i):
	line.set_ydata(np.sin(x + i / 50.0))
	return line


def init():
	line.set_ydata(np.sin(x))
	return line

# 循環 100 次 還原始值
plot_animating = animation.FuncAnimation(fig=fig, func=animate, frames=100,
																				 init_func=init, interval=20, blit=False)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
# anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()
