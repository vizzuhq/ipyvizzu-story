<p align="center">
  <a href="https://ipyvizzu-story.vizzuhq.com">
    <img src="https://ipyvizzu-story.vizzuhq.com/assets/ipyvizzu-story.gif" alt="ipyvizzu-story" />
  </a>
  <p align="center"><b>ipyvizzu-story</b> Animated Chart Presentation in Jupyter Notebook and in many other environments</p>
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

ipyvizzu-story is an extension of
[ipyvizzu](https://github.com/vizzuhq/ipyvizzu) that enables users to create
interactive presentations within the data science notebook of their choice. The
extension provides a widget that contains the presentation and adds controls for
navigating between slides - predefined stages within the story being presented.
Navigation also works with keyboard shortcuts - arrow keys, PgUp, PgDn, Home,
End - and you can also use a clicker to switch between the slides. Since
ipyvizzu-story's synthax is a bit different to ipyvizzu's, we suggest you to
start from the [ipyvizzu repo](https://github.com/vizzuhq/ipyvizzu) if you're
interested in building animated charts but not necessarly presenting them live
or to share your presentation as an HTML file.

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
  - [Jupyter Notebook](https://ipyvizzu-story.vizzuhq.com/environments/jupyter/jupyternotebook.html)
  - [Colab](https://ipyvizzu-story.vizzuhq.com/environments/jupyter/colab.html)
    [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1VnmuPHm7Ynk6aZiWN0QcnIqGGW5ODnFf?usp=sharing)
  - [Databricks](https://ipyvizzu-story.vizzuhq.com/environments/jupyter/databricks.html)
  - [DataCamp](https://ipyvizzu-story.vizzuhq.com/environments/jupyter/datacamp.html)
  - [Deepnote](https://ipyvizzu-story.vizzuhq.com/environments/jupyter/deepnote.html)
    [![View in Deepnote](https://deepnote.com/static/buttons/view-in-deepnote.svg)](https://deepnote.com/workspace/david-andras-vegh-bc03-79fd3a98-abaf-40c0-8b52-9f3e438a73fc/project/ipyvizzu-story-demo-11b5d5eb-7f68-44c4-b1a7-347fde1a8f64)
  - [JupyterLab](https://ipyvizzu-story.vizzuhq.com/environments/jupyter/jupyterlab.html)
  - [JupyterLite](https://ipyvizzu-story.vizzuhq.com/environments/jupyter/jupyterlite.html)
  - [Kaggle](https://ipyvizzu-story.vizzuhq.com/environments/jupyter/kaggle.html)
    [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://www.kaggle.com/dvidandrsvgh/ipyvizzu-story-demo)
  - [Noteable](https://ipyvizzu-story.vizzuhq.com/environments/jupyter/noteable.html)
- App platforms
  - [Streamlit](https://ipyvizzu-story.vizzuhq.com/environments/streamlit.html)
  - [Panel](https://ipyvizzu-story.vizzuhq.com/environments/panel.html)
  - [Mercury/mljar](https://ipyvizzu-story.vizzuhq.com/environments/jupyter/mercury.html)
  - [Voilà](https://ipyvizzu-story.vizzuhq.com/environments/jupyter/voila.html)
- BI tools
  - [Mode](https://ipyvizzu-story.vizzuhq.com/environments/jupyter/mode.html)
- IDEs
  - [PyCharm](https://ipyvizzu-story.vizzuhq.com/environments/jupyter/pycharm.html)
  - [VSCode Python](https://ipyvizzu-story.vizzuhq.com/environments/jupyter/vscode.html)
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
