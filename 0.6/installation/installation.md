# Installation

`ipyvizzu-story` requires the [ipyvizzu](https://pypi.org/project/ipyvizzu)
package.

!!! info
    `ipyvizzu-story` requires and downloads the
    [Vizzu](https://github.com/vizzuhq/vizzu-lib) `JavaScript`/`C++`
    [library](https://www.jsdelivr.com/package/npm/vizzu) and the
    [vizzu-story](https://github.com/vizzuhq/vizzu-ext-js-story) `JavaScript`
    [package](https://www.jsdelivr.com/package/npm/vizzu-story) from
    `jsDelivr CDN`, but you can also use a different or self-hosted version of
    them. Check
    [Initialization chapter](./tutorial/initialization.md#story-properties) for
    more details.

## pypi

Run the following command to install `ipyvizzu-story` from
[pypi](https://pypi.org/project/ipyvizzu-story/)

```sh
pip install ipyvizzu-story
```

and this is how to upgrade it.

```sh
pip install -U ipyvizzu-story
```

You can use `ipyvizzu-story` in `Jupyter/IPython`, `Streamlit`, `Panel` or
`Python` (see [Environments chapter](environments/index.md) for more details).

### Jupyter/IPython

You can install `ipyvizzu-story` in your notebook without using the command line
by entering the following code into a cell.

```
!pip install ipyvizzu-story
```

If you want to install `Jupyter/IPython` as a dependency, install
`ipyvizzu-story` with the following command.

```sh
pip install ipyvizzu-story[jupyter]
```

### Streamlit

If you want to install `Streamlit` as a dependency, install `ipyvizzu-story`
with the following command.

```sh
pip install ipyvizzu-story[streamlit]
```

### Panel

If you want to install `Panel` as a dependency, install `ipyvizzu-story` with
the following command.

```sh
pip install ipyvizzu-story[panel]
```

## conda / mamba

Installing `ipyvizzu-story` from `conda-forge` can be achieved by adding
`conda-forge` to your channels with:

```sh
conda config --add channels conda-forge
conda config --set channel_priority strict
```

Once the `conda-forge` channel has been enabled, run the following command to
install `ipyvizzu-story` from
[conda](https://anaconda.org/conda-forge/ipyvizzu-story/)

```sh
conda install ipyvizzu-story

# or with mamba:

mamba install ipyvizzu-story
```

and this is how to upgrade it.

```sh
conda update ipyvizzu-story

# or with mamba:

mamba update ipyvizzu-story
```
