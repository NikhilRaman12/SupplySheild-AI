# SupplyShield AI

**AI-Native E-Commerce Supply Chain Risk Copilot & Control Tower**
*Built for the Snowflake CoCo CLI Hackathon.*

## Overview
SupplyShield transforms fragmented e-commerce supply-chain data into a canonical business ontology, governed semantic metrics, and deterministic supply-chain risk. It acts as an enterprise Copilot, instantly surfacing upstream supplier delays and quantifying downstream customer impact (Revenue at Risk).

By leveraging **Snowflake Cortex AI, Snowpark, and Streamlit**, SupplyShield AI replaces manual risk monitoring with conversational analytics and proactive intelligence.

## Hackathon Features
- **Built with Snowflake CoCo CLI:** Streamlined enterprise deployment and configuration (`snowflake.yml`).
- **Cortex-Powered Conversational Analytics:** Ask natural language questions about supply chain risk and get deterministic, trusted answers.
- **Real-World E-Commerce Data:** Integrates orders, shipments, products, and order items to build a realistic control tower.
- **Production-Ready UI:** A polished Streamlit dashboard displaying critical KPIs (SKUs at Risk, FCs Exposed, Revenue at Risk).

## Architecture
See [ARCHITECTURE.md](ARCHITECTURE.md) for a detailed look at the data flow from raw ingestion to the Cortex Agent.
For judge evaluation, please read [JUDGE_WALKTHROUGH.md](docs/JUDGE_WALKTHROUGH.md).

## Quick Start

### Local Streamlit Deployment
```bash
pip install -r requirements.txt
streamlit run app.py
```

### Snowflake CLI Deployment (CoCo CLI)
```bash
# Deploy the application to your Snowflake account
snow app run
```
