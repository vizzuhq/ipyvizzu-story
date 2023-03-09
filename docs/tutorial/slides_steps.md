# Slides and Steps

Create the data story by defining a sequence of slides. A slide can be a single
chart corresponding to a single `chart.animate` call from
[ipyvizzu](https://ipyvizzu.vizzuhq.com/latest/tutorial/). Or a slide can be a
sequence of animation calls, in which case all of these animations will be
played until the last one in the sequence, allowing for more complex transitions
between slides. Navigation controls beneath the chart will navigate between the
slides. You can use the `PgUp` and `PgDn` buttons, left and right arrows to
navigate between slides, and the `Home` and `End` buttons to jump to the first
or last slide.

On each chart, you can define the chart configuration and style with the same
objects as in `ipyvizzu`. However, you can not modify the underlying data
between the slides, only the data filter can be used.

!!! tip
    See
    [ipyvizzu - Filtering & adding new records chapter](https://ipyvizzu.vizzuhq.com/latest/tutorial/filter_add_new_records/)
    for more details on data filtering options.

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

## Story features

You can enable or disable chart features.

!!! tip
    See
    [ipyvizzu - Axes, title, tooltip chapter](https://ipyvizzu.vizzuhq.com/latest/tutorial/axes_title_tooltip/)
    for more details on chart features.

```python
story.set_feature("tooltip", True)
```

## Story events

You can add events.

!!! tip
    See
    [ipyvizzu - Events chapter](https://ipyvizzu.vizzuhq.com/latest/tutorial/events/)
    for more details on events.

```python
handler = "alert(JSON.stringify(event.data))"

story.add_event("click", handler)
```

## Play

After you create your story, you can play it with the `play` method

```python
story.play()
```

or with the `_repr_html_` method:

```python
story
```

!!! info
    If you run into any problems about playing your story, check
    [Environments chapter](../environments/index.md) for more details on
    available features.
