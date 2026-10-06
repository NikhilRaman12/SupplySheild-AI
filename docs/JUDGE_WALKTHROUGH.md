# Judge Walkthrough: SupplyShield AI

Welcome to **SupplyShield AI**, our submission for the **Snowflake CoCo CLI Hackathon**.

This walkthrough demonstrates how SupplyShield AI perfectly aligns with the core hackathon objectives: building a production-ready, enterprise-grade AI application using the Snowflake Data Cloud, Cortex AI, and the CoCo CLI.

## 🎯 The Enterprise Challenge (Hackathon Alignment)

SupplyShield AI addresses the **Supply Chain Ontology and Governed Conversational Analytics** challenge. 
It transforms a highly manual, reactive process (identifying upstream supplier delays and estimating downstream revenue impact) into an automated, AI-driven **Copilot and Control Tower**. By mapping real-world E-Commerce logistics data into a robust semantic ontology, we instantly surface risk signals and provide actionable, governed conversational analytics.

---

## 🏆 Key Evaluation Criteria Addressed

### 1. REAL-WORLD RELEVANCE (30%)
*   **The Problem:** E-commerce companies often realize a supplier delay has occurred only when customer SLAs are missed, leading to lost revenue and churn.
*   **The Solution:** SupplyShield AI bridges the gap between siloed ERP/WMS systems. It links a specific `Supplier -> Product -> Fulfillment Center (FC) -> Customer Order`, allowing supply chain managers to immediately quantify **Revenue at Risk**.
*   **Business Value:** Proactive risk mitigation, protected customer SLAs, and automated recommended actions (e.g., redistributing inventory).

### 2. TECHNICAL EXECUTION (40%)
*   **Snowflake CoCo CLI First:** The entire project structure, deployment, and configuration are managed via the Snowflake CLI (`snowflake.yml`), demonstrating modern developer workflows.
*   **Snowflake Cortex AI:** We leverage Cortex for natural language querying (the "Copilot" experience). Instead of complex SQL, users ask, *"Which suppliers are putting our Hyderabad FC at risk?"*
*   **Snowpark & SQL-First:** Data from raw CSVs (orders, shipments, products) is modeled using robust SQL schemas and Snowpark data frames for scalable entity resolution.
*   **Governed Metrics:** Core logic (like calculating `Revenue at Risk`) is centralized as a semantic layer, preventing hallucinations by Cortex AI.

### 3. SOLUTION COMPLETENESS (30%)
*   **End-to-End Architecture:** From raw data ingestion (`data_cortex/` CSVs) to a fully interactive Streamlit application.
*   **Production-Ready:** Includes a canonical ontology, data dictionary, architecture diagrams, and a beautifully designed, responsive UI.
*   **Actionability:** The application doesn't just show charts; it generates specific recommended actions based on deterministic data provenance.

---

## 🚀 How to Evaluate the Project

1. **Review the Architecture:** Check `ARCHITECTURE.md` to see the seamless flow from raw data to Cortex Agent.
2. **Examine the Code:** Open `app.py` to see the Streamlit integration and dynamic metric calculations based on real e-commerce data.
3. **Run the App:** Execute `streamlit run app.py` to experience the Control Tower firsthand. Note the dynamic KPIs and the "Conversational Analytics" Copilot interface powered by Cortex AI concepts.
4. **Inspect the Data Foundation:** Review `docs/data_cortex/` and `docs/DATA_QUALITY.md` to see how we handled real-world schema design and data validation.

Thank you for reviewing SupplyShield AI! We believe this represents the future of enterprise risk intelligence on Snowflake.
