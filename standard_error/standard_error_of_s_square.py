import matplotlib.pyplot as plt
import numpy as np

from global_name_space import ARGS

def main():
    S_square = []
    for _ in range(10_000):
        x = np.random.uniform(size=(5,))
        sigma = x.std()
        S_square.append(sigma**2)

    average = np.array(S_square).mean()
    standard_error = np.array(S_square).std()

    print(f'(Estimated) Mean of S^2 : {average:.4}')
    print(f'Standard Error   of S^2 : {standard_error:.4}')

    fig, ax =plt.subplots(figsize=(12,3))

    ax.set_title("Sampling Distribution of S^2", fontsize=20)

    ax.hist(S_square, bins=100, density=True, alpha=0.3)
    ax.vlines(average, ymin=0, ymax=12, alpha=1.0, color='k', ls='-', lw=5)
    ax.vlines(average+standard_error, ymin=0, ymax=12, alpha=0.7, color='k', ls='--')
    ax.vlines(average-standard_error, ymin=0, ymax=12, alpha=0.7, color='k', ls='--')

    arrowprops=dict(arrowstyle='<->', color='k', linewidth=3, mutation_scale=20)
    ax.annotate(text='',
                xy=(average,12),
                xytext=(average+standard_error,12),
                arrowprops=arrowprops)
    ax.annotate(text='Standard Error',
                xy=(average,13),
                xytext=(average,13),
                fontsize=15)

    ax.set_xlim(0.0,0.2)
    ax.set_ylim(-0.1,15)

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    plt.show()

if __name__ == "__main__":
    main()