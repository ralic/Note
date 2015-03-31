import numpy as np
import pandas as pd
from functools import partial


def summary(df, fn=np.sum, axis=0, name='Total', table_class_prefix='dataframe-summary'):
    """Append a summary row or column to DataFrame.
    Input:
    ------
    df : Dataframe to be summarized
    fn : Summary function applied over each column
    axis : Axis to summarize on (1: by row, 0: by column)
    name : Index or column label for summary
    table_class_prefix : Custom css class for dataframe

    Returns:
    --------
    Dataframe with applied summary.

    """
    total = df.apply(fn, axis=axis).to_frame(name)
    table_class = ""
    if axis == 0:
        total = total.T
        table_class = "{}-row".format(table_class_prefix)
    elif axis == 1:
        table_class = "{}-col".format(table_class_prefix)

    out = pd.concat([df, total], axis=axis)
    # Patch to_html function to use custom css class
    out.to_html = partial(out.to_html, classes=table_class)
    return out

if __name__ == '__main__':
    summary(pd.DataFrame([1, 2, 3], columns=["a", "b", "c"]), axis=0)
