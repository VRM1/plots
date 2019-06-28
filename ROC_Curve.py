# roc curve and auc
from sklearn.metrics import roc_curve
from matplotlib import pyplot as plt
import pandas as pd
from matplotlib.ticker import MaxNLocator

fil = '<fileName>'
loc = '<locationOfData>'
df = pd.read_csv(loc+fil+'.csv')
params = {'legend.fontsize': 30,
          'xtick.labelsize':30,
          'ytick.labelsize':30,
          'axes.labelsize':30}
Y,logist_Y = df['isChurn'],df['Logistic Regression (1.0)']
rf_Y,nn_y = df['Random Forest (1.0)'],df['Neural Network (1.0)']
# calculate roc curve
fpr_1, tpr_1, thresholds_1 = roc_curve(Y, logist_Y)
fpr_2, tpr_2, thresholds_2 = roc_curve(Y, rf_Y)
fpr_3, tpr_3, thresholds_3 = roc_curve(Y, nn_y)
# plot no skill
fig = plt.figure(figsize=(14,7))
plt.rcParams.update(params)
ax = plt.axes()
ax.plot([0, 1], [0, 1], linestyle='--',color='red')
# plot the roc curve for the model
ax.set_xlabel('FP Rate')
ax.set_ylabel('TP Rate')
ax.set_xlim([0,1])
ax.set_ylim([0,1.01])
plt_a, = ax.plot(fpr_1, tpr_1, marker='.',color='green')
plt_b, = ax.plot(fpr_3,tpr_3,marker='.',color='blue')
plt_c, = ax.plot(fpr_2,tpr_2,marker='.',color='magenta')
handles, labels = ax.get_legend_handles_labels()
plt.legend([plt_a,plt_b,plt_c],['Logistic', 'RF', 'MLP'])
plt.gca().xaxis.set_major_locator(MaxNLocator(prune='lower'))
# show the plot
plt.grid(linestyle='--')
plt.savefig('plots/'+fil+'.png',dpi=300,bbox_inches='tight')
