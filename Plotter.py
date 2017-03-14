import PiDay17 as PiDay
import matplotlib.pyplot as plot
import math


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
    line2, = plot.plot(pie, label='Pie: {:.5f}'.format(pie[-1]))
    line3, = plot.plot(error, label='Wrongness: {:.2f}%'.format(error[-1]))

    plot.legend(handles=[line1, line2, line3])
    plot.show()

step = int(input("input number of iterations: "))
gen_plot(step)



