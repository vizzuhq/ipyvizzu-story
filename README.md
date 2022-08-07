<p align="center">
  <a href="https://github.com/vizzuhq/vizzu-lib">
    <img src="https://github.com/vizzuhq/ipyvizzu-story/raw/main/docs/examples/demo/ipyvizzu-story_example.gif" alt="ipyvizzu-story demo" />
  </a>
  <p align="center"><b>ipyvizzu-story</b> Animated Chart Presentation in Jupyter Notebook</p>
  <p align="center">
    <a href="https://vizzuhq.github.io/ipyvizzu-story/docs/tutorial.html">Tutorial</a>
    · <a href="https://vizzuhq.github.io/ipyvizzu-story/docs/examples.html">Examples</a>
    · <a href="https://vizzuhq.github.io/ipyvizzu-story/ipyvizzustory.html#reference">Reference</a>
    · <a href="https://github.com/vizzuhq/ipyvizzu-story">Repository</a>
  </p>
</p>

[![PyPI version](https://badge.fury.io/py/ipyvizzu-story.svg)](https://badge.fury.io/py/ipyvizzu-story)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/ipyvizzu-story.svg)](https://anaconda.org/conda-forge/ipyvizzu-story)
[![CI-CD](https://github.com/vizzuhq/ipyvizzu-story/actions/workflows/cicd.yml/badge.svg?branch=main)](https://github.com/vizzuhq/ipyvizzu-story/actions/workflows/cicd.yml)

# About The Extension

ipyvizzu-story is an extension of [ipyvizzu](https://github.com/vizzuhq/ipyvizzu) that enables users to create interactive presentations within the data science notebook of their choice.
The extension provides a widget that contains the presentation and adds controls for navigating between slides - predefined stages within the story being presented. Navigation also works with keyboard shortcuts - arrow keys, PgUp, PgDn, Home, End - and you can also use a clicker to switch between the slides.
Since ipyvizzu-story's synthax is a bit different to ipyvizzu's, we suggest you to start from the [ipyvizzu repo](https://github.com/vizzuhq/ipyvizzu) if you're interested in building animated charts but not necessarly presenting them live or to share your presentation as an HTML file.

# Installation

```sh
pip install ipyvizzu-story
```
Visit our [documentation site](https://vizzuhq.github.io/ipyvizzu-story/docs/installation.html) site for more details about installation.

# Usage

You can check the code behind the animation on the top of the page in [HTML](https://vizzuhq.github.io/ipyvizzu-story/examples/demo/ipyvizzu-story_example.html) or download it as an [ipynb file](https://vizzuhq.github.io/ipyvizzu-story/examples/demo/ipyvizzu-story_example.ipynb)

You can create the story below with the following code snippet.

<p align="center">
  <img src="https://github.com/vizzuhq/vizzu-ext-js-story/raw/main/assets/readme-example.gif" alt="ipyvizzu" />
</p>

```python
from ipyvizzu import Data, Config
from ipyvizzustory import Story, Slide, Step

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

story.play()
```
Visit our [documentation site](https://vizzuhq.github.io/ipyvizzu-story/docs/tutorial.html#Usage) site for more details and a step-by-step tutorial into ipyvizzu-story or check out our example [gallery](https://vizzuhq.github.io/ipyvizzu-story/examples.html).

# Environment support

ipyvizzu-story can be used in a wide variety of environments, visit our [documentation site](https://vizzuhq.github.io/ipyvizzu-story/docs/environments.html) site for more details.

# Contributing

We welcome contributions to the project, visit our contributing [guide](https://github.com/vizzuhq/ipyvizzu-story/blob/main/CONTRIBUTING.md) for further info.

# Contact

* Join our Slack if you have any questions or comments: [vizzu-community.slack.com](https://join.slack.com/t/vizzu-community/shared_invite/zt-w2nqhq44-2CCWL4o7qn2Ns1EFSf9kEg)
* Drop us a line at hello@vizzuhq.com
* Follow us on Twitter: [VizzuHQ](https://twitter.com/VizzuHQ)

# License

Copyright © 2022 [Vizzu Kft.](https://vizzuhq.com).

Released under the [Apache 2.0 License](https://github.com/vizzuhq/vizzu-lib/blob/main/LICENSE).
