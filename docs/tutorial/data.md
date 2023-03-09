---
csv_url: ../../assets/data/data.csv
---

# Data

You can use the same data definition formats as in the `ipyvizzu` library.

!!! tip
    See
    [ipyvizzu - Data chapter](https://ipyvizzu.vizzuhq.com/latest/tutorial/data/)
    for more details about data formats.

Below you can see some commonly used cases.

## Using pandas DataFrame

```python
from ipyvizzu import Data
import pandas as pd


data = Data()
df = pd.read_csv(
    "https://ipyvizzu-story.vizzuhq.com/latest/assets/data/data.csv"
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
