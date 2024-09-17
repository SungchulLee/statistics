import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

from global_name_space import ARGS

def main():
    obj = stats.norm(loc=ARGS.mu, scale=ARGS.sigma)
    
    x = np.linspace(ARGS.mu-3*ARGS.sigma, ARGS.mu+3*ARGS.sigma, 100)
    pdf = obj.pdf(x)
    random_samples = obj.rvs(size=(ARGS.n_samples,), random_state=ARGS.seed)

    _, ax = plt.subplots(figsize=(12,3))
    ax.plot(x, pdf, color='b', label='pdf')
    ax.hist(random_samples, bins=x, density=True, label="random_samples")
    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()