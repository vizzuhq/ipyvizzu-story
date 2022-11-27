# Databricks

You can use ipyvizzu-story in Databricks with the following restrictions:

- [x] Display the created Story (`play` method)

- [x] Display the created Story (`_repr_html_` method)

- [x] Use fullscreen

- [x] Use navigation buttons

- [x] Set width/height of the Story \*

- [x] Export the Story into a html file

- [x] Get the html Story as a string

\*mandatory

## Installation

Place the following code into a notebook cell in order to install ipyvizzu-story (for more installation options and details see [Installation chapter](../../installation.md) of our documentation site).

```
!pip install ipyvizzu-story[jupyter]
```

## Example

Below you can see an example, place the following code blocks into notebook cells in order to try it in Databricks.

For more information regarding to how to use ipyvizzu-story please check [Tutorial chapter](../../tutorial.md) of our documentation site.

```python
# import ipyvizzu and ipyvizzu-story

from ipyvizzu import Data, Config
from ipyvizzustory import Slide, Step

from ipyvizzustory import Story  # or

# from ipyvizzustory.env.ipy.story import Story
```

```python
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
#     "https://raw.githubusercontent.com/" +
#     "vizzuhq/ipyvizzu-story/main/" +
#     "docs/examples/basic/basic.csv"
# )
# data.add_data_frame(df)

story = Story(data=data)
```

```python
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
```

```python
# note: in Databricks,
# you need to set the width and height (CSS style)

story.set_size(width="800px", height="480px")
```

```python
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
```

```python
# you can display the Story with the `play` method

story.play()
```

```python
# or you can also use the `_repr_html_` method.

# story
```

## Try it!

Place the above code blocks into notebook cells in order to try it.
