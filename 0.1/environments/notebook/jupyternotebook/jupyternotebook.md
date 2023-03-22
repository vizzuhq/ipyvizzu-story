---
csv_url: ../../../assets/data/data.csv
---

# Jupyter Notebook

## Features

The features of `ipyvizzu-story` that are available in `Jupyter Notebook` are
marked with a green check.

- [x] Display the created `Story` (`play` method)

- [x] Display the created `Story` (`_repr_html_` method)

- [x] Use fullscreen

- [x] Use navigation buttons

- [x] Set width/height of the `Story`

- [x] Export the `Story` into a html file

- [x] Get the html `Story` as a string

## Installation

Run the following command in your command line

```sh
pip install ipyvizzu-story[jupyter]
```

or place the following code into a notebook cell in order to install
`ipyvizzu-story` (visit [Installation chapter](../../installation.md) for more
options and details).

```
!pip install ipyvizzu-story[jupyter]
```

## Sample

Try `ipyvizzu-story` in `Jupyter Notebook` with the following sample.

```python
# import ipyvizzu and ipyvizzu-story

from ipyvizzu import Data, Config
from ipyvizzustory import Slide, Step

from ipyvizzustory import Story  # or

# from ipyvizzustory.ipy_env.story import Story


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


# you can display the Story with the `play` method

story.play()


# or you can also use the `_repr_html_` method.

# story
```

Check the [Tutorial](../../tutorial/index.md) for more info.
