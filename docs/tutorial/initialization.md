# Initialization

## Import

From `ipyvizzu` import `Data`, `Config` and `Style` and from `ipyvizzu-story`
import `Story`, `Slide` and `Step`:

```python
from ipyvizzu import Data, Config, Style
from ipyvizzustory import Story, Slide, Step
```

## Constructor

You need to put the `data` object (from the [Data](./data.md) chapter) into the
`Story` constructor, you can not change this later.

```python
story = Story(data=data)
```

Here you can also set the chart style used for the whole story as you can see in
our [example](../examples/us_budget.ipynb).

!!! tip
    See
    [ipyvizzu - Color palette & fonts chapter](https://ipyvizzu.vizzuhq.com/latest/tutorial/color_palette_fonts/)
    and
    [ipyvizzu - Chart layout chapter](https://ipyvizzu.vizzuhq.com/latest/tutorial/chart_layout/)
    for more details on style options.

```python
story = Story(data=data, style=Style({"title": {"fontSize": 50}}))
```

## Size

`ipyvizzu-story` tries to figure out the ideal `width` and `height` of the
story, but you can also set them manually with the `set_size` method.

```python
story.set_size(width="100%", height="400px")
```

## Story properties

### vizzu

`ipyvizzu-story` requires and downloads the
[Vizzu](https://github.com/vizzuhq/vizzu-lib) `JavaScript`/`C++`
[library](https://www.jsdelivr.com/package/npm/vizzu) from `jsDelivr CDN`, but
you can also use a different or self-hosted version of it.

!!! info
    The default value of `vizzu` property is `None`, because the default version
    of `Vizzu` is stored in the `vizzu-story` package.

```python
story.vizzu = "<url>/vizzu.min.js"
```

### vizzu_story

`ipyvizzu-story` requires and downloads the
[Vizzu](https://github.com/vizzuhq/vizzu-ext-js-story) `JavaScript`
[package](https://www.jsdelivr.com/package/npm/vizzu-story) from `jsDelivr CDN`,
but you can also use a different or self-hosted version of it.

```python
story.vizzu_story = "<url>/vizzu-story.min.js"
```
