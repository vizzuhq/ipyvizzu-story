# Databricks

You can use ipyvizzu-story in Databricks with the following restrictions:

- [x] Display the created Story (`play` method)
- [x] Display the created Story (`_repr_html_` method)
- [x] Use fullscreen
- [x] Use navigation buttons

- [x] Set width/height of the Story *

- [x] Export the Story into a html file **
- [x] Get the html story as a string

*mandatory
**ipyvizzu-story works in the exported html which was made with the `export_to_html` method,
but currently does not work in the Databricks build-in published html.

Install ipyvizzu-story (see [Installation chapter](../../installation.md) of our documentation site).

```python
!pip install ipyvizzu-story[jupyter]
```

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

Note: In Databricks, the Story does not appear correctly if the size is not set.

```python
story.set_size(width="800px", height="480px")
```

You can export your pure story into a html file with the `export_to_html` method
(where databricks_unique_id is your unique id which can be found after `?o=` in the url)

```python
databricks_unique_id = "000000000000000"
html_file = "mystory.html"

story.export_to_html(filename=f"/{html_file}")

dbutils.fs.cp (f"file:/{html_file}", f"dbfs:/FileStore/{html_file}")
displayHTML(f"""<a href="/files/{html_file}/?o={databricks_unique_id}" download>Download HTML</a>""")
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

or you can also use the `_repr_html_` method.

```python
story
```

Place the above code in a notebook in order to try it.
