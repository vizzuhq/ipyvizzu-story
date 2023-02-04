<p align="center">
  <a href="https://ipyvizzu-story.vizzuhq.com">
    <img src="https://ipyvizzu-story.vizzuhq.com/assets/ipyvizzu-story.gif" alt="ipyvizzu-story" />
  </a>
  <p align="center"><b>ipyvizzu-story</b> - Build, present and share animated data stories in Jupyter Notebook and similar environments</p>
  <p align="center">
    <a href="https://ipyvizzu-story.vizzuhq.com">Documentation</a>
    · <a href="https://ipyvizzu-story.vizzuhq.com/examples/index.html">Examples</a>
    · <a href="https://ipyvizzu-story.vizzuhq.com/reference/ipyvizzustory/index.html">Code reference</a>
    · <a href="https://github.com/vizzuhq/ipyvizzu-story">Repository</a>
  </p>
</p>

[![PyPI version](https://badge.fury.io/py/ipyvizzu-story.svg)](https://badge.fury.io/py/ipyvizzu-story)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/ipyvizzu-story.svg)](https://anaconda.org/conda-forge/ipyvizzu-story)
[![CI-CD](https://github.com/vizzuhq/ipyvizzu-story/actions/workflows/cicd.yml/badge.svg?branch=main)](https://github.com/vizzuhq/ipyvizzu-story/actions/workflows/cicd.yml)

# ipyvizzu-story

## About The Extension

ipyvizzu-story is an extension of the animated charting tool
[ipyvizzu](https://github.com/vizzuhq/ipyvizzu) that enables users to create and
present interactive data presentations within the data science notebook of their
choice and to share them as an HTML file. The extension provides a widget that
contains the presentation and adds controls for navigating between slides -
predefined stages within the story being presented. Navigation also works with
keyboard shortcuts - arrow keys, PgUp, PgDn, Home, End - and you can also use a
clicker to switch between the slides. .

## Installation

```sh
pip install ipyvizzu-story
```

Visit
[Installation chapter](https://ipyvizzu-story.vizzuhq.com/installation.html) for
more options and details.

## Usage

You can check the code behind the animation on the top of the page in
[HTML](https://ipyvizzu-story.vizzuhq.com/examples/complex/complex.html) or
download it as an
[ipynb file](https://ipyvizzu-story.vizzuhq.com/examples/demo/ipyvizzu-story_example.ipynb).

You can create the story below with the following code snippet.

<p align="center">
  <img src="https://ipyvizzu-story.vizzuhq.com/assets/readme-example.gif" alt="ipyvizzu-story" />
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

Visit our [Documentation site](https://ipyvizzu-story.vizzuhq.com/index.html)
for more details and a step-by-step tutorial into ipyvizzu-story or check out
our [Example gallery](https://ipyvizzu-story.vizzuhq.com/examples/index.html).

## Environments

ipyvizzu-story can be used in a wide variety of environments, visit
[Environments chapter](https://ipyvizzu-story.vizzuhq.com/environments/index.html)
for more details.

- Notebooks
  - [Jupyter Notebook](https://ipyvizzu-story.vizzuhq.com/environments/notebook/jupyternotebook.html)
  - [Colab](https://ipyvizzu-story.vizzuhq.com/environments/notebook/colab.html)
  - [Databricks](https://ipyvizzu-story.vizzuhq.com/environments/notebook/databricks.html)
  - [DataCamp](https://ipyvizzu-story.vizzuhq.com/environments/notebook/datacamp.html)
  - [Deepnote](https://ipyvizzu-story.vizzuhq.com/environments/notebook/deepnote.html)
  - [JupyterLab](https://ipyvizzu-story.vizzuhq.com/environments/notebook/jupyterlab.html)
  - [JupyterLite](https://ipyvizzu-story.vizzuhq.com/environments/notebook/jupyterlite.html)
  - [Kaggle](https://ipyvizzu-story.vizzuhq.com/environments/notebook/kaggle.html)
  - [Noteable](https://ipyvizzu-story.vizzuhq.com/environments/notebook/noteable.html)
- App platforms
  - [Streamlit](https://ipyvizzu-story.vizzuhq.com/environments/platform/streamlit.html)
  - [Flask](https://ipyvizzu-story.vizzuhq.com/environments/platform/flask.html)
  - [Panel](https://ipyvizzu-story.vizzuhq.com/environments/platform/panel.html)
  - [Mercury/mljar](https://ipyvizzu-story.vizzuhq.com/environments/platform/mercury.html)
  - [Voilà](https://ipyvizzu-story.vizzuhq.com/environments/platform/voila.html)
- BI tools
  - [Mode](https://ipyvizzu-story.vizzuhq.com/environments/bi/mode.html)
- IDEs
  - [PyCharm](https://ipyvizzu-story.vizzuhq.com/environments/ide/pycharm.html)
  - [VSCode Python](https://ipyvizzu-story.vizzuhq.com/environments/ide/vscode.html)
- [Python](https://ipyvizzu-story.vizzuhq.com/environments/python.html)

## Contributing

We welcome contributions to the project, visit our
[Contributing guide](https://ipyvizzu-story.vizzuhq.com/CONTRIBUTING.html) for
further info.

## Contact

- Join our Slack if you have any questions or comments:
  [vizzu-community.slack.com](https://join.slack.com/t/vizzu-community/shared_invite/zt-w2nqhq44-2CCWL4o7qn2Ns1EFSf9kEg)
- Drop us a line at hello@vizzuhq.com
- Follow us on Twitter: [VizzuHQ](https://twitter.com/VizzuHQ)

## License

Copyright © 2022-2023 [Vizzu](https://vizzuhq.com).

Released under the
[Apache 2.0 License](https://ipyvizzu-story.vizzuhq.com/LICENSE.html).
