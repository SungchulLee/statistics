import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

from global_name_space import ARGS
from load_data import load_data

def main():
    data_dict = load_data()

    _, axes = plt.subplots(1,len(data_dict),figsize=(12,3))

    for ax, (population_name, population) in zip(axes,data_dict.items()):

        s_square_simulations = np.array(
            [np.random.choice(population, 
                              size=ARGS.n_sample, 
                              replace=False).var(ddof=1) for _ in range(ARGS.n_sim)]
                              )

    
        _, bins, _ = ax.hist(s_square_simulations,density=True,bins=30,label="x_bar_simulation")
        ax.set_title(f"s_square_simulation from\npopulation\n{population_name}")
        df = ARGS.n_sample - 1
        c = df / population.var()
        pdf = stats.chi2(df).pdf(bins*c) * c
        ax.plot(bins,pdf,'--r',alpha=0.5,lw=2,label="theoretical pdf")
        #ax.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()