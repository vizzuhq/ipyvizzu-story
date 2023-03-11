---
csv_url: ../../../assets/data/data.csv
---

# Flask

## Features

The features of `ipyvizzu-story` that are available in `Flask` are marked with a
green check.

- [ ] Display the created `Story` (`play` method) \*

- [ ] Display the created `Story` (`_repr_html_` method) \*

- [x] Use fullscreen

- [x] Use navigation buttons

- [x] Set width/height of the `Story`

- [x] Export the `Story` into a html file

- [x] Get the html `Story` as a string

\*you can display the created `Story` in other ways, see the sample below

## Installation

Run the following command in your command line in order to install
`ipyvizzu-story` (visit [Installation chapter](../../installation.md) for more
options and details).

```sh
pip install ipyvizzu-story flask
```

## Sample

Try `ipyvizzu-story` in `Flask` with the following sample.

```python
# import flask, ipyvizzu and ipyvizzu-story

from pathlib import Path

from ipyvizzu import Data, Config
from ipyvizzustory import Slide, Step

from ipyvizzustory import Story  # or

# from ipyvizzustory.env.py.story import Story

from flask import Flask, render_template


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


# you can set the width and height (CSS style)

story.set_size(width="800px", height="480px")


# you can export the Story into a html file

Path("static").mkdir(parents=True, exist_ok=True)
story.export_to_html(filename="static/mystory.html")

# or you can get the html Story as a string

html = story.to_html()


# you can display the Story from the saved string

app = Flask(__name__)


@app.route("/")
def vizzu():
    return render_template("vizzu.html", mystory=html)
```

Place the above code blocks into a python file (for example called
`application.py`), create the html template (`templates/vizzu.html`) with the
following content if you display the `Story` from the saved string

```html
<!DOCTYPE html>
<html>
 <body>
  <div class="container">
   <iframe frameborder="0" height="480px" scrolling="no" src="data:text/html, {{ mystory }}" width="800px">
   </iframe>
  </div>
 </body>
</html>

```

or with the following if you display the `Story` from the exported html file

```html
<!DOCTYPE html>
<html>
 <body>
  <div class="container">
   <iframe frameborder="0" height="480px" scrolling="no" src=" {{url_for('static', filename='/mystory.html')}}" width="800px">
   </iframe>
  </div>
 </body>
</html>

```

and run the following command in your command line in order to try it.

```sh
flask --app application run
```

Check the [Tutorial](../../tutorial/index.md) for more info.
