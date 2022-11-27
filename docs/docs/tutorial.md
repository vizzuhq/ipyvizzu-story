# Tutorial

## Usage

**Note:** ipyvizzu-story uses vizzu and vizzu-story javascript packages and loads them from jsDelivr CDN. If you get a vizzu or vizzu-story releated error in your browser console, please clean your browser cache, because an older version of these could be stored in your browser.

From `ipyvizzu` import Data, Config and Style and from `ipyvizzu-story` import Story, Slide and Step:

```python
from ipyvizzu import Data, Config, Style
from ipyvizzustory import Story, Slide, Step
```

Add the underlying data for the story. You can use the same data definition formats as in the ipyvizzu library, but you must add the entire data set for the whole story in the initial step, you can not change this later. See [ipyvizzu tutorial - Adding data](https://ipyvizzu.vizzuhq.com/tutorial/01_02_adding_data.html) for more details on data formats.

```python
data = Data()
data.add_series("Foo", ["Alice", "Bob", "Ted"])
data.add_series("Bar", [15, 32, 12])
data.add_series("Baz", [5, 3, 2])
```

Put the data object into the `Story` constructor. Here you can also set the `Story` object's `style` property to set the chart style used for the whole story as you can see in our [complex example](../examples/complex/complex.ipynb).
See [ipyvizzu tutorial - Color palette & fonts](https://ipyvizzu.vizzuhq.com/tutorial/01_13_color_palette_fonts.html) and [ipyvizzu tutorial - Chart layout](https://ipyvizzu.vizzuhq.com/tutorial/01_14_chart_layout.html) for more details on style options.

```python
story = Story(data=data)
```

Create the data story by defining a sequence of slides. A slide can be a single chart corresponding to a single `chart.animate()` call from ipyvizzu, see [ipyvizzu tutorial - Intro](https://ipyvizzu.vizzuhq.com/tutorial/01_01_intro.html) for more details. Or a slide can be a sequence of animation calls, in which case all of these animations will be played until the last one in the sequence, allowing for more complex transitions between slides. Navigation controls beneath the chart will navigate between the slides. You can use the PgUp and PgDn buttons, left and right arrows to navigate between slides, and the Home and End buttons to jump to the first or last slide.

On each chart, you can define the chart configuration and style with the same objects as in ipyvizzu. However, you can not modify the underlying data between the slides, only the data filter used. See [ipyvizzu tutorial - Filtering & adding new records](https://ipyvizzu.vizzuhq.com/tutorial/01_11_filter_add_new_records.html) for more details on data filtering options.

```python
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

Before you play the story, many parameters can be changed.

You can enable or disable chart features. See [ipyvizzu tutorial - Axes, title, tooltip](https://ipyvizzu.vizzuhq.com/tutorial/01_03_axes_title_tooltip.html) for more details on chart features.

```python
story.set_feature("tooltip", True)
```

You can add events. See [ipyvizzu tutorial - Events](https://ipyvizzu.vizzuhq.com/tutorial/01_17_events.html) for more details on events.

```python
handler = "alert(JSON.stringify(event.data))"

story.add_event("click", handler)
```

You can set the width and height of the chart.

```python
story.set_size(width="800px", height="480px")
```

Then play the Story.

```python
story.play()
```

For live examples check out our [Example gallery](../examples/index.md)!

## Export

You can export your story to an html file, just place the following code after your story

```python
story.export_to_html(filename="mystory.html")
```

or you can get the html story as a string with the following code:

```python
html = story.to_html()

print(html)
```
