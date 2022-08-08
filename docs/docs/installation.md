# Installation

ipyvizzu-story requires [ipyvizzu](https://pypi.org/project/ipyvizzu) package.

## pypi

Run the following command to install ipyvizzu-story or the second command below to upgrade it.

```sh
pip install ipyvizzu-story
```

```sh
pip install -U ipyvizzu-story
```

You can use ipyvizzu-story in Jupyter, Streamlit or Python (see [Environments chapter](environments.md) of our documentation site).

If you want to install IPython as a dependency, install ipyvizzu-story with the following command.

```sh
pip install ipyvizzu-story[jupyter]
```

If you want to install Streamlit as a dependency, install ipyvizzu-story with the following command.

```sh
pip install ipyvizzu-story[streamlit]
```

## conda / mamba

Installing `ipyvizzu-story` from the `conda-forge` channel can be achieved by adding `conda-forge` to your channels with:

```
conda config --add channels conda-forge
conda config --set channel_priority strict
```

Once the `conda-forge` channel has been enabled, `ipyvizzu-story` can be installed with `conda`:

```
conda install ipyvizzu-story
```

or with `mamba`:

```
mamba install ipyvizzu-story
```
