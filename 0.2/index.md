<p align="center">
  <a href="./">
    <img src="./assets/ipyvizzu-story.gif" alt="ipyvizzu-story" />
  </a>
  <p align="center"><b>ipyvizzu-story</b> - Build, present and share animated data stories in Jupyter Notebook and similar environments</p>
  <p align="center">
    <a href="./">Documentation</a>
    · <a href="./examples/">Examples</a>
    · <a href="https://github.com/vizzuhq/ipyvizzu-story">Repository</a>
  </p>
</p>

[![PyPI version](https://badge.fury.io/py/ipyvizzu-story.svg)](https://badge.fury.io/py/ipyvizzu-story)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/ipyvizzu-story.svg)](https://anaconda.org/conda-forge/ipyvizzu-story)
[![CI-CD](https://github.com/vizzuhq/ipyvizzu-story/actions/workflows/cicd.yml/badge.svg?branch=main)](https://github.com/vizzuhq/ipyvizzu-story/actions/workflows/cicd.yml)

# ipyvizzu-story

## About The Extension

`ipyvizzu-story` is an extension of the animated charting tool
[ipyvizzu](https://github.com/vizzuhq/ipyvizzu) that enables users to create and
present interactive data presentations within the data science notebook of their
choice and to share them as an `HTML` file. The extension provides a widget that
contains the presentation and adds controls for navigating between slides -
predefined stages within the story being presented. Navigation also works with
keyboard shortcuts - arrow keys, `PgUp`, `PgDn`, `Home`, `End` - and you can
also use a clicker to switch between the slides.

## Installation

```sh
pip install ipyvizzu-story
```

Visit
[Installation chapter](./installation)
for more options and details.

## Usage

You can check and download the code behind the animation on the top of the page
in our
[Example gallery](./examples/usbudget/).

You can create the story below with the following code snippet.

<p align="center">
  <img src="./assets/readme-example.gif" alt="ipyvizzu-story" />
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
story.add_slide(slide2)

story.play()
```

## Documentation

Visit our [Documentation site](./) for
more details and a step-by-step tutorial into `ipyvizzu-story` or check out our
[Example gallery](./examples/).

## Environments

`ipyvizzu-story` can be used in a wide variety of environments, visit
[Environments chapter](./environments/)
for more details.

- Notebooks
  - [Jupyter Notebook](./environments/notebook/jupyternotebook/)
  - [Colab](./environments/notebook/colab/)
  - [DataCamp](./environments/notebook/datacamp/)
  - [Deepnote](./environments/notebook/deepnote/)
  - [JupyterLab](./environments/notebook/jupyterlab/)
  - [JupyterLite](./environments/notebook/jupyterlite/)
  - [Kaggle](./environments/notebook/kaggle/)
  - [Noteable](./environments/notebook/noteable/)
- App platforms
  - [Streamlit](./environments/platform/streamlit/)
  - [Flask](./environments/platform/flask/)
  - [Mercury/mljar](./environments/platform/mercury/)
  - [Voilà](./environments/platform/voila/)
- BI tools
  - [Mode](./environments/bi/mode/)
- IDEs
  - [PyCharm](./environments/ide/pycharm/)
  - [VSCode Python](./environments/ide/vscode/)
- [Python](./environments/python/)

## Contributing

We welcome contributions to the project, visit our
[Contributing guide](./CONTRIBUTING) for
further info.

## Contact

- Join our Slack if you have any questions or comments:
  [vizzu-community.slack.com](https://join.slack.com/t/vizzu-community/shared_invite/zt-w2nqhq44-2CCWL4o7qn2Ns1EFSf9kEg)
- Drop us a line at hello@vizzuhq.com
- Follow us on Twitter: [VizzuHQ](https://twitter.com/VizzuHQ)

## License

Copyright © 2022-2023 [Vizzu Inc](https://vizzuhq.com).

Released under the
[Apache 2.0 License](./LICENSE).
