from scipy.stats import ttest_ind, f_oneway
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def T_test(group1, group2):
    t_stat, p_value = ttest_ind(group1, group2)
    return t_stat, p_value
    
def Anova_test(*groups):
    f_stat, p_value = f_oneway(*groups)
    return f_stat, p_value

def Correlation_matrix(data):
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Compute correlation matrix
    correlation_matrix = df.corr()
    
    # Plotting heatmap
    plt.figure(figsize=(10, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix of Similarity Score, Mean Rating, and Mean Variance')
    plt.show()

def Descriptive_statistics(data):
    df = pd.DataFrame(data)
    desc_stats = df.describe()
    print(desc_stats)

# Example usage
# Example groups
# group1 = [0.56, 0.78, 0.664, 0.841]
# group2 = [0.874, 0.733, 0.823, 0.66]
# group3 = [0.54, 0.65, 0.325, 0.775]
# group4 = [0.664, 0.345, 0.884, 0.995]
# group5 = [0.763, 0.554, 0.885, 0.674]

# Perform T-test
# t_stat, p_value = T_test(group1, group2)
# print("T-test results:", t_stat, p_value)

# Perform ANOVA test
# f_stat, p_value = Anova_test(group1, group2, group3, group4, group5)
# print("ANOVA test results:", f_stat, p_value)

# Example data for correlation matrix
# data = {
#     'Group': ['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5', 'Group 6', 'Group 7', 'Group 8', 'Group 9', 'Group 10', 'Group 11',
#               'Group 12'],
#     'Mean Rating': [4.0, 3.33, 4.0, 4.0, 3.67, 4.44, 3.5, 3.5, 3.75, 3.5, 4.0, 3.5, 3.5],
#     'Mean Variance': [0.28, 1.72, 0.83, 0.22, 0.28, 0.22, 3.5, 2.83, 1.08, 1.67, 0.28, 0.83, 0.33],
#     'Similarity Score': [0.76, 0.5, 0.65, 0.94, 0.61, 0.94, 0.94, 0.72, 0.69, 0.39, 0.85, 0.67, 0.44]
# }

# Generate Correlation Matrix
# Correlation_matrix(data)

# Compute Descriptive Statistics
# Descriptive_statistics(data)
