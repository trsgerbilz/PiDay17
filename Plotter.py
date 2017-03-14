import PiDay17 as PiDay
import matplotlib.pyplot as plot
import math


step = 12


def gen_plot(step):
    pi = []
    probability =[]
    pie = []
    error = []
    resolution = 2
    for i in range(step):
        probability.append(PiDay.get_probability(resolution))
        pie.append(PiDay.get_pie(probability[i]))
        error.append(abs(pie[i]/math.pi*100-100))
        pi.append(math.pi)
        resolution *= 2

    line1, = plot.plot(pi, label='Pi')
    line2, = plot.plot(pie, label='Pie')
    line3, = plot.plot(error, label='Wrongness')

    plot.legend(handles=[line1, line2, line3])
    plot.show()

gen_plot(step)



