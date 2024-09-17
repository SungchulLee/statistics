import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

from global_name_space import ARGS

def main():
    obj = stats.norm(loc=ARGS.mu, scale=ARGS.sigma)
    
    x = np.linspace(ARGS.mu-3*ARGS.sigma, ARGS.mu+3*ARGS.sigma, 100)
    pdf = obj.pdf(x)

    _, ax = plt.subplots(figsize=(12,3))
    ax.plot(x, pdf, color='b', label='pdf')
    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()