# Cortex Agent / CoCo CLI

SupplyShield uses the Snowflake CLI (`coco` or `snow`) and Cortex Search/Agent capabilities to deploy governed conversational analytics.

## Skill Definition
Located in `.cortex/skills/supplyshield/SKILL.md`, this defines the domain vocabulary, metrics, and risk rules for the Cortex Agent.

## Deployment
```bash
snow cortex agent deploy --skill .cortex/skills/supplyshield
```
