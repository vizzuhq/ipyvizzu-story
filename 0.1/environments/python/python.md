---
csv_url: ../../assets/data/data.csv
---

# Python

## Features

The features of `ipyvizzu-story` that are available in `Python` are marked with
a green check.

- [ ] Display the created `Story` (`play` method)

- [ ] Display the created `Story` (`_repr_html_` method)

- [x] Use fullscreen \*

- [x] Use navigation buttons \*

- [x] Set width/height of the `Story` \*

- [x] Export the `Story` into a html file

- [x] Get the html `Story` as a string

\*can only be used in the exported html file.

## Installation

Run the following command in your command line in order to install
`ipyvizzu-story` (visit [Installation chapter](../installation.md) for more
options and details).

```sh
pip install ipyvizzu-story
```

## Sample

Try `ipyvizzu-story` in `Python` with the following sample.

```python
# import ipyvizzu and ipyvizzu-story

from ipyvizzu import Data, Config
from ipyvizzustory import Slide, Step

from ipyvizzustory import Story  # or

# from ipyvizzustory.py_env.story import Story


# create data and initialize Story with the created data

data = Data()
data.add_series("Foo", ["Alice", "Bob", "Ted"])
data.add_series("Bar", [15, 32, 12])
data.add_series("Baz", [5, 3, 2])

# you can also add data with pandas

# import pandas as pd
#
# data = Data()
# df = pd.read_csv(
#     "https://ipyvizzu-story.vizzuhq.com/0.1/assets/data/data.csv"
# )
# data.add_data_frame(df)

story = Story(data=data)


# create Slides and Steps and add them to the Story

slide1 = Slide(
    Step(
        Config({"x": "Foo", "y": "Bar"}),
    )
)
story.add_slide(slide1)

slide2 = Slide(
    Step(
        Config({"color": "Foo", "x": "Baz", "geometry": "circle"}),
    )
)
story.add_slide(slide2)


# you can get the html Story as a string

html = story.to_html()
print(html)
```

Place the above code blocks into a python file (for example called
`ipyvizzustory_example.py`) and run the following command in your command line
in order to try it.

```sh
python3 ipyvizzustory_example.py
```

Check the [Tutorial](../tutorial/index.md) for more info.