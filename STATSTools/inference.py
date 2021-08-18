import numpy as np



def sample_mean_std(array):
    '''
    计算样本期望的标准差
    array: 样本值(numpy array格式)
    '''
    return np.std(array,ddof=1)/np.sqrt(len(array))

def binominal_p_std(p,n):
    '''
    计算二项分布p估计量的标准差
    p: 二项分布样本中正样本的比例
    n: 样本个数
    '''
    return np.sqrt(p*(1-p))/np.sqrt(n-1)
