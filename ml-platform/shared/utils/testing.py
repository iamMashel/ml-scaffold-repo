from scipy import stats

def run_ttest(group1, group2):
    t_stat, p_value = stats.ttest_ind(group1, group2, nan_policy='omit')
    return {'t-statistic': t_stat, 'p-value': p_value}
