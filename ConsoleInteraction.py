import PiDay17 as PiDay
import math


"""calls all the other pies for a meeting"""
resolution = 2
user_input = ''
while user_input != 'quit':
    user_input = input('Press enter to continue, type anything else to kill.')
    if user_input == '':
        probability = PiDay.get_probability(resolution)
        pie = PiDay.get_pie(probability)
        if pie == -1:
            print('Was gonna divide by zero, lets try that again.')
        else:
            print('Resolution: {}'.format(resolution))
            print('Probability: {}'.format(probability))
            print('Generated Pi: {}'.format(pie))
            print('Wrongness: {:.2f}%'.format(abs(pie/math.pi*100-100)))
            resolution = resolution * 2
    else:
        break
