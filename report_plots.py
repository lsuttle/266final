from scipy.stats.stats import pearsonr 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
plt.style.use('seaborn-notebook')

def descriptives(unique_users, body, drange3, seasons):
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize = [9,9])

    fig.suptitle('Comments increase over time, spike when show is on-air', fontsize=14)

    years = mdates.YearLocator()
    yearsFmt = mdates.DateFormatter('%Y')
    months = mdates.MonthLocator()

    ax1.xaxis.set_major_locator(years)
    ax1.xaxis.set_major_formatter(yearsFmt)
    ax1.xaxis.set_minor_locator(months)
    
    ax1.set_title("Unique Users Per Month")
    ax1.set_xlabel('Date')
    ax1.set_ylabel('# Unique Users')

    ax1.plot(drange3[:-1],[len(x) for x in unique_users])
    for pair in seasons:
        ax1.axvspan(pair[0], pair[1], alpha=0.5, color='lightgrey', label='season')
    ax1.grid(True, linestyle='--', color='lightgrey')
    ax1.patch.set_facecolor('white')

    ax2.xaxis.set_major_locator(years)
    ax2.xaxis.set_major_formatter(yearsFmt)
    ax2.xaxis.set_minor_locator(months)
    
    ax2.set_title("Unique Comments Per Month")
    ax2.set_xlabel('Date')
    ax2.set_ylabel('# Comments')

    ax2.plot(drange3[:-1],[len(x) for x in body])
    for pair in seasons:
        ax2.axvspan(pair[0], pair[1], alpha=0.5, color='lightgrey')
    ax2.patch.set_facecolor('white')
    ax2.grid(True, linestyle='--', color='lightgrey')
    
    
def descriptives2(lengths, per_new, drange3, seasons):
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize = [9,9])

    years = mdates.YearLocator()
    yearsFmt = mdates.DateFormatter('%Y')
    months = mdates.MonthLocator()

    ax1.xaxis.set_major_locator(years)
    ax1.xaxis.set_major_formatter(yearsFmt)
    ax1.xaxis.set_minor_locator(months)

    ax1.set_xlabel('Date')
    ax1.set_ylabel('median post length')

    ax1.plot(drange3[13:-1], [np.median(x) for x in lengths])

    for pair in seasons[2:]:
        ax1.axvspan(pair[0], pair[1], alpha=0.5, color='lightgrey')
    ax1.patch.set_facecolor('white')
    ax1.grid(True, linestyle='--', color='lightgrey')
    
    ax2.xaxis.set_major_locator(years)
    ax2.xaxis.set_major_formatter(yearsFmt)
    ax2.xaxis.set_minor_locator(months)

    ax2.set_xlabel('Date')
    ax2.set_ylabel('% of posts from new users')

    ax2.plot(drange3[13:-1], per_new)

    for pair in seasons[2:]:
        ax2.axvspan(pair[0], pair[1], alpha=0.5, color='lightgrey')
    ax2.patch.set_facecolor('white')
    ax2.grid(True, linestyle='--', color='lightgrey')

def results_plot(avg_scores, avg_new_user_scores, avg_old_user_scores, drange3, seasons):
    fig, ax = plt.subplots()

    years = mdates.YearLocator()
    yearsFmt = mdates.DateFormatter('%Y')
    months = mdates.MonthLocator()

    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(yearsFmt)
    ax.xaxis.set_minor_locator(months)

    fig.suptitle('Cross entropy decreases over time for all users', fontsize=14)

    ax.set_xlabel('Date')
    ax.set_ylabel('Cross-Entropy')

    ax.plot(drange3[13:-1],[np.median(score) for score in avg_scores], color = 'black', label='all users')
    ax.plot(drange3[13:-1],[np.median(score) for score in avg_new_user_scores], color='orange', linestyle='--', label = 'new users')
    ax.plot(drange3[13:-1],[np.median(score) for score in avg_old_user_scores], 
            color = 'blue', linestyle='--', label='existing users')

    for pair in seasons[2:]:
        ax.axvspan(pair[0], pair[1], alpha=0.5, color='lightgrey')
    ax.patch.set_facecolor('white')
    ax.grid(True, linestyle='--', color='lightgrey')

    legend = ax.legend()
    legend.get_frame().set_facecolor('white')
    legend.get_frame().set_edgecolor('darkgrey')
    
def corr_plot(x,y):
    fig, ax = plt.subplots()

    left, width = .25, 0.7
    bottom, height = .25, 0.7
    right = left + width
    top = bottom + height

    fig.suptitle('No relationship between cross-entropy and comment score', fontsize=14)

    ax.set_xlabel('Cross Entropy')
    ax.set_ylabel('Comment Score')

    ax.scatter(x,y, alpha=.25, edgecolors='none')

    ax.text(right, top, 'r = ' + str(round(pearsonr(x, y)[0], 2)),
        horizontalalignment='right',
        verticalalignment='top',
        transform=ax.transAxes)

    ax.patch.set_facecolor('white')
    ax.grid(True, linestyle='--', color='lightgrey')