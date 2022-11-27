# Installation

`ipyvizzu-story` requires [ipyvizzu](https://pypi.org/project/ipyvizzu) package.

## pypi

Run the following command to install `ipyvizzu-story` from [pypi](https://pypi.org/project/ipyvizzu-story/)

```sh
pip install ipyvizzu-story
```

or the command below to upgrade it.

```sh
pip install -U ipyvizzu-story
```

You can use `ipyvizzu-story` in `Jupyter/IPython`, `Streamlit`, `Panel` or `Python` (see [Environments chapter](environments/index.md) of our documentation site).

### Jupyter/IPython

You can easily install `ipyvizzu-story` in your notebook without using the command line
if you place the following code into a cell.

```
!pip install ipyvizzu-story
```

If you want to install `Jupyter/IPython` as a dependency, install `ipyvizzu-story` with the following command.

```sh
pip install ipyvizzu-story[jupyter]
```

### Streamlit

If you want to install `Streamlit` as a dependency, install `ipyvizzu-story` with the following command.

```sh
pip install ipyvizzu-story[streamlit]
```

### Panel

If you want to install `Panel` as a dependency, install `ipyvizzu-story` with the following command.

```sh
pip install ipyvizzu-story[panel]
```

## conda / mamba

Installing `ipyvizzu-story` from `conda-forge` can be achieved by adding `conda-forge` to your channels with:

```
conda config --add channels conda-forge
conda config --set channel_priority strict
```

Once the `conda-forge` channel has been enabled,
run the following command to install `ipyvizzu-story` from [conda](https://anaconda.org/conda-forge/ipyvizzu-story/)

```
conda install ipyvizzu-story

# or with mamba:

mamba install ipyvizzu-story
```

or the command below to upgrade it.

```
conda update ipyvizzu-story

# or with mamba:

mamba update ipyvizzu-story
```
