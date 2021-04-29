import numpy as np
import pandas as pd
import os

def toPickle(new_filename: str, path: str, path_models:str):
    """[summary]

    Args:
        new_filename (str): [description]
        path (str): [description]
        path_models (str): [description]
    """
    nz = 30
    nAvs = 10
    zs = np.logspace(-3, 0, nz)
    Avs = np.logspace(-4, 1, nAvs)
    
    files = os.listdir(path)
    models = pd.read_csv(path_models)
    # Inicializando el modelo
    columns_names = ["mdot_msunyr", "mass_msun", "energy_foe", "beta", "redshift", "attenuattion", "light curves"]

    df = pd.DataFrame(columns = columns_names)

    # Explorando los datos para agregarlos al modelo
    for f in files:
        name = f[:-4]
        if name in models.index:
            lc_matrix = np.load(path+f)
            data = models.loc[name]
            for i in range(lc_matrix.shape[0]):
                for j in range(lc_matrix.shape[1]):
                    params = {'mdot_msunyr': data['mdot_msunyr'],
                                'mass_msun': data['mass_msun'], 
                                'energy_foe': data['energy_foe'], 
                                'beta': data['beta'], 
                                'redshift': zs[i], 
                                'attenuattion': Avs[j], 
                                'light curves': lc_matrix[i,j,:]}
                    df = df.append(params, ignore_index=True)
    df.to_pickle(new_filename + ".pkl")