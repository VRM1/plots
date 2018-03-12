import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
import pandas as pd

# load variables and data
figure_nam = 'my_fig.png'
n_col = 1 #No. of column in legend
loc = 1 #Location for legend
lc='dataset/'
# load data
fil=[lc+'Substitutes.csv']
df1=pd.read_csv(fil[0])
data_x=df1['Unnamed: 0'] # 'names for each group of plots.'
# load data
data1= [df1['Sceptre'],df1['LVAE']]

def bar_plot2(data_x,data_y1):
    font = {'family' : 'Serif',
        'weight' : 'normal',
        'size'   : 14}
    rc('font', **font)
    
    #set color of the bar in the plot
    c2='#D1D0CE'
    c3='#000000'
    
    #To plot
    fig = plt.figure(num=1,figsize=(18,5))
    ax = fig.add_subplot(121)
    list_vals1=np.array(data_y1[0])
    list_vals2=np.array(data_y1[1])
            
    N = len(list_vals1)      
    ind = np.arange(N)  # the x locations for the groups
    width = 0.2       # the width of the bars
    
    b1 = ax.bar(ind, list_vals1, width, color=c2)
    b2 = ax.bar(ind+0.2, list_vals2, width, color=c3)
    
    # add some text for labels, title and axes ticks
    ax.set_ylabel('RunTime in hrs (log scale)',fontsize=18)
#     ax.set_xlabel('Substitutes',fontsize=18)
    ax.set_xticks(ind+width)
    ax.set_xticklabels(data_x)
    ax.legend((b1,b2), ('Sceptre','LVAE'),ncol=n_col,prop={'size':10},frameon=True,loc=loc)
    
    plt.subplots_adjust(bottom = 0.1,top = 0.95,wspace = 0.2,hspace = 0.3 )
    plt.savefig(figure_nam,orientation='portrait',bbox_inches='tight',dpi=300)
#     plt.show()
bar_plot2(data_x,data1)