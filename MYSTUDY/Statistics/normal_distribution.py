import random
import pylab


def make_normal_distribution(mean, sd, numtrail):
    samples = []
    for num in range(numtrail):
        samples.append(random.gauss(mean, sd))
    pylab.hist(samples, bins=101)

if __name__ == '__main__':
    make_normal_distribution(0.0, 1.0, 1000000)
    pylab.show()