import pytest
import pandas as pd
import matplotlib
from matplotlib.testing.decorators import image_comparison
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')

import visualize as v

def test_top_ten():
    df = pd.DataFrame(
        data = [
            ["a", 1],
            ["b", 2],
            ["c", 3],
            ["d", 4],
            ["e", 5],
            ["f", 6],
            ["g", 7],
            ["h", 8],
            ["i", 59],
            ["j", 10],
            ["j", 11],
            ["k", 75],
            ["l", 13],
            ["m", 14],
            ["n", 15],
            ["o", 16],
            ["p", 33],
        ],
        columns = ['letter', 'position']
    )
    top_ten_df = v.top_ten(df, 'position')
    assert(len(top_ten_df) == 10)
    assert(top_ten_df.index[0] == df['position'].idxmax())

def test_highlight_max():
    df = pd.DataFrame(
        data = [
            ["a", 1],
            ["b", 2],
            ["c", 3],
            ["d", 4],
            ["e", 5],
            ["f", 6],
            ["g", 75],
            ["h", 8],
            ["i", 59],
            ["j", 10],
            ["j", 11],
            ["k", 75],
            ["l", 13],
            ["m", 14],
            ["n", 15],
            ["o", 16],
            ["p", 33],
        ],
        columns = ['letter', 'position']
    )
    colors = v.highlight_max(df['position'], 'red', 'grey')
    # bad test
    # max_index = df['position'].idxmax()
    # assert(colors[max_index] == 'red')
    # colors.pop(max_index)
    # assert(set(colors) == set(['grey']))
    # better test
    max_value = df['position'].max()
    not_max_colors = []
    for i, value in df['position'].iteritems():
        if value != max_value:
            not_max_colors.append(colors[i])
    assert(set(not_max_colors) == set(['grey']))
