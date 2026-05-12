# ClarIQ
### Know Your Lane. Own Your Path.
 
> AI-powered career navigation for non-traditional tech talent — built on Microsoft Foundry
 
[![Live App](https://img.shields.io/badge/Live%20App-clariq--app.streamlit.app-F59E0B?style=for-the-badge&logo=streamlit)](https://clariq-app.streamlit.app)
[![Microsoft Foundry](https://img.shields.io/badge/Built%20on-Microsoft%20Foundry-0078D4?style=for-the-badge&logo=microsoft)](https://ai.azure.com)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)](https://python.org)
 
---
 
## The Problem
 
Millions of talented professionals cannot break into the AI and cloud economy. Not because they lack skills. Not because opportunities don't exist. But because of a documented, researched, named barrier:
 
**The Navigation Gap.**
 
> "Not a skills gap. Not an opportunity gap. A navigation gap."
> — Women in Cloud Economic Access Report 2026
 
- Only **10%** of respondents said pathways to employment were clear
- **56%** said access to funding and entrepreneurship pathways was unclear
- Post-ChatGPT, demand for analytical and technical roles grew **20%** (Harvard Business School)
Career pivoters, women in cloud, STEM professionals from adjacent fields, bootcamp graduates, and first-generation tech professionals all face the same problem: real skills, no clear map.
 
---
 
## The Solution
 
ClarIQ is a **governed multi-agent AI system** built on Microsoft Foundry that closes the navigation gap for non-traditional tech talent.
 
It turns a user's background into a specific, grounded, actionable career positioning plan in under 60 seconds — grounded in real enterprise role frameworks, not generic career advice.
 
**The transformation:**
- From: scattered background, unclear pathways, imposter syndrome
- To: specific role match, three concrete gaps, 90-day action plan
---
 
## Live Demo
 
**[clariq-app.streamlit.app](https://clariq-app.streamlit.app)**
 
Try it with your own background or use one of the built-in examples:
- Marketing professional + AWS cert → AI Product Manager path
- Chemical Engineer pivoting to AI → Cloud Solution Architect path
- Operations coordinator with no certs → Technical Program Manager path
- ICU nurse interested in healthcare AI → Healthcare AI Consultant path
---
 
## Architecture
 
ClarIQ is a sequential multi-agent workflow built on Microsoft Foundry (Sweden Central):
 
```
User Input
    ↓
ClarIQ Knowledge Agent (v8)
    ↓ Retrieves grounded context from enterprise knowledge base
    ↓ Cites sources: role frameworks, cert paths, research
ClarIQ Action Agent (v7)
    ↓ Maps background to best-fit role
    ↓ Identifies top 3 gaps
    ↓ Generates 90-day action plan
Output → Streamlit UI
```
 
### Agent 1: ClarIQ Knowledge Agent
 
| Property | Value |
|----------|-------|
| Model | GPT-5 Mini (Microsoft Foundry) |
| Role | Career navigation knowledge specialist |
| Knowledge Base | 9 enterprise documents (Azure AI Search) |
| Guardrail | ClarIQ-Guardrail (custom enterprise) |
| Entra Agent ID | `e15f3e4d-f7f1-4e87-96b2-c628f2a29029` |
| Version | v8 (published) |
 
**System Prompt:**
```
You are ClarIQ's Knowledge Agent, a career navigation specialist for non-traditional 
tech job seekers. Answer questions grounded exclusively in the indexed knowledge base 
documents. Always cite which document your answer comes from. Never fabricate role 
requirements or salary figures. Be concise. Maximum 250 words. Use bullet points.
```
 
### Agent 2: ClarIQ Action Agent
 
| Property | Value |
|----------|-------|
| Model | GPT-5 Mini (Microsoft Foundry) |
| Role | Career positioning specialist and action planner |
| Input | User background + Knowledge Agent output |
| Guardrail | ClarIQ-Guardrail (custom enterprise) |
| Entra Agent ID | `b69d350b-7b2d-452c-92a6-d0957b126c15` |
| Version | v7 (published) |
 
**System Prompt:**
```
You are ClarIQ's Action Agent, a career positioning specialist. Map the user's 
background to the most suitable tech role from the available role frameworks. 
Identify their top three skill or certification gaps for that role. Output a 
prioritized action plan. Three sections only: BEST ROLE MATCH, YOUR TOP 3 GAPS, 
YOUR NEXT STEPS. Maximum 350 words. No optional follow-up offers.
```
 
### Workflow: ClarIQ Orchestrator
 
| Property | Value |
|----------|-------|
| Type | Sequential workflow |
| Step 1 | ClarIQ Knowledge Agent |
| Step 2 | ClarIQ Action Agent |
| Guardrail | ClarIQ-Guardrail applied at workflow level |
| Entra Workflow ID | `978fff5e-be3b-40dc-8bfb-ef6cf44a255b` |
| Tracing | Application Insights (clariq-insights) |
 
---
 
## Knowledge Base
 
9 enterprise documents indexed in Azure AI Search (Sweden Central):
 
| # | Document | Purpose |
|---|----------|---------|
| 1 | Women in Cloud Economic Access Report 2026 | Navigation gap research and evidence |
| 2 | Harvard Business School AI Job Market Research | Market reality and demand shifts |
| 3 | MIT Sloan AI/ML Careers | Role taxonomy and employer landscape |
| 4 | Forbes 10 Highest Paying AI Jobs 2026 | Salary benchmarks by role |
| 5 | Forbes 20 AI-Resistant Careers 2026 | Career stability analysis |
| 6 | Coursera 9 AI Jobs to Explore 2026 | Entry path and certification guidance |
| 7 | FAANG Role Frameworks | 21 roles across Microsoft, Google, AWS, Salesforce, IBM |
| 8 | Certification Path Map | 2026 updated paths across all 5 platforms |
| 9 | Skills Translation Guide | 6 non-traditional background paths into tech |
 
---
 
## Security and Governance
 
### Guardrails
 
**ClarIQ-Guardrail** — custom enterprise guardrail applied to both agents and the orchestrator workflow:
 
| Control | Coverage | Action |
|---------|----------|--------|
| Jailbreak | User input | Block |
| Indirect prompt injections | User input, Tool output | Block |
| Sensitive data leakage | 46 PII types — all intervention points | Block |
| Task drift | Tool input | Annotate |
| Content safety | Hate, self-harm, sexual, violence | Block (medium threshold) |
| Protected materials | Code and text | Block |
 
### Identity Governance (Microsoft Entra ID)
 
All agents are registered as enterprise applications with managed identities:
 
| Agent | Object ID | Application ID |
|-------|-----------|----------------|
| Knowledge Agent | `e15f3e4d-f7f1-4e87-96b2-c628f2a29029` | `e15f3e4d-f7f1-4e87-96b2-c628f2a29029` |
| Action Agent | `b69d350b-7b2d-452c-92a6-d0957b126c15` | `b69d350b-7b2d-452c-92a6-d0957b126c15` |
| Orchestrator | `978fff5e-be3b-40dc-8bfb-ef6cf44a255b` | `52bdb589-e10d-4395-a598-61e618051e24` |
 
Access management: RBAC restricts agent modification and republishing to the project owner. Guardrail policy is centrally managed and enforced across all three components.
 
---
 
## Traces
 
Application Insights (clariq-insights) connected for full observability:
 
| Conversation | Status | Duration | Tokens In | Tokens Out | Cost |
|-------------|--------|----------|-----------|------------|------|
| conv_943... | ✅ Completed | 16.5s | 504 | 774 | $0.002 |
| conv_e98... | ❌ Failed (guardrail) | 3.0s | 0 | 0 | - |
| conv_515... | ❌ Failed (guardrail) | 4.4s | 0 | 0 | - |
 
**Trace insight:** Failed traces revealed Task drift guardrail was over-blocking legitimate career navigation queries. Configuration adjusted from Block to Annotate — preserving audit logging while allowing valid responses.
 
---
 
## Test Cases
 
### Test 1: Complete Success Case
**Input:** Digital marketing background, 3 years, AWS Cloud Practitioner, strong stakeholder communication  
**Output:** AI Product Manager (AWS L4) — specific role match with 3 gaps and 90-day plan  
**Status:** ✅ Completed in 16.5 seconds
 
### Test 2: Guardrail Trigger (Edge Case)
**Input:** Prompt triggering task drift detection  
**Output:** "This interaction was blocked by a safety and security control"  
**Status:** ✅ Correctly blocked — 0 tokens consumed, $0 cost
 
### Test 3: Non-Traditional Background
**Input:** ICU nurse, 7 years experience, interested in healthcare AI  
**Output:** Healthcare AI Consultant (IBM L3) — mapped clinical skills to responsible AI governance  
**Status:** ✅ Completed with accurate role mapping and certification path
 
---
 
## Tech Stack
 
| Layer | Technology |
|-------|-----------|
| Agent Platform | Microsoft Foundry (Azure AI Foundry) |
| Models | GPT-5 Mini |
| Knowledge Store | Azure AI Search (Sweden Central) |
| Blob Storage | Azure Blob Storage (West US 3) |
| Observability | Azure Application Insights |
| Identity | Microsoft Entra ID (Managed Identities) |
| Frontend | Streamlit (Python) |
| Hosting | Streamlit Cloud |
| Source Control | GitHub |
 
---
 
## Local Setup
 
```bash
# Clone the repo
git clone https://github.com/ChichiDiwuorie/clariq-streamlit.git
cd clariq-streamlit
 
# Install dependencies
pip install -r requirements.txt
 
# Configure secrets
mkdir .streamlit
cat > .streamlit/secrets.toml << EOF
AZURE_ENDPOINT = "your_foundry_project_endpoint"
AZURE_API_KEY = "your_api_key"
EOF
 
# Run locally
streamlit run app.py
```
 
---
 
## Project Structure
 
```
clariq-streamlit/
├── app.py              # Streamlit frontend + agent API calls
├── requirements.txt    # Python dependencies
├── .gitignore         # Excludes secrets.toml
└── README.md          # This file
```
 
---
 
## Impact
 
ClarIQ addresses a problem affecting millions — not just women in cloud, but every career pivoter, every STEM professional repositioning into AI, every first-generation tech job seeker with real skills and no clear map.
 
The navigation gap is a systemic barrier that costs the AI economy diverse talent at exactly the moment when diverse thinking is most needed.
 
**Roadmap:**
- Resume analysis — map uploaded resumes directly to role frameworks
- Real-time job posting integration — identify which roles are actively hiring
- Community features — connect users with mentors who made similar transitions
- Industry expansion — healthcare AI, fintech, media tech role frameworks
---
 
## Built By
 
**Chinwendu Doris Iwuorie**  
AI Technical Program Manager | Cloud, Multi-Agent Systems  
Founder, Corro AI — Empowering operations with intelligent systems
 
Submitted to: **Microsoft x Founderz Agent-a-thon | Level 3: Master Agents**  
May 2026
 
---
 
*Built on Microsoft Foundry · Multi-agent AI · Grounded in enterprise knowledge · ClarIQ 2026*
