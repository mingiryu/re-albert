[OpenReview](https://openreview.net/forum?id=UkIQrHoru_J)

[PDF](https://openreview.net/pdf?id=UkIQrHoru_J)


## [RE] ALBERT: A Lite BERT for Self-supervised Learning of Language Representations

### Abstract

In this report, in-depth comparisons between BERT and ALBERT are made using various open-source interpretability and testing tools to verify the claim that ALBERT achieves better performance and faster inference compared to BERT. ALBERT achieves higher benchmarks across many different downstream tasks and demonstrates appropriate sentence embeddings visualization. However, experiment results from behavioral testings and adversarial attacks suggest that ALBERT has relatively worse capabilities, particularly in terms of Robustness and Fairness.

### Scope of Reproducibility

Lan et al.[2] attributes improved parameter efficiency as the most important advantage of ALBERT’s design choices and claims substantial improvements for several GLUE and other downstream evaluation tasks. Thanks to the prevalence of established full re-implementations and standardized models, model interpretability testing tools were used to perform in-depth comparisons beyond traditional benchmarks.

### Methodology

Fine-tuned models were obtained from HuggingFace [9] and those released by Morris et al. [4] were used to ensure consistency across models and experiments.  Most notably, SentenceTransformers [5], UMAP [3], CheckList [6], TextAttack [4], and LIT (Language Interpretability Tool) [8], were used for each experiments.

### Results

Based on several experiments in this report, ALBERT is qualitatively worse than BERT and has consistently slower inference speed. Therefore, this work does not support the broad conclusion that ALBERT outperforms BERT in terms of performance and inference speed in most cases.

### What was easy

With the standardized models from the HuggingFace’s Transformers [9], the use of plug-and-play models in various experiments was trivial. Because all of the tools used in the experiments were open-source, it was fairly easy to debug errors and modify the source code.

### What was difficult

Reviewing the literature and writing this reproducibility report alone took a significant amount of time, notwithstanding the absence of re-implementation or training.

### Communication with original authors

Initially, We chose not to contact the original authors because we did not intend to fully re-implement the original paper. Since communication with the original authors is curucial for successful reproducibility in natural language processing, we shared our report with the authors for further discussion and potential improvements.
