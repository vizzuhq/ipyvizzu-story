# Building blocks

In`ipyvizzu-story`, you can build, show and export a `Story` object that
contains all of the data being shown throughout the story and the charts created
based on that data, arranged into `Slides` and `Steps`.

## Slides and Steps

`Slides` can contain one or more `Steps`.

A `Step` (and a single-Step `Slide`) is basically the same as the `Chart` object
in [ipyvizzu](https://ipyvizzu.vizzuhq.com/0.15/tutorial/), with some minor,
but important differences (for now):

- all of the data has to be added to the story at initialization, and it can be
  filtered at every `Step` throughout the `Story`.
- animation options are not available

```python
slide = Slide(
    Step(
        Config({"x": "Foo", "y": "Bar"}),
    )
)
story.add_slide(slide)
```

In case of a `Slide` with a sequence of `Steps`, all, but the last `Steps` are
interim charts that connect a `Slide` with a previous `Slide`. The animation
will be automatically played until the last `Step` in the sequence, allowing for
more complex transitions between `Slides`.

```python
slide = Slide()
slide.add_step(
    Step(
        Config({"color": "Foo", "x": "Baz", "geometry": "circle"}),
    )
)
slide.add_step(
    Step(
        Config({"x": "Foo", "y": "Bar", "geometry": "rectangle"}),
    )
)
story.add_slide(slide)
```

Viewers can navigate between `Slides` with the navigation controls that appear
beneath the chart. They can also use the `PgUp` and `PgDn` buttons, and the left
and right arrows to navigate between `Slides`, and the `Home` and `End` buttons
to jump to the first and last `Slide` in the `Story`.

On each chart, you can define the chart configuration and style using the same
objects as in `ipyvizzu`. However, you can not modify the underlying data
between the slides, just the data filter can be used.

```python
slide = Slide(
    Step(
        Data.filter("record['Foo'] == 'Bob'"),
        Config({"geometry": "circle"}),
        Style({"plot": {"marker": {"colorPalette": "#FF0000"}}}),
    )
)
story.add_slide(slide)
```

!!! tip
    Check
    [ipyvizzu - Filtering & adding new records chapter](https://ipyvizzu.vizzuhq.com/0.15/tutorial/filter_add_new_records/)
    for more details on data filtering options.

There are some parameters of the `Story` you can change before you play it.

## Story features

You can enable or disable chart features, such as the `Tooltip` that appears if
the viewer hovers their mouse over a specific element of the chart.

```python
story.set_feature("tooltip", True)
```

!!! tip
    See
    [ipyvizzu - Axes, title, tooltip chapter](https://ipyvizzu.vizzuhq.com/0.15/tutorial/axes_title_tooltip/)
    for more details on chart features.

## Story events

You have many more options to change the look and feel of the `Story` by using
events.

```python
handler = "alert(JSON.stringify(event.data))"

story.add_event("click", handler)
```

!!! tip
    See
    [ipyvizzu - Events chapter](https://ipyvizzu.vizzuhq.com/0.15/tutorial/events/)
    for more details on events.

## Play

After you created the `Story`, you can play it with the `play`, or the
`_repr_html_` method, depending on the environment you run `ipyvizzu-story` in.

```python
story.play()
```

or

```python
story
```

!!! info
    If you run into issues with playing your story, check the
    [Environments chapter](../environments/index.md) for more details on the
    available features in your environment.
