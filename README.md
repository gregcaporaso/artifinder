# artifinder

`artifinder` is designed to help you identify [Q2 `Results`](https://use.qiime2.org/en/latest/back-matter/glossary.html#term-result) that are relevant to your analysis from a directory that might contain a mix of relevant and irrelevant `Result` files.
This can be useful when you're getting to the end of a complex analysis and need to compile relevant [QIIME 2 `Artifacts`](https://use.qiime2.org/en/latest/back-matter/glossary.html#term-artifact) for inclusion with a manuscript.

For example, given a **target** `Result` (`ss-usage/Serial/hits-table.qzv` in the example that follows) and a search directory (`ss-usage`), `artifinder` provides you with absolute file paths to all of the QIIME 2 `Artifacts` that were used in the creation of the target.
If an `Artifact` that was used is not found in the search path, that information is reported.

```shell
$ artifinder ss-usage/Serial/hits-table.qzv ss-usage

Target `Result` UUID(s):
 * 4e5df73c-a24e-4f02-b0a3-6ad1995fe5a7

Predecessor `Results`:
 * 4e5df73c-a24e-4f02-b0a3-6ad1995fe5a7
  * Visualization
  * /Users/jgc/temp/uq2/ss-usage/Serial/hits-table.qzv
 * 3d410727-d6cc-4d97-bbbf-473954a25e4f
  * FeatureData[Sequence]
  * /Users/jgc/temp/uq2/ss-usage/Serial/query-seqs.qza
 * 572a62ce-8ae4-442e-bfbf-e1e177ea767a
  * FeatureData[Sequence]
  * Result not found in search path.
```

`artifinder` is untested at this point, aside from applications to some local data - it's just a simple utility script, after all.
[Let me know](https://github.com/gregcaporaso/artifinder/issues) if it's not working for you or if you think it's cool and have ideas for new functionality.

## Installation and usage instructions

The following instructions will enable you to install the most recent *development* version of `artifinder`.

### Install Prerequisites

[Miniconda](https://conda.io/miniconda.html) provides the `conda` environment and package manager, and is currently the only supported way to install QIIME 2.
Follow the instructions for downloading and installing Miniconda.

After installing Miniconda and opening a new terminal, make sure you're running the latest version of `conda`:

```bash
conda update conda
```

###  Install development version of `artifinder`

If you're in a conda environment, deactivate it by running `conda deactivate`.

Then, run:

```shell
conda env create -n artifinder --file https://raw.githubusercontent.com/gregcaporaso/artifinder/refs/heads/main/environments/artifinder-qiime2-tiny-2024.10.yml
```

After this completes, activate the new environment you created by running:

```shell
conda activate artifinder
```

### Usage

You should then be able to use `artifinder` as follows:

```shell
$ artifinder <target-result> <search-directory>
```

For example:

```shell
$ artifinder hits-table.qzv ss-usage
```

Have fun! 😎

## About

`artifinder` is a Research Data Management (RDM) tool [developed](https://develop.qiime2.org) by Greg Caporaso (greg.caporaso@nau.edu).
The `artifinder` Python package was [created from a template](https://develop.qiime2.org/en/latest/plugins/tutorials/create-from-template.html).
