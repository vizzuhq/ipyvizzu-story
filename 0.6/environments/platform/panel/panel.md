---
csv_url: ../../../assets/data/data.csv
---

# Panel

## Features

The features of `ipyvizzu-story` that are available in `Panel` are marked with a
green check.

- [x] Display the created `Story` (`play` method)

- [x] Display the created `Story` (`_repr_html_` method) \*

- [x] Use fullscreen

- [x] Use navigation buttons

- [x] Set width/height of the `Story`

- [x] Export the `Story` into a html file

- [x] Get the html `Story` as a string

\*for example, used in `pn.pane.HTML` method

## Installation

Run the following command in your command line in order to install
`ipyvizzu-story` (visit [Installation chapter](../../installation.md) for more
options and details).

```sh
pip install ipyvizzu-story[panel]
```

## Sample

Try `ipyvizzu-story` in `Panel` with the following sample.

```python
# import ipyvizzu and ipyvizzu-story

from ipyvizzu import Data, Config
from ipyvizzustory import Slide, Step

from ipyvizzustory.env.pn.story import Story


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
#     "https://ipyvizzu-story.vizzuhq.com/0.6/assets/data/data.csv"
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


# note: in Panel if you want to use the `play` method,
# you need to set the width and height in pixels

story.set_size(width="800px", height="480px")


# you can export the Story into a html file

story.export_to_html(filename="mystory.html")

# or you can get the html Story as a string

html = story.to_html()
print(html)


# you can display the Story with the `play` method

story.play()


# or you can customize Panel before `play`

# import panel as pn
#
# pn.extension(sizing_mode="stretch_width", template="fast")
#
# pn.state.template.param.update(
#     title="ipyvizzu-story",
# )
#
# story.play()


# or if you would like to customize it completely,
# you can do it with the `_repr_html_` method

# import panel as pn
#
# pn.extension(sizing_mode="stretch_width", template="fast")
#
# pn.state.template.param.update(
#     title="ipyvizzu-story",
# )
#
# pn.pane.HTML(
#     story,
#     height=500,
#     sizing_mode="stretch_both"
# ).servable()
```

Place the above code blocks into a python file (for example called
`ipyvizzustory_example.py`) and run the following command in your command line
in order to try it.

```sh
panel serve ipyvizzustory_example.py --autoreload
```

Check the [Tutorial](../../tutorial/index.md) for more info.
