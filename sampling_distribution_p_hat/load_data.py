import scipy.stats as stats

from global_name_space import ARGS

def load_data():
    data_dict = {}
    
    data_dict["0.4"] = stats.binom(n=1,p=0.4).rvs(ARGS.n_population, random_state=ARGS.seed)
    data_dict["0.5"] = stats.binom(n=1,p=0.5).rvs(ARGS.n_population, random_state=ARGS.seed)
    data_dict["0.6"] = stats.binom(n=1,p=0.6).rvs(ARGS.n_population, random_state=ARGS.seed)
    data_dict["0.7"] = stats.binom(n=1,p=0.7).rvs(ARGS.n_population, random_state=ARGS.seed)
        
    return data_dict