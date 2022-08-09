# Environments

You can use ipyvizzu-story in Jupyter, Streamlit, Panel or Python environments. ipyvizzu-story tries to figure out the environment and import the correct type of Story, however Story could be imported with full path.

## Jupyter/IPython

In Jupyter/IPython environment, ipyvizzu-story can display and export the created html code.

You can also use `Story._repr_html_()` method to display your story.

In some of the Jupyter/IPython environments you need to set the width and height of your Story in pixels in order to display the story correctly.

```python
from ipyvizzu import Data, Config
from ipyvizzustory import Slide, Step
from ipyvizzustory import Story  # from ipyvizzustory.env.ipy.story import Story


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

# story.set_size(width="800px", height="480px")

story.play()  # or just `story` if you would like to use `_repr_html_`

story.export_to_html(filename="mystory.html")
```

After installing ipyvizzu-story (see [Installation chapter](installation.md) of our documentation site),
place the above code in a Jupyter Notebook cell.

## Streamlit

In Streamlit environment, ipyvizzu-story can display and export the created html code.

You need to set the width and height of your Story in pixels as int.

```python
from ipyvizzu import Data, Config
from ipyvizzustory import Slide, Step
from ipyvizzustory import Story  # from ipyvizzustory.env.st.story import Story


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

story.set_size(width=800, height=480)

story.play()

story.export_to_html(filename="mystory.html")
```

After installing ipyvizzu-story (see [Installation chapter](installation.md) of our documentation site),
place the above code in a file (for example called `ipyvizzustory_example.py`) and run the following command:

```sh
streamlit run ipyvizzustory_example.py
```

## Panel

In Panel environment, ipyvizzu-story can display and export the created html code.

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

story.export_to_html(filename="mystory.html")

# ...
```

If you would like to try ipyvizzu-story in Panel without customizing it,
we have configured a working environment in the `play` method

```python
# ...

story.play(width=800, height=480)
```

or you can configure and use your own.
In that case instead of `play` you should use the `_repr_html_` method of the `Story`.

```python
import panel as pn

# ...

story_width = "800px"
story_height = "480px"

story.set_size(width=story_width, height=story_height)

pn.extension(sizing_mode="stretch_width", template="fast")

pn.state.template.param.update(
    title="ipyvizzu-story",
)

pn.pane.HTML(
    story,
    height=int(story_height[:-2]) + 10,
    sizing_mode="stretch_both"
).servable()
```

After installing ipyvizzu-story (see [Installation chapter](installation.md) of our documentation site),
place the above code in a file (for example called `ipyvizzustory_example.py`) and run the following command:

```sh
panel serve ipyvizzustory_example.py --autoreload
```

## Python

In basic Python environment, ipyvizzu-story can not display the created html code, but it can export it to an html file.

```python
from ipyvizzu import Data, Config
from ipyvizzustory import Slide, Step
from ipyvizzustory import Story  # from ipyvizzustory.env.py.story import Story


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

story.export_to_html(filename="mystory.html")
```

After installing ipyvizzu-story (see [Installation chapter](installation.md) of our documentation site),
place the above code in a file (for example called `ipyvizzustory_example.py`) and run the following command:

```sh
python3 ipyvizzustory_example.py
```
