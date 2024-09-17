import argparse
import numpy as np
import torch

parser = argparse.ArgumentParser(description='random_number_generation_using_numpy')
parser.add_argument('--seed', type=int, default=1, metavar='S',
                    help='random seed (default: 1)')
ARGS = parser.parse_args()

np.random.seed(ARGS.seed)
torch.manual_seed(ARGS.seed)

ARGS.n_samples = 10_000
ARGS.mu = 0.
ARGS.sigma = 1.
ARGS.prob = 0.975