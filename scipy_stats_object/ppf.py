import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

from global_name_space import ARGS

def main():
    obj = stats.norm(loc=ARGS.mu, scale=ARGS.sigma)
    
    x = np.linspace(ARGS.mu-3*ARGS.sigma, ARGS.mu+3*ARGS.sigma, 1000)
    pdf = obj.pdf(x)
    z = obj.ppf(ARGS.prob)

    _, ax = plt.subplots(figsize=(12,3))
    ax.plot(x, pdf, color='b', label='pdf')
    ax.plot([z,z], [0,obj.pdf(z)], lw=5)
    ax.fill_between(x[x<=z], pdf[x<=z], np.zeros_like(pdf[x<=z]), 
                    interpolate=True, color='r', alpha=0.3)
    ax.legend()
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    plt.show()

if __name__ == "__main__":
    main()