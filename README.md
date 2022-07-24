<p align="center">
  <a href="https://github.com/vizzuhq/vizzu-lib">
    <img src="https://github.com/vizzuhq/vizzu-lib-doc/raw/main/docs/readme/infinite-60.gif" alt="Vizzu" />
  </a>
  <p align="center"><b>ipyvizzu - story</b> Extension</p>
  <p align="center">
    <a href="https://vizzuhq.github.io/ipyvizzu-story/examples/readme_complex/index.html">Example</a>
    · <a href="https://github.com/vizzuhq/ipyvizzu-story">Repository</a>
  </p>
</p>

[![PyPI version](https://badge.fury.io/py/ipyvizzu-story.svg)](https://badge.fury.io/py/ipyvizzu-story)
[![CI-CD](https://github.com/vizzuhq/ipyvizzu-story/actions/workflows/cicd.yml/badge.svg?branch=main)](https://github.com/vizzuhq/ipyvizzu-story/actions/workflows/cicd.yml)


# About The Extension

ipyvizzu-story is an extension of [ipyvizzu](https://github.com/vizzuhq/ipyvizzu) that enables users to create interactive presentations from the animated data visualizations built with ipyvizzu right within the data science notebook of their choice.
The extension provides a widget that contains the presentation and adds controls for navigating between slides - predefined stages within the story being presented.

# Installation

Visit our [wiki](https://github.com/vizzuhq/ipyvizzu-story/wiki/Tutorial#installation) site for more details about installation.

```sh
pip install ipyvizzu-story
```

# Usage

You can create the story below with the following code snippet.

Visit our [wiki](https://github.com/vizzuhq/ipyvizzu-story/wiki/Tutorial#usage) site for more details and a step-by-step tutorial into ipyvizzu-story or check out our example [gallery](https://github.com/vizzuhq/ipyvizzu-story/wiki/Examples).

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

# Contributing

We welcome contributions to the project, visit our contributing [guide](https://github.com/vizzuhq/ipyvizzu-story/blob/main/CONTRIBUTING.md) for further info.

# Contact

* Join our Slack if you have any questions or comments: [vizzu-community.slack.com](https://join.slack.com/t/vizzu-community/shared_invite/zt-w2nqhq44-2CCWL4o7qn2Ns1EFSf9kEg)
* Drop us a line at hello@vizzuhq.com
* Follow us on Twitter: [VizzuHQ](https://twitter.com/VizzuHQ)

# License

Copyright © 2022 [Vizzu Kft.](https://vizzuhq.com).

Released under the [Apache 2.0 License](https://github.com/vizzuhq/vizzu-lib/blob/main/LICENSE).
