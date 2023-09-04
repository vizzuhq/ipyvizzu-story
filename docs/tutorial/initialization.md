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

You can also set the aspect ratio of the story. This will not affect the aspect
ratio in full-screen view as that will be determined by the actual screen's
dimensions.

```python
story.set_size(aspect_ratio=16 / 9)
```

If you use the `aspect_ratio`, the `width` or `height` parameters can also be
set, but in some environments, if you want to use the `play` method, it will
only accept pixels.

```python
story.set_size(width="800px", aspect_ratio=16 / 9)
```

## Story properties

### Analytics

The usage statistics feature in `ipyvizzu-story` allows aggregate usage data
collection using [Plausible](https://plausible.io/)'s algorithm. Enabling this
feature helps us follow the progress and overall trends of our library, allowing
us to focus our resources effectively and better serve our users.

We do not track, collect, or store any personal data or personally identifiable
information. All data is isolated to a single day, a single site, and a single
device only.

Usage statistics feature is optional, and by default, it is enabled (default
value: `True`). Users can choose to opt-out if they prefer not to participate in
data collection. Please note that even when this feature is enabled, publishing
anything made with `ipyvizzu-story` remains GDPR compatible.

To disable usage statistics feature, set `analytics` property to `False`.

```python
story.analytics = False
```

### Vizzu

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

### Vizzu-Story

`ipyvizzu-story` requires and downloads the
[Vizzu-Story](https://github.com/vizzuhq/vizzu-ext-js-story) `JavaScript`
[package](https://www.jsdelivr.com/package/npm/vizzu-story) from `jsDelivr CDN`,
but you can also use a different or self-hosted version of it.

```python
story.vizzu_story = "<url>/vizzu-story.min.js"
```

### Start slide

You can start the story on a specific slide via the `start_slide` property. You
can also use negative numbers, where `-1` means the last slide.

```python
story.start_slide = 3
```
