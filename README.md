# Modeling-SNe-light-curves-using-neural-networks

The motivation of the present work is the parameters estimation using bayesian estimation methods. The original method calculates the likelihood of a set of physical parameters generating a light curve from a grid that contains different combinations of parameters and its asociated light curve. That grid was generated synthetically from hidrodynamical models of SNe II from the literature. The original calculation of a light curve associated to a vector of model paramters is a linear combination of the 

The principal aim is to train a neural network to capture this linear interpolation. The advantage is do the same calculus but using less memory space.
