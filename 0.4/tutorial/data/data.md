---
csv_url: ../../assets/data/data.csv
---

# Data

You can use the same data definition formats as in the `ipyvizzu` library:
`pandas DataFrame`, `JSON`, or add data manually in different formats. Similarly
to `ipyvizzu`, there are two types of data series: dimensions and measures.

!!! note
    Please note, that all of the data used throughout your data story has to be
    added to the story at initialization. The data being shown can be filtered
    at each step.

!!! tip
    See
    [ipyvizzu - Data chapter](https://ipyvizzu.vizzuhq.com/0.15/tutorial/data/)
    for more details about data.

Here's some sample code for common use cases.

## Using pandas DataFrame

```python
from ipyvizzu import Data
import pandas as pd


data = Data()
df = pd.read_csv(
    "https://ipyvizzu-story.vizzuhq.com/0.4/assets/data/data.csv"
)
data.add_data_frame(df)
```

## Specify data by series

```python
from ipyvizzu import Data


data = Data()
data.add_series("Foo", ["Alice", "Bob", "Ted"])
data.add_series("Bar", [15, 32, 12])
data.add_series("Baz", [5, 3, 2])
```
