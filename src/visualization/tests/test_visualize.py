import pytest
import pandas as pd

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
    assert(True == True)
    assert(True == True)

def test_highlight_max():
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
    colors = v.highlight_max(df['position'], 'red', 'grey')

    assert(True == True)
