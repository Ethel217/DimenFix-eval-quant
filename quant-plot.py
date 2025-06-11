import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

metrics = ['Continuity', 'Trustworthiness', 'InterConintuity', 'Steadiness', 'Cohesiveness']
m = len(metrics)
datasets = {
    'ESR': [
        0.0334,	0.6645,	0.0251	,0.5912	,0.7420,
0.0323	,0.6633,	0.0251,	0.5989,	0.6964,
0.0307,	0.6603,	0.0224,	0.5901	,0.7287,
0.0341,	0.6679,	0.0252,	0.5883,	0.7227,
0.0344	,0.6660,	0.0252,	0.5944,	0.7096,
0.0331,	0.6617	,0.0233,	0.5809,	0.7024,
0.0329,	0.6662,	0.0248	,0.6042,	0.6921,
0.0308,	0.6596,	0.0222,	0.5836,	0.7354,
0.0329	,0.6640,	0.0246,	0.5821,	0.7009,
0.0342,	0.6659,	0.0242,	0.5929,	0.7132,
0.0335,	0.6651,	0.0246,	0.5889,	0.7135,
0.0324,	0.6642,	0.0239,	0.5930,	0.7008,
0.0308,	0.6592,	0.0217,	0.5895,	0.7193,
0.0342,	0.6678,	0.0251,	0.6070,	0.7108,
0.0346,	0.6667,	0.0245	,0.6016,	0.7149,
        0.1995,	0.8085,	0.1230,	0.6779,	0.6501,#
        0.1981,	0.8076,	0.1204,	0.6812,	0.6114,
        0.1983,	0.8072,	0.1199,	0.6687,	0.6572,
    ],
    'Imageseg': [
        0.5532,	0.9819,	0.2952,	0.6343,	0.7415,
        0.5192,	0.9701,	0.2417,	0.5934,	0.7327,
        0.5547,	0.9864,	0.2949,	0.7029,	0.8485,
        0.5148,	0.9658,	0.2302,	0.5452,	0.7298,
        0.5416,	0.9793,	0.2746,	0.6151,	0.7767,
        0.5186,	0.9635,	0.2711,	0.5361,	0.7541,
        0.7564,	0.9958,	0.3449,	0.9085,	0.7581,
        0.7570,	0.9961,	0.3394,	0.9125,	0.7790,
        	0.7569,	0.9966,	0.3558,	0.9125,	0.7440,
    ],
    'TODOSpam': [
        0.7053, 0.9897, 0.4920, 0.9364, 0.7174,
        0.7127, 0.9911, 0.5013, 0.9387, 0.7032,
        0.7120, 0.9913, 0.4873, 0.9279, 0.6721,
        0.7707, 0.9989, 0.3887, 0.9312, 0.7821,
        0.7313, 0.9908, 0.3667, 0.9389, 0.7876,
        0.7627, 0.9957, 0.3687, 0.9374, 0.7589,
    ]
}

all_data = []

for dataset_name, values in datasets.items():
    total_values = len(values)
    values_per_run = m
    total_runs = total_values // values_per_run
    num_b_runs = 3
    num_a_runs = total_runs - num_b_runs
    
    idx = 0
    for run in range(total_runs):
        setting = 'DimenFix' if run < num_a_runs else 'Regular'
        for i in range(m):
            all_data.append({
                'Dataset': dataset_name,
                'Setting': setting,
                'Metric': metrics[i],
                'Value': values[idx]
            })
            idx += 1

# Convert to DataFrame
df = pd.DataFrame(all_data)

# Plot per metric
for metric in metrics:
    plt.figure(figsize=(4, 8))
    subset = df[df['Metric'] == metric]
    sns.boxplot(x='Dataset', y='Value', hue='Setting', data=subset, palette='Set2')
    plt.title(f'{metric} Comparison')
    plt.xlabel('')
    plt.ylabel('')
    plt.legend(title='')
    plt.tight_layout()
    plt.savefig(f"{metric}_quant.png", dpi=300)
    plt.show()
