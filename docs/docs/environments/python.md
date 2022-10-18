# Python

You can use ipyvizzu-story in Python with the following restrictions:

- [ ] Display the created Story (`play` method)
- [ ] Display the created Story (`_repr_html_` method)
- [x] Use fullscreen *
- [x] Use navigation buttons *

- [x] Set width/height of the Story *

- [x] Export the Story into a html file
- [x] Get the html story as a string

*can only be used in the exported html file.

```python
from ipyvizzu import Data, Config
from ipyvizzustory import Slide, Step
from ipyvizzustory import Story  # or
# from ipyvizzustory.env.py.story import Story


data = Data()
data.add_series("Foo", ["Alice", "Bob", "Ted"])
data.add_series("Bar", [15, 32, 12])
data.add_series("Baz", [5, 3, 2])

story = Story(data=data)

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

You can export your pure story into a html file with the `export_to_html` method

```python
story.export_to_html(filename="mystory.html")
```

or you can get the html story as a string with the `to_html` method:

```python
html = story.to_html()

print(html)
```

Install ipyvizzu-story (see [Installation chapter](../installation.md) of our documentation site),

```sh
pip install ipyvizzu-story
```

and place the above code in a file (for example called `ipyvizzustory_example.py`)
and run the following command in order to try it.

```sh
python3 ipyvizzustory_example.py
```