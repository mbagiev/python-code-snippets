# Generates random sample from multivariate normal distribution based on
# defined mean, standard deviation and correlation coefficients of 3 variables

import numpy as np

# Input - descriptive statistics
# Correlation coefficients order: cor(var1, var2), cor(var1, var3), cor(var2, var3)
stat = {'mean': [120, 75, 100],
        'std': [4.5, 7.5, 1.2],
        'cor': [0.5, -0.2, 0.7]}

# Mean
mean = stat['mean']

# Diagonal matrix of standard deviations
std = np.diag(stat['std'])

# Correlation matrix
cor = [[1.0,            stat['cor'][0], stat['cor'][1]],
       [stat['cor'][0], 1.0,            stat['cor'][2]],
       [stat['cor'][1], stat['cor'][2], 1.0]]

# Covariance matrix: cov = std * cor * std
cov = np.dot(np.dot(std, cor), std)

size = 100

# Random sample from multivariate normal distribution
sample = np.random.multivariate_normal(mean=mean, cov=cov, size=size)
print(sample)
