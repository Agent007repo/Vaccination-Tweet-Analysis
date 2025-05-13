# Vaccination Tweet Analysis

## Project Overview

This project applies advanced social media analytics techniques to analyze vaccination-related tweets, extracting meaningful insights about public sentiment, information flow, and discourse evolution. By leveraging computational methods, we explored how social dynamics and information networks shaped public perception of vaccination during the COVID-19 vaccine rollout period.

## Project Objectives & Achievements

### 1. Sentiment Dynamics Mapping

**Goal:** Track how public opinion evolved in response to key events such as Emergency Use Authorization (EUA) announcements.

**Implementation:** 
- Applied VADER sentiment analysis to quantify emotional responses in vaccination tweets
- Tracked sentiment trends over time, correlated with major vaccine events
- Created temporal visualizations showing sentiment evolution

**Findings:**
- Overall sentiment distribution showed a mix of positive, neutral, and negative reactions
- Temporal patterns reflected public response to major vaccination announcements
- Visualization clearly demonstrated sentiment shifts over the study period

### 2. Influencer and Community Identification

**Goal:** Identify influential users and detect community structures within the vaccination discourse network.

**Implementation:**
- Constructed social network graphs from mentions and interactions
- Applied centrality measures (PageRank, degree, betweenness) to identify influencers
- Used Louvain community detection to identify echo chambers

**Findings:**
- High network modularity (0.9174) indicating distinct communities in vaccination discourse
- Key influencers identified included pharmaceutical companies like Pfizer, healthcare professionals, and political figures
- Top influencers by PageRank included "pfizer" (0.0109), "Simon Hodes" (0.0102), and various healthcare voices

### 3. Information Propagation Analysis

**Goal:** Understand how vaccine information spreads through social networks.

**Implementation:**
- Built cascade models to track information flow
- Analyzed cascade size and duration
- Identified patterns in information spread

**Findings:**
- Information propagation analysis revealed how content dispersed through the network
- Cascade patterns showed variance in spread size and velocity
- Implementation of propagation_metrics function allowed quantification of influence reach

### 4. Topic Cluster Detection

**Goal:** Identify and characterize prominent narratives in vaccination discussions.

**Implementation:**
- Applied topic modeling techniques
- Performed keyword extraction and term frequency analysis
- Created visualizations to represent topic distributions

**Findings:**
- Topics clustered around vaccine safety, distribution logistics, efficacy, and policy
- Implementation of visualization techniques to represent topic distribution
- Identification of key terms and phrases defining each topic

### 5. Causal Impact Measurement

**Goal:** Measure the impact of specific events (e.g., Moderna EUA approval) on public sentiment.

**Implementation:**
- Conducted difference-in-differences analysis
- Implemented before-after comparisons with statistical controls
- Developed visualization for sentiment shifts around key dates

**Findings:**
- Analysis framework successfully implemented to detect sentiment shifts
- Implementation of prepare_did_data and run_did_regression functions
- Visualization capabilities for pre/post event sentiment comparison

## Methodology

The project employed a comprehensive analytical approach:

1. **Data Processing and Handling**
   - Leveraged Pandas for data manipulation of vaccination-related tweets
   - Implemented efficient cleaning and preprocessing for text analysis
   - Created structured pipeline for data preparation

2. **Network and Graph Analytics**
   - Constructed interaction graphs with nodes representing users and edges representing interactions
   - Applied centrality measures (PageRank, betweenness, degree) to identify key influencers
   - Conducted community detection using Louvain method identifying distinct conversation clusters

3. **Natural Language Processing**
   - Performed sentiment analysis using VADER
   - Implemented topic modeling to identify key discussion themes
   - Analyzed temporal patterns in sentiment and topic evolution

4. **Causal Inference**
   - Measured the impact of specific events (e.g., Moderna EUA approval) on sentiment
   - Applied difference-in-differences approach for causal estimation
   - Implemented statistical controls for confounding factors

5. **Advanced Visualization**
   - Created interactive network visualizations with PyVis
   - Developed temporal visualizations for sentiment tracking
   - Built integrated dashboard for holistic data exploration

## Key Insights

1. **Community Structure:** The network analysis revealed distinct communities in the vaccination discourse, with modularity score of 0.9174 indicating strong community separation.

2. **Influencer Identification:** The PageRank algorithm successfully identified key influencers, with pharmaceutical companies, healthcare professionals, and political figures emerging as central nodes.

3. **Sentiment Patterns:** Sentiment analysis revealed temporal patterns in public response to vaccination events, with the ability to track shifts around key announcements.

4. **Information Flow:** The cascade analysis framework demonstrated the spread patterns of vaccine information through the network.

5. **Topic Evolution:** The topic modeling implementation successfully identified major discussion themes within the vaccination discourse.

## Technological Implementation

The analysis utilized a comprehensive Python-based data science stack:
- pandas for data handling
- NLTK/VADER for sentiment analysis
- NetworkX for network construction and analysis
- Community module for community detection
- Topic modeling for thematic analysis
- Matplotlib/Plotly for visualization
- ipywidgets for interactive dashboard development

## Conclusions

This project demonstrates the implementation of a comprehensive computational approach to social media analysis focused on vaccination discourse. The multi-faceted methodology successfully combines sentiment analysis, network science, topic modeling, and causal inference to generate insights into how social media shapes public health perceptions.

The analytical framework provides a foundation for understanding the complex interplay between sentiment, network structure, information flow, and discourse topics in online conversations about critical public health issues. 