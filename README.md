# Vaccination Tweet Analysis

Notebook-based social media analytics project studying COVID-19 vaccine discourse through sentiment analysis, network analysis, topic exploration, and event-impact framing.

## Project Maturity

Analytical notebook project. This repository is strongest as evidence of NLP, social network analysis, and public-discourse analytics. It should not be presented as a production misinformation monitoring platform without additional packaging, data governance, and deployment work.

## Main Artifact

- `Taha_Vaccination_tweet_analysis-2-fixed.ipynb`: notebook containing the analysis workflow and outputs.

If this was completed as a group or adapted class project, add a short provenance note in this README before using it as a hiring artifact.

## What The Project Demonstrates

- Text preprocessing for social media data.
- Sentiment analysis using VADER-style methods.
- Interaction graph construction.
- Influencer detection using centrality/PageRank-style metrics.
- Community detection using Louvain modularity.
- Topic and narrative exploration.
- Difference-in-differences style framing around vaccine authorization events.

## Key Result Signals

- Community modularity reported around 0.9174, suggesting strongly separated discourse clusters.
- Influencer analysis identifies central accounts and institutions in the conversation graph.
- Temporal sentiment analysis connects public response patterns to major vaccine rollout events.

## Local Setup

```bash
git clone https://github.com/Agent007repo/Vaccination-Tweet-Analysis.git
cd Vaccination-Tweet-Analysis
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook Taha_Vaccination_tweet_analysis-2-fixed.ipynb
```

## Known Limitations

- Social media datasets can include sampling bias, bot activity, deleted posts, and platform-specific distortions.
- Sentiment models can misread sarcasm, political language, and public-health terminology.
- Network centrality does not automatically imply real-world influence.
- Causal claims around public events require careful control groups, assumptions, and sensitivity checks.
- Public-health data work should include privacy and ethics notes before broader use.

## Recommended Next Improvements

- Rename the notebook to `vaccination_tweet_analysis.ipynb`.
- Add `requirements.txt`.
- Add exported network and sentiment plots under `outputs/`.
- Add a short ethics and data provenance section.
- Add a causal assumptions note for the event-impact analysis.

## Role Signal

This project supports analytics, NLP, social network analysis, and data storytelling roles. For ML/AI engineering roles, it should be treated as supporting evidence rather than a flagship engineering project.
