import numpy as np
import scipy.stats as stats

from global_name_space import ARGS

def sign_test(paired_data):
    p_0 = 0.5
    q_0 = 0.5

    # tie is not counted
    n_plus = np.sum(paired_data[:,0] > paired_data[:,1])
    n_minus = np.sum(paired_data[:,0] < paired_data[:,1])
    n = n_plus + n_minus
    p = n_plus / (n_plus + n_minus)

    z = (p - p_0) / np.sqrt(p_0*q_0/n)

    if ARGS.test_type == "less": # alternative p < p_0
        p_value = stats.norm.cdf(z)
    elif ARGS.test_type == "two-sided": # alternative p != p_0
        p_value = 2 * stats.norm.cdf(-abs(z))
    elif ARGS.test_type == "greater": # alternative p > p_0
        p_value = stats.norm.sf(z)

    return z, p_value