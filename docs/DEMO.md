# Demo Script

## The Killer Question
**User:** "Which supplier disruptions could cause customer-facing fulfillment failures, and what should we act on first?"

**Agent Response Flow:**
1.  **Answer**: Identifies top suppliers (e.g., "Nova Components").
2.  **Why It Matters**: Explains that delays from these suppliers are depleting safety stock below critical thresholds.
3.  **Supply-Chain Chain**: `Nova Components -> SKU-204 -> Hyderabad FC -> Inbound Delay (4 days) -> 150 Orders Exposed`.
4.  **Customer Impact**: "₹450,000 Revenue at Risk, 120 unique customers affected."
5.  **Recommended Action**: "Expedite inbound shipment PO-8892 and redistribute inventory from secondary FC."
6.  **Evidence**: Links to `ANALYTICS.V_DOWNSTREAM_IMPACT`.
