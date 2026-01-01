# artifinder 📚

`artifinder` is a `rachis` (formerly Q2F) utility designed to help you find and identify `[rachis](https://news.rachis.org/en/latest/2025-10-23-q2f-transition.html)` (formerly Q2F) [`Results`](https://use.qiime2.org/en/latest/back-matter/glossary.html#term-result) that are relevant to your analysis from a directory that might contain a mix of relevant and irrelevant `Result` files.
This can be useful when:

 1. you're getting to the end of a complex analysis and need to compile relevant [`Artifacts`](https://use.qiime2.org/en/latest/back-matter/glossary.html#term-artifact) for archival; or
 2. you're picking up an analysis that someone left off on, and you're struggling to make sense of which files were used for what; or
 3. you're picking up an analysis that you left off on a while ago, and you're can't remember which files were used for what.

## Basic usage

If you have the `tests/data` directory from this repository in your current working directory, you can use `artifinder` as follows.

```
$ artifinder prov tests/data/ tests/data/scatter_plot.qzv

`artifinder` version: ...

Scanning search path for .qza and .qzv files...
Found 4 `Results` in search directory.

Parsing target's provenance...
Found 6 `Results` in target's provenance (not including target).
 * 2 were found in the search directory.
 * 4 were not found in the search directory.

Target `Result`:
af47db9d-bfd7-4a72-a266-cfa8defff718	Visualization	/Users/jgcap/4-git-repos/gregcaporaso/artifinder/tests/data/scatter_plot.qzv

Found `Results`:
7095b508-4ae3-4791-9e7d-7ca4f5a50279	FeatureData[Sequence]	/Users/jgcap/4-git-repos/gregcaporaso/artifinder/tests/data/asv-seqs-ms2.qza
76793c84-899d-4540-8352-1a0d2255500c	FeatureTable[Frequency]	/Users/jgcap/4-git-repos/gregcaporaso/artifinder/tests/data/asv-table-ms2.qza

`Results` not found:
d27a741c-f7e9-48af-ad8a-a479bd89ec9e	SampleData[PairedEndSequencesWithQuality]
1a4485df-2031-4e98-aecf-193ee8497f80	SampleData[PairedEndSequencesWithQuality]
83f7bac5-325f-4268-8754-c816ac46c97f	FeatureData[Sequence]
79a34b19-4a78-49ec-9771-b62ca20adafd	FeatureTable[Frequency]
```

Have fun! 😎

## About

`artifinder` is developed by [Greg Caporaso](https://caplab.dev).
