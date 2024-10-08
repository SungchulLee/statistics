import argparse
import numpy as np

parser = argparse.ArgumentParser(description='PyTorch MNIST Example')
parser.add_argument('--seed', type=int, default=1, metavar='S',
                    help='random seed (default: 1)')
ARGS = parser.parse_args()

np.random.seed(ARGS.seed)

ARGS.n_population = 10_000
ARGS.n_sample = 100
ARGS.n_sim = 1_000