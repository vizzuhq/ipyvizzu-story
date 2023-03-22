---
csv_url: ../../../assets/data/data.csv
---

# Mercury/mljar

## Features

The features of `ipyvizzu-story` that are available in `Mercury/mljar` are
marked with a green check.

- [x] Display the created `Story` (`play` method)

- [ ] Display the created `Story` (`_repr_html_` method)

- [x] Use fullscreen

- [x] Use navigation buttons

- [x] Set width/height of the `Story`

- [ ] Export the `Story` into a html file

- [x] Get the html `Story` as a string

## Live example

[![Open in Mercury](https://raw.githubusercontent.com/mljar/mercury/main/docs/media/open_in_mercury.svg)](https://huggingface.co/spaces/veghdev/ipyvizzu-story-demo)

## Installation

Add `ipyvizzu-story` to `requirements.txt`.

```
python-dotenv
pandas
mljar-mercury
ipyvizzu-story
```

## Sample

Try `ipyvizzu-story` in `Mercury/mljar` with the following sample.

```
---
title: ipyvizzu-story demo
description: ipyvizzu-story demo with mercury
show-code: False
params:
params:
    selected:
        input: select
        label: select what you want to see
        choices: [animation, code]
        multi: True
---
```

```python
# configure default value

selected = ["animation"]


# import ipyvizzu and ipyvizzu-story

from ipyvizzu import Data, Config
from ipyvizzustory import Slide, Step

from ipyvizzustory import Story  # or

# from ipyvizzustory.env.ipy.story import Story

from IPython.display import display as display_html, HTML


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
#     "https://ipyvizzu-story.vizzuhq.com/0.5/assets/data/data.csv"
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


# you can set the width and height (CSS style)

story.set_size(width="800px", height="480px")


# you can get the html Story as a string

html = story.to_html()


if "animation" is selected:
    # you can display the Story with the `play` method
    story.play()
if "code" is selected:
    # you can display the html code
    display_html(html)
```

Check the [Tutorial](../../tutorial/index.md) for more info.
