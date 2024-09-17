import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

from global_name_space import ARGS

def main():
    obj = stats.norm(loc=ARGS.mu, scale=ARGS.sigma)
    
    x = np.linspace(ARGS.mu-3*ARGS.sigma, ARGS.mu+3*ARGS.sigma, 100)
    cdf = obj.cdf(x)
    sf = obj.sf(x)

    _, ax = plt.subplots(figsize=(12,3))
    ax.plot(x, sf, color='b', label='sf')
    ax.plot(x, cdf, color='r', label='cdf')
    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()