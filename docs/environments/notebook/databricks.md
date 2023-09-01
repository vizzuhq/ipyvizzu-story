---
csv_url: ../../../assets/data/data.csv
---

# Databricks

## Features

The features of `ipyvizzu-story` that are available in `Databricks` are marked
with a green check.

- [x]  Display the created `Story` (`play` method)

- [x]  Display the created `Story` (`_repr_html_` method)

- [x]  Use fullscreen

- [x]  Use navigation buttons

- [x]  Set width/height of the `Story` \*

- [x]  Export the `Story` into a html file

- [x]  Get the html `Story` as a string

\*mandatory

## Live example

[Open in Databricks](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/808850182010194/1655405509226124/1947355309752283/latest.html)

## Installation

Place the following code into a notebook cell in order to install
`ipyvizzu-story` (visit [Installation chapter](../../installation.md) for more
options and details).

```
!pip install ipyvizzu-story[jupyter]
```

## Sample

Try `ipyvizzu-story` in `Databricks` with the following sample.

```python
# import ipyvizzu and ipyvizzu-story

from ipyvizzu import Data, Config
from ipyvizzustory import Slide, Step

from ipyvizzustory import Story  # or

# from ipyvizzustory.env.ipy.story import Story


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
    Step(
        Config({"color": "Foo", "x": "Baz", "geometry": "circle"}),
    )
)
story.add_slide(slide2)


# note: in Databricks,
# you need to set the width and height (CSS style)

story.set_size(width="800px", height="480px")


# you can export the Story into a html file

# `databricks_unique_id` is your id which can be found after `?o=` in the url)
databricks_unique_id = "000000000000000"
html_file = "mystory.html"

story.export_to_html(filename=f"/{html_file}")

dbutils.fs.cp(f"file:/{html_file}", f"dbfs:/FileStore/{html_file}")
displayHTML(
    f'<a href="/files/{html_file}/?o={databricks_unique_id}"'
    + " "
    + "download>Download HTML</a>"
)

# or you can get the html Story as a string

html = story.to_html()
print(html)


# you can display the Story with the `play` method

story.play()


# or you can also use the `_repr_html_` method.

# story
```

Check the [Tutorial](../../tutorial/index.md) for more info.
