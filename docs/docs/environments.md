# Environments

You can use ipyvizzu-story in Jupyter, Streamlit, Panel or Python environments. ipyvizzu-story tries to figure out the environment and import the correct type of Story, however Story could be imported with full path.

## Jupyter/IPython

In Jupyter/IPython environment, ipyvizzu-story can display and export the created story.

```python
from ipyvizzu import Data, Config
from ipyvizzustory import Slide, Step

from ipyvizzustory import Story  # or
# from ipyvizzustory.env.ipy.story import Story


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

You can change the CSS style width and height parameters of your story with the `set_size` method.

Note: In some of the Jupyter/IPython environments, the width and height must be set in pixels to display the story correctly.

```python
story.set_size(width="800px", height="480px")
```

You can export your pure story into a html file with the `export_to_html` method.

```python
story.export_to_html(filename="mystory.html")
```

You can display your story with the `play` method,

```python
story.play()
```

or you can also use the `_repr_html_` method.

```python
story
```

Install ipyvizzu-story (see [Installation chapter](installation.md) of our documentation site),

```sh
pip install ipyvizzu-story[jupyter]
```

and place the above codes in a Jupyter Notebook cell in order to try it.

## Streamlit

In Streamlit environment, ipyvizzu-story can display and export the created story.

```python
from ipyvizzu import Data, Config
from ipyvizzustory import Slide, Step

from ipyvizzustory import Story  # or
# from ipyvizzustory.env.st.story import Story


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

Note: In Streamlit environment you need to set the width and height of your story in pixels as int.

```python
story.set_size(width=800, height=480)
```

You can export your pure story into a html file with the `export_to_html` method.

```python
story.export_to_html(filename="mystory.html")
```

You can display your story with the `play` method.

```python
story.play()
```

Install ipyvizzu-story (see [Installation chapter](installation.md) of our documentation site),

```sh
pip install ipyvizzu-story[streamlit]
```

and place the above code in a file (for example called `ipyvizzustory_example.py`)
and run the following command in order to try it.

```sh
streamlit run ipyvizzustory_example.py
```

## Panel

In Panel environment, ipyvizzu-story can display and export the created story.

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

You can export your pure story into a html file with the `export_to_html` method.

```python
story.export_to_html(filename="mystory.html")
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

Install ipyvizzu-story (see [Installation chapter](installation.md) of our documentation site),

```sh
pip install ipyvizzu-story[panel]
```

and place the above code in a file (for example called `ipyvizzustory_example.py`)
and run the following command in order to try it.

```sh
panel serve ipyvizzustory_example.py --autoreload
```

## Python

In Python environment, ipyvizzu-story can can export the created story to an html file.

Note: In Python environment ipyvizzu-story can not display the created story.

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

story.export_to_html(filename="mystory.html")
```

Install ipyvizzu-story (see [Installation chapter](installation.md) of our documentation site),

```sh
pip install ipyvizzu-story
```

and place the above code in a file (for example called `ipyvizzustory_example.py`)
and run the following command in order to try it.

```sh
python3 ipyvizzustory_example.py
```
