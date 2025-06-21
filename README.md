# ESG Growth Opportunity Identification Tool

This tool leverages AI to help organizations identify ESG growth opportunities by scanning public data, mining customer sentiment, and visualizing opportunity hotspots.

## Features

- **AI-enabled ESG demand scan** from public sources (news, reports, etc.).
- **Customer sentiment mining** using state-of-the-art NLP.
- **Value pool heatmap** to visualize growth pockets.
- **Automated web scraping** with scheduling.
- **Data anonymization** for privacy/security.
- **Interactive dashboard** with Streamlit.

## Setup

1. Clone the repo and navigate to the folder.
2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Run the main application:
    ```
    streamlit run dashboard/app.py
    ```

## Customization

- Add more data sources to `SCRAPE_URLS` in `config.py` or automate with web crawlers.
- Feed actual customer feedback, reviews, or social media data to the sentiment analyzer.

## Extending

- Plug in advanced LLMs for deeper ESG theme extraction.
- Use dashboards (e.g., Dash, Streamlit) for interactive visualizations.
- Integrate with internal datasets.
