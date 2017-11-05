def top_ten(df, column, index=True):
    '''Returns 10 highest values of df.column'''
    if index != True:
        df = df.set_index(index)
    return df.sort_values(column, ascending=False)[column].head(10)

def highlight_max(data, highlight, standard):
    '''Sets biggest value to highlight color'''
    return [highlight if (x == max(data.values)) else standard for x in data.values]

def create_empty_fig(xlabel='', ylabel=''):
    '''Returns empty Tufte-style fig, ax objects'''
    # create figures and axes objects to modify
    # fig controls figure-level settings (across group of subplots)
    # ax controls axis-level settings (across each subplot)
    fig, ax = plt.subplots(figsize=(10,8))

    # remove square outline
    ax.set_frame_on(False)

    return fig, ax

def set_axes_labels(ax, xlabel='', ylabel=''):
    '''Adds axes labels'''
    # add labels for axes
    ax.set(xlabel=xlabel, ylabel=ylabel)
    return ax

def format_xticks(data, ax, xticks=True, xticksrotate=False):
    '''Formats xtick labels to title case if True, removes xtick labels if False'''
    if (xticks == True and xticksrotate == False):
        ax.set_xticklabels([label.title() for label in data.index])

    elif (xticks == True and xticksrotate == True):
        ax.set_xticklabels([label.title() for label in data.index], rotation=45, ha='right')

    elif (xticks == False):
        ax.set_xticklabels([])

    return ax

def add_bar_labels(data, ax):
    '''Removes y-axis label and adds direct labels to tops of bars of sns barplot'''
    # remove y axis tick labels
    ax.set_yticklabels([])

    # label each bar with y value
    labels = data.values
    y_margin = max(labels) * 0.01
    for bar, label in zip(ax.patches, labels):
        #x location of label
        x = bar.get_x()
        bar_width = bar.get_width()
        center = x + bar_width/2.0

        #y location of label
        bar_height = bar.get_height()

        ax.text(x=center, y=bar_height + y_margin, s=label, ha='center')

    return ax

def bar_chart(data, highlight='grey', standard='grey', xlabel='', ylabel='', title='', xticksrotate=False):
    '''
    Creates Tufte-style bar chart with highest values highlighted
    Note: data is a series with labeled indices
    '''
    # create empty fig, ax
    fig, ax = create_empty_fig()

    # draw plot bar
    colors = highlight_max(data, highlight, standard)
    ax = sns.barplot(x=data.index, y=data.values, palette=colors, ax=ax)

    ax = set_axes_labels(ax, xlabel=xlabel, ylabel=ylabel)

    # format xtick labels
    ax = format_xticks(data, ax, xticksrotate=xticksrotate)

    # add labels on top of bars
    ax = add_bar_labels(data, ax)

    # add a meaningful title
    ax.set_title(title, loc='left')

    return fig, ax
