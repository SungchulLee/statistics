import matplotlib.pyplot as plt
import numpy as np

from global_name_space import ARGS

def main():
    X_bar = []
    for _ in range(10_000):
        x = np.random.uniform(size=(5,))
        x_bar = x.mean()
        X_bar.append(x_bar)

    average = np.array(X_bar).mean()
    standard_error = np.array(X_bar).std()

    print(f'(Estimated) Mean of X_bar : {average:.4}')
    print(f'Standard Error   of X_bar : {standard_error:.4}')

    fig, ax =plt.subplots(figsize=(12,3))

    ax.set_title("Sampling Distribution of X_bar", fontsize=20)

    ax.hist(X_bar, bins=100, density=True, alpha=0.3)
    ax.vlines(average, ymin=0, ymax=5, alpha=1.0, color='k', ls='-', lw=5)
    ax.vlines(average+standard_error, ymin=0, ymax=5, alpha=0.7, color='k', ls='--')
    ax.vlines(average-standard_error, ymin=0, ymax=5, alpha=0.7, color='k', ls='--')

    arrowprops=dict(arrowstyle='<->', color='k', linewidth=3, mutation_scale=20)
    ax.annotate(text='',
                xy=(average,5),
                xytext=(average+standard_error,5),
                arrowprops=arrowprops)
    ax.annotate(text='Standard Error',
                xy=(average,5.5),
                xytext=(average,5.5),
                fontsize=15)

    ax.set_xlim(0.0,1.0)
    ax.set_ylim(-0.1,6)

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    plt.show()

if __name__ == "__main__":
    main()