import argparse
import numpy as np

parser = argparse.ArgumentParser(description='PyTorch MNIST Example')
parser.add_argument('--seed', type=int, default=1, metavar='S',
                    help='random seed (default: 1)')
parser.add_argument('--test_type', type=int, default=1, metavar='S',
                    help='alternative p < 0.5 (0), p != 0.5 (1), p > 0.5 (2)')
ARGS = parser.parse_args()

np.random.seed(ARGS.seed)

ARGS.test_type == "two-sided"