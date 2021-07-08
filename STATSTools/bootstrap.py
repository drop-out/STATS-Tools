
#coding=utf-8
import numpy as np


def bootstrap_index(n_obs,n_bootstrap_obs=None,random_seed=0):
    '''
    n_obs: 样本总数
    n_bootstrap_obs: 每个bootstrap样本中的observation个数
    random_seed: 随机数种子
    
    return: bootstrap index生成器
    '''
    if n_bootstrap_obs is None:
        n_bootstrap_obs = n_obs
    np.random.seed(random_seed)
    while True:
        yield np.random.randint(0,n_obs,size=n_bootstrap_obs)
