# Panel

You can use ipyvizzu-story in Panel with the following restrictions:

- [x] Display the created Story (`play` method)
- [x] Display the created Story (`_repr_html_` method) *
- [x] Use fullscreen
- [x] Use navigation buttons

- [x] Set width/height of the Story

- [x] Export the Story into a html file
- [x] Get the html story as a string

*for example, used in `pn.pane.HTML` method

```python
from ipyvizzu import Data, Config
from ipyvizzustory import Slide, Step
from ipyvizzustory.env.pn.story import Story


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

Note: In Panel environment if you want to use the `play` method,
you need to set the width and height of your story in pixels.

```python
story.set_size(width="800px", height="480px")
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

You can display your story with the `play` method,

```python
story.play()
```

or you can customize the Panel environment before displaying your story,

```python
import panel as pn

# ...

pn.extension(sizing_mode="stretch_width", template="fast")

pn.state.template.param.update(
    title="ipyvizzu-story",
)

story.play()
```

or if you would like to customize it completely,
you can do it with the `_repr_html_` method.

```python
import panel as pn

# ...

pn.extension(sizing_mode="stretch_width", template="fast")

pn.state.template.param.update(
    title="ipyvizzu-story",
)

pn.pane.HTML(
    story,
    height=500,
    sizing_mode="stretch_both"
).servable()
```

Install ipyvizzu-story (see [Installation chapter](../installation.md) of our documentation site),

```sh
pip install ipyvizzu-story[panel]
```

and place the above code in a file (for example called `ipyvizzustory_example.py`)
and run the following command in order to try it.

```sh
panel serve ipyvizzustory_example.py --autoreload
```
