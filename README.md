<p align="center">
  <a href="https://github.com/vizzuhq/vizzu-lib">
    <img src="https://github.com/vizzuhq/vizzu-lib-doc/raw/main/docs/readme/infinite-60.gif" alt="Vizzu" />
  </a>
  <p align="center"><b>ipyvizzu - story</b> Extension</p>
  <p align="center">
    <a href="https://vizzuhq.github.io/ipyvizzu-story/examples/readme_complex/index.html">Example</a>
    · <a href="https://github.com/vizzuhq/ipvizzu-story">Repository</a>
  </p>
</p>

[![CI-CD](https://github.com/vizzuhq/ipyvizzu-story/actions/workflows/cicd.yml/badge.svg?branch=main)](https://github.com/vizzuhq/ipyvizzu-story/actions/workflows/cicd.yml)


# About The Extension

ipyvizzu-story is an extension of [ipyvizzu](https://github.com/vizzuhq/ipyvizzu) that enables users to create interactive presentations from the animated data visualizations built with ipyizzu right within the data science notebook of their choice.
The extension provides a widget that contains the presentation and adds controls for navigating between slides - predefined stages within the story being presented.

# Installation

ipyvizzu-story requires [ipyvizzu](https://pypi.org/project/ipyvizzu) package.

```sh
pip install ipyvizzu-story
```

# Usage

![Readme example](https://github.com/vizzuhq/vizzu-ext-js-story/raw/main/assets/readme-example.gif)

Import `ipyvizzu` and `ipyvizzu-story`:

```python
from ipyvizzu import Data, Config
from ipyvizzustory import Story, Slide, Step
```

Add the underlying data for the data story. You can use the same data definition formats as in the ipyvizzu library, but you must add the entire data set for the whole story in the initial step, you can not change this later. See [ipyvizzu tutorial - Adding data](https://ipyvizzu.vizzuhq.com/tutorial/01_02_adding_data.html) for more details on data formats.

```python
data = Data()
data.add_series("Foo", ["Alice", "Bob", "Ted"])
data.add_series("Bar", [15, 32, 12])
data.add_series("Baz", [5, 3, 2])
```

Put the data object into the `Story` constructor. Here you can also set the `Story` objects `style` property to set the chart style used for the whole story.

```python
story = Story(data=data)
```

Create the data story by defining a sequence of slides. A slide can be a single chart corresponding to a single [chart.animate()](https://ipyvizzu.vizzuhq.com/tutorial/01_01_intro.html) call from ipvizzu. Or a slide can be a sequence of animation calls, in which case all of these animations will be played until the last one in the sequence, allowing for more complex transitions between slides. Navigation controls beneath the chart will navigate between the slides. You can use the PgUp, and PgDn buttons, left and right arrows to navigate between slides, and the Home and End buttons to jump to the first or last slide.

On each chart, you can define the chart configuration and style with the same objects as in ipyvizzu. However, you can not modify the underlying data between the slides, only the data filter used.

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

Then play the Story.

```python
story.play()
```

> [Check out a live example!](https://vizzuhq.github.io/ipyvizzu-story/examples/readme/index.html)

Or check out the source of this example to see a more complex use case:

> [Check out a live complex example!](https://vizzuhq.github.io/ipyvizzu-story/examples/readme_complex/index.html)

# Contributing

We welcome contributions to the project, visit our [contributing guide](https://github.com/vizzuhq/ipyvizzu-story/blob/main/CONTRIBUTING.md) for further info.

# Contact

* Join our Slack if you have any questions or comments: [vizzu-community.slack.com](https://join.slack.com/t/vizzu-community/shared_invite/zt-w2nqhq44-2CCWL4o7qn2Ns1EFSf9kEg)
* Drop us a line at hello@vizzuhq.com
* Follow us on twitter: [https://twitter.com/VizzuHQ](https://twitter.com/VizzuHQ)

# License

Copyright © 2022 [Vizzu Kft.](https://vizzuhq.com).

Released under the [Apache 2.0 License](https://github.com/vizzuhq/vizzu-lib/blob/main/LICENSE).
