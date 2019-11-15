from __future__ import print_function, division
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

import scipy.stats as stats
import hypothesis_tests as hyp
from scipy import stats
import math


def welch_t(a, b):
   
    
    """ Calculate Welch's t-statistic for two samples. """

    numerator = a.mean() - b.mean()
    
    # “ddof = Delta Degrees of Freedom”: the divisor used in the calculation is N - ddof, 
    #  where N represents the number of elements. By default ddof is zero.
    
    denominator = np.sqrt(a.var(ddof=1)/a.size + b.var(ddof=1)/b.size)
    
    return np.abs(numerator/denominator)


def welch_df(a,b):
    
                          
    "Calculate the effective degrees of freedom from two samples"
                          
    s1 = a.var(ddof=1)
    s2 = b.var(ddof=1)
    n1 = a.size
    n2 = b.size
                          
    numerator = (s1/n1 + s2/n2)**2
    denominator = (s1/n1)**2/(n1-1) + (s2/n2)**2/(n2-1)
                          
    return numerator / denominator



def p_val(a, b, two_sided=True):
                          
     t = welch_t(a,b)
     df = welch_df(a,b)
                          
     p = 1-stats.t.cdf(np.abs(t), df)
                          
     if two_sided:
         return 2*p
     else:
         return p
        
        
def compare_pval_alpha(p_val, alpha):
    alpha = 0.05
    status = ''
    if p_val > alpha:
        status = "Fail to reject"
    else:
        status = 'Reject'
    return status


        
def Cohen_d(a, b):

    # Compute Cohen's d.

    # group1: Series or NumPy array
    # group2: Series or NumPy array

    # returns a floating point number 

    diff = a.mean() - b.mean()

    n_a, n_b = len(a), len(b)
    var_a = a.var()
    var_b = b.var()

    # Calculate the pooled threshold as shown earlier
    pooled_var = (n_a * var_a + n_b * var_b) / (n_a + n_b)
    
    # Calculate Cohen's d statistic
    d = diff / np.sqrt(pooled_var)
    
    return d


# def Cohen_d(group1, group2):
    
#     group1 = a,c
#     group2 = b,e

#     # Compute Cohen's d.

#     # group1: Series or NumPy array
#     # group2: Series or NumPy array

#     # returns a floating point number 

#     diff = group1.mean() - group2.mean()

#     n1, n2 = len(group1), len(group2)
#     var1 = group1.var()
#     var2 = group2.var()

#     # Calculate the pooled threshold as shown earlier
#     pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    
#     # Calculate Cohen's d statistic
#     d = diff / np.sqrt(pooled_var)
    
#     return d


def plot_pdfs(cohen_d=2):
    """Plot PDFs for distributions that differ by some number of stds.
    
    cohen_d: number of standard deviations between the means
    """
    group1 = scipy.stats.norm(0, 1)
    group2 = scipy.stats.norm(cohen_d, 1)
    xs, ys = evaluate_PDF(group1)
    plt.fill_between(xs, ys, label='Group1', color='#ff2289', alpha=0.7)

    xs, ys = evaluate_PDF(group2)
    plt.fill_between(xs, ys, label='Group2', color='#376cb0', alpha=0.7)
    
    o, s = overlap_superiority(group1, group2)
    print('overlap', o)
    print('superiority', s)


# # generate points on the x axis between -5 and 5:
# xs = np.linspace(-5, 5, 200)

# # use stats.t.pdf to get values on the probability density function for the t-distribution
# # the second argument is the degrees of freedom
# ys = stats.t.pdf(xs, df, 0, 1)

# # initialize a matplotlib "figure"
# fig = plt.figure(figsize=(8,5))

# # get the current "axis" out of the figure
# ax = fig.gca()

# # plot the lines using matplotlib's plot function:
# ax.plot(xs, ys, linewidth=3, color='darkblue')

# # plot a vertical line for our measured difference in rates t-statistic
# ax.axvline(t, color='red', linestyle='--', lw=5,label='t-statistic')
# ax.legend()
# plt.show()

        
def visualize_t(t_stat, n_a, n_b):
   
    initialize a matplotlib "figure"
    fig = plt.figure(figsize=(8,5))
    ax = fig.gca()
    # generate points on the x axis between -4 and 4:
    xs = np.linspace(-10, 10, 500)
    
    # use stats.t.ppf to get critical value. For alpha = 0.05 and two tailed test
    crit = stats.t.ppf(1-0.025, (n_a+n_b-2))
    
    # use stats.t.pdf to get values on the probability density function for the t-distribution
    
    ys= stats.t.pdf(xs, (n_a+n_b-2), 0, 1)
    ax.plot(xs, ys, linewidth=3, color='darkred')

    ax.axvline(crit, color='black', linestyle='--', lw=5)
    ax.axvline(-crit, color='black', linestyle='--', lw=5)
    ax.axvline(t_stat, color='black', linestyle='--', lw=5)
    
    plt.show()
    return None

t_crit = np.round(stats.t.ppf(1 - 0.05, df=df),3)

          
# Visualize p_value


# def visualize_t(t_stat, n_control, n_experimental):
    
#     """
#     Visualize the critical t values on a t distribution
    
#     Parameters
#     -----------
#     t-stat: float
#     n_control: int
#     n_experiment: int
    
#     Returns
#     ----------
#     None
    
#     """
#     # initialize a matplotlib "figure"
#     fig = plt.figure(figsize=(8,5))
#     ax = fig.gca()
#     # generate points on the x axis between -4 and 4:
#     xs = np.linspace(-4, 4, 500)

#     # use stats.t.ppf to get critical value. For alpha = 0.05 and two tailed test
#     crit = stats.t.ppf(1-0.025, (n_control+n_experimental-2))
    
#     # use stats.t.pdf to get values on the probability density function for the t distribution
    
#     ys= stats.t.pdf(xs, (n_control+n_experimental-2), 0, 1)
#     ax.plot(xs, ys, linewidth=3, color='darkred')

#     ax.axvline(crit, color='black', linestyle='--', lw=5)
#     ax.axvline(-crit, color='black', linestyle='--', lw=5)
    
#     plt.show()
#     return None

# n_control = len(control)
# n_experimental = len(experimental)
# visualize_t(t_stat, n_control, n_experimental)


                          
                