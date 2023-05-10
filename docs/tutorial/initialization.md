# Initialization

## Import

From `ipyvizzu` import `Data`, `Config` and `Style` and from `ipyvizzu-story`
import `Story`, `Slide` and `Step`:

```python
from ipyvizzu import Data, Config, Style
from ipyvizzustory import Story, Slide, Step
```

## Constructor

You need to put the `Data` object (described in the [Data](./data.md) chapter)
into the `Story` constructor. You can not alter the data later but the data
being shown can be filtered at each step.

```python
story = Story(data=data)
```

You can set the style used initally for the story as you can see in this
[example](../examples/usbudget.md), and you can alter the style at each step
within the story.

```python
story = Story(data=data, style=Style({"title": {"fontSize": 50}}))
```

!!! tip
    Check
    [ipyvizzu - Color palette & fonts chapter](https://ipyvizzu.vizzuhq.com/latest/tutorial/color_palette_fonts/)
    and
    [ipyvizzu - Chart layout chapter](https://ipyvizzu.vizzuhq.com/latest/tutorial/chart_layout/)
    for more details on the available styling options.

## Size

`ipyvizzu-story` tries to apply the ideal `width` and `height` for the story,
but you can also set them manually with the `set_size` method.

```python
story.set_size(width="100%", height="400px")
```

## Story properties

### vizzu

`ipyvizzu-story` requires and downloads the
[Vizzu](https://github.com/vizzuhq/vizzu-lib) `JavaScript`/`C++`
[library](https://www.jsdelivr.com/package/npm/vizzu) from `jsDelivr CDN`, but
you can also use a different or self-hosted version of it.

```python
story.vizzu = "<url>/vizzu.min.js"
```

!!! info
    The default value of `vizzu` property is `None`, because the default version
    of `Vizzu` is stored in the `vizzu-story` package.

### vizzu_story

`ipyvizzu-story` requires and downloads the
[Vizzu-Story](https://github.com/vizzuhq/vizzu-ext-js-story) `JavaScript`
[package](https://www.jsdelivr.com/package/npm/vizzu-story) from `jsDelivr CDN`,
but you can also use a different or self-hosted version of it.

```python
story.vizzu_story = "<url>/vizzu-story.min.js"
```

### start_slide

You can start the story on a specific slide via the `start_slide` property.

```python
story.start_slide = 3
```
