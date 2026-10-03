# Vaccination Tweet Analysis

An exploratory notebook combining VADER and transformer sentiment, BERTopic and LDA topic analysis, mention-network centrality and Louvain communities, geographic plots, and an interactive sentiment dashboard.

## Run

Use Python 3.11+ and a clean environment. Install `requirements.txt`. Set `VACCINATION_TWEETS_CSV` to the vaccination-tweet CSV, or place the expected dataset in the repository root as specified by the notebook. Run `Taha_Vaccination_tweet_analysis-2-fixed.ipynb` in Jupyter from this directory.

```bash
pip install -r requirements.txt
jupyter notebook Taha_Vaccination_tweet_analysis-2-fixed.ipynb
```

NLTK lexicons/tokenizers and Hugging Face model weights require an initial download. TLS verification remains enabled. Downloaded models and third-party packages may require additional compatible dependencies; a clean installation and full dataset run have not been reproduced during this review.

The analysis normalizes hashtag representations, preserves unique row indices after parallel cleaning, supports BERTopic's different probability shapes, truncates long transformer inputs, and uses a fixed sampling seed. Plotted sentiment shares are percentages. Edge frequency represents mention strength; weighted betweenness uses inverse frequency as distance.

## Scope of conclusions

Mention graphs describe observed mentions. They do not reconstruct tweet-level retweet cascades, information exposure, or causal propagation. Display names and mention handles can represent different identifiers, so identity resolution is needed before attributing influence to individuals. Community separation does not demonstrate an echo chamber.

The event comparison and dashboard regression are exploratory associations. No validated untreated comparison group or parallel-trends check supports a causal effect claim. The earlier README's cascade functions and causal-analysis function names were absent from the implementation and have been removed. Historical modularity, PageRank, and sentiment claims are unverified and must be recomputed. Notebook outputs are cleared.

```bash
python -m unittest discover -s tests -p test_regressions.py -v
```

Three regression tests check hashtag normalization, graph-distance semantics, and transformer truncation. Model downloads, topic fitting, dashboard rendering, and real-data results remain unverified.
