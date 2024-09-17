import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

from global_name_space import ARGS
from load_data import load_data

def main():
    data_dict = load_data()

    _, axes = plt.subplots(1,len(data_dict),figsize=(12,3))

    for ax, (population_name, population) in zip(axes,data_dict.items()):

        x_bar_simulations = np.array(
            [np.random.choice(population, 
                              size=ARGS.n_sample, 
                              replace=False).mean() for _ in range(ARGS.n_sim)]
                              )

    
        _, bins, _ = ax.hist(x_bar_simulations,density=True,bins=10,label="x_bar_simulation")
        ax.set_title(f"p_hat_simulation from\npopulation\nB(1,{population_name})")
        p = float(population_name)
        sigma = np.sqrt(p*(1-p)/ARGS.n_sample)
        pdf = stats.norm(loc=p,scale=sigma).pdf(bins)
        ax.plot(bins,pdf,'--r',alpha=0.5,lw=2,label="theoretical pdf")
        #ax.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()