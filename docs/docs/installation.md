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

You can use `ipyvizzu-story` in `Jupyter`, `Streamlit`, `Panel` or `Python` (see [Environments chapter](environments.md) of our documentation site).

If you want to install `IPython` as a dependency, install `ipyvizzu-story` with the following command.

```sh
pip install ipyvizzu-story[jupyter]
```

If you want to install `Streamlit` as a dependency, install `ipyvizzu-story` with the following command.

```sh
pip install ipyvizzu-story[streamlit]
```

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
