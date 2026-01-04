# artifinder 📚

`artifinder` is a [`rachis` (formerly Q2F)](https://news.rachis.org/en/latest/2025-10-23-q2f-transition.html) utility designed to help you find and identify [`Artifacts`](https://use.qiime2.org/en/latest/back-matter/glossary.html#term-artifact) that are relevant to your analysis from a directory that might contain a mix of relevant and irrelevant `Artifacts` and [`Visualizations`](https://use.qiime2.org/en/latest/back-matter/glossary.html#term-visualization).
This can be useful when:

 1. you're getting to the end of a complex analysis and need to identify relevant [`Artifacts`](https://use.qiime2.org/en/latest/back-matter/glossary.html#term-artifact) to compile them for archival; or
 2. you're restarting an analysis that someone (you, or someone else) paused, and you're struggling to find specific files; or
 3. you want to run a variation on an analysis (for example, [ANCOMBC2](https://amplicon-docs.qiime2.org/en/stable/references/plugins/composition.html#q2-action-composition-ancombc2) with a different forumla) and you want to find and use the same inputs that you used for all previous variations on the analysis.

## Installation

`artifinder` depends only `rachis` >= 2025.10 and `click`.
If you have an existing `rachis` deployment, such as QIIME 2 2025.10, or MOSHPIT 2025.10, you can activate that environment and then install `artifinder` as follows:

```shell
pip install https://github.com/gregcaporaso/artifinder/archive/refs/heads/main.zip
```

If you don't have an existing deployment, you can install the tiny distribution with artifinder as follows:

```shell
conda env create -n artifinder --file https://raw.githubusercontent.com/gregcaporaso/artifinder/refs/heads/main/environment-files/artifinder-dev.yml
```

## Basic usage

If you have the `tests/data` directory from this repository (find it [here](https://github.com/gregcaporaso/artifinder/tree/main/tests/data)) in your current working directory, you can use `artifinder` as follows.

```
$ artifinder prov tests/data/ tests/data/scatter_plot.qzv

`artifinder` version: xxx

Scanning search path for .qza and .qzv files...
Found 4 `Results` in search directory.

Parsing target's provenance...
Found 6 `Results` in target's provenance (not including target).
 * 2 were found in the search directory.
 * 4 were not found in the search directory.

Target `Result`:
af47db9d-bfd7-4a72-a266-cfa8defff718	Visualization	./data/scatter_plot.qzv

Found `Results`:
7095b508-4ae3-4791-9e7d-7ca4f5a50279	FeatureData[Sequence]	./data/asv-seqs-ms2.qza
76793c84-899d-4540-8352-1a0d2255500c	FeatureTable[Frequency]	./data/asv-table-ms2.qza

`Results` not found:
d27a741c-f7e9-48af-ad8a-a479bd89ec9e	SampleData[PairedEndSequencesWithQuality]
1a4485df-2031-4e98-aecf-193ee8497f80	SampleData[PairedEndSequencesWithQuality]
83f7bac5-325f-4268-8754-c816ac46c97f	FeatureData[Sequence]
79a34b19-4a78-49ec-9771-b62ca20adafd	FeatureTable[Frequency]
```

Have fun! 😎

## About

`artifinder` is developed by [Greg Caporaso](https://caplab.dev).
