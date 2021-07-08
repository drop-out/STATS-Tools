import numpy as np
import pandas as pd
from STATSTools.bootstrap import bootstrap_index

# 生成一个nobs=1000的正态分布样本
np.random.seed(0)
data = pd.DataFrame({'draw':np.random.normal(1,size=1000)})

# 传统标准误计算方法，注意计算标准差时自由度-1，除以√n时不用减自由度 
print(np.std(data.draw,ddof=1)/np.sqrt(len(data.draw)))
# 0.031228347154118385

# bootstrap
bootstrap_generator = bootstrap_index(1000,random_seed=0)
mean = []
for i in range(10000):
    bs_sample = data.iloc[next(bootstrap_generator),:]
    mean.append(np.mean(bs_sample.draw))
    
# bootstrap标准误计算方法，注意自由度-1
print(np.std(mean,ddof=1))
# 0.03100896563227704
