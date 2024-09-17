import pandas as pd
import scipy.stats as stats

from global_name_space import ARGS

def load_data():
    data_dict = {}
    
    data_dict["norm"] = stats.norm().rvs(ARGS.n_population, random_state=ARGS.seed)
    data_dict["expon"] = stats.expon().rvs(ARGS.n_population, random_state=ARGS.seed)
    data_dict["chi2"] = stats.chi2(df=2).rvs(ARGS.n_population, random_state=ARGS.seed)
    data_dict["uniform"] = stats.uniform().rvs(ARGS.n_population, random_state=ARGS.seed)

    url = 'https://raw.githubusercontent.com/gedeck/practical-statistics-for-data-scientists/master/data/loans_income.csv'
    df = pd.read_csv(url)
    data_dict["loans_income"] = df.values.reshape((-1,))
        
    return data_dict