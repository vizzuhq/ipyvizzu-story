---
csv_url: ../../../assets/data/data.csv
---

# Streamlit

## Features

The features of `ipyvizzu-story` that are available in `Streamlit` are marked
with a green check.

- [x]  Display the created `Story` (`play` method)

- [ ]  Display the created `Story` (`_repr_html_` method)

- [x]  Use fullscreen

- [x]  Use navigation buttons

- [x]  Set width/height of the `Story`

- [x]  Export the `Story` into a html file

- [x]  Get the html `Story` as a string

## Installation

Run the following command in your command line in order to install
`ipyvizzu-story` (visit [Installation chapter](../../installation.md) for more
options and details).

```sh
pip install ipyvizzu-story[streamlit]
```

## Sample

Try `ipyvizzu-story` in `Streamlit` with the following sample.

```python
# import ipyvizzu and ipyvizzu-story

from ipyvizzu import Data, Config
from ipyvizzustory import Slide, Step

from ipyvizzustory import Story  # or

# from ipyvizzustory.env.st.story import Story


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
#     "https://ipyvizzu-story.vizzuhq.com/latest/assets/data/data.csv"
# )
# data.add_df(df)

story = Story(data=data)


# create Slides and Steps and add them to the Story

slide1 = Slide(
    Step(
        Config({"x": "Foo", "y": "Bar"}),
    )
)
story.add_slide(slide1)

slide2 = Slide(
    Step(Config({"color": "Foo", "x": "Baz", "geometry": "circle"}))
)
story.add_slide(slide2)


# note: in Streamlit if you want to use the `play` method,
# you need to set the width and height in pixels or set the width to 100%

story.set_size(width="800px", height="480px")


# you can export the Story into a html file

story.export_to_html(filename="mystory.html")

# or you can get the html Story as a string

html = story.to_html()
print(html)


# you can display the Story with the `play` method

story.play()
```

Place the above code blocks into a python file (for example called
`ipyvizzustory_example.py`) and run the following command in your command line
in order to try it.

```sh
streamlit run ipyvizzustory_example.py
```

Check the [Tutorial](../../tutorial/index.md) for more info.
