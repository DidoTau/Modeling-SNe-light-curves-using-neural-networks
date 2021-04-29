class Preprocessing:
    def __init__(self, sample, number_of_samples):
        self.sample = sample
        self.number_of_samples=number_of_samples
    
    def separate_sample(self,ind_vars=6):
        X = self.sample.iloc[:,0:ind_vars]
        y = self.sample.iloc[:,-1]

        return X, y