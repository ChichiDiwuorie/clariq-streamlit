import streamlit as st
from azure.ai.projects import AIProjectClient
from azure.core.credentials import AzureKeyCredential
import time

# ─── Page config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ClarIQ — Know Your Lane. Own Your Path.",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ─── Custom CSS — Amber Gold Theme ──────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:ital,wght@0,300;0,400;1,300&display=swap');

:root {
  --bg: #0c0a06;
  --surface: #141209;
  --border: #2a2410;
  --gold: #f59e0b;
  --gold2: #fb923c;
  --text: #fef3c7;
  --muted: #78716c;
  --success: #86efac;
}

html, body, .stApp {
  background-color: #0c0a06 !important;
  font-family: 'DM Mono', monospace !important;
}

/* Hide Streamlit branding */
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }

/* Main container */
.block-container {
  max-width: 740px !important;
  padding-top: 2rem !important;
}

/* Hero */
.hero {
  text-align: center;
  padding: 48px 0 40px;
}

.badge {
  display: inline-block;
  background: #141209;
  border: 1px solid #2a2410;
  border-radius: 100px;
  padding: 5px 16px;
  font-size: 11px;
  letter-spacing: 0.12em;
  color: #78716c;
  text-transform: uppercase;
  margin-bottom: 24px;
  font-family: 'DM Mono', monospace;
}

.hero-title {
  font-family: 'Syne', sans-serif;
  font-size: 64px;
  font-weight: 800;
  line-height: 0.95;
  letter-spacing: -0.03em;
  color: #fef3c7;
  margin-bottom: 16px;
}

.hero-title .accent {
  background: linear-gradient(135deg, #f59e0b, #fb923c);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-tagline {
  font-size: 12px;
  color: #78716c;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 12px;
}

.hero-sub {
  font-size: 14px;
  color: #a8a29e;
  max-width: 480px;
  margin: 0 auto;
  line-height: 1.7;
  font-style: italic;
}

/* Stats */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  margin: 32px 0;
}

.stat-card {
  background: #141209;
  border: 1px solid #2a2410;
  border-radius: 12px;
  padding: 16px;
  text-align: center;
}

.stat-num {
  font-family: 'Syne', sans-serif;
  font-size: 28px;
  font-weight: 800;
  background: linear-gradient(135deg, #f59e0b, #fb923c);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  display: block;
}

.stat-label {
  font-size: 10px;
  color: #78716c;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin-top: 4px;
}

/* Section labels */
.section-label {
  font-size: 10px;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: #f59e0b;
  margin-bottom: 8px;
  padding-bottom: 8px;
  border-bottom: 1px solid #2a2410;
}

/* Result cards */
.result-card {
  background: #141209;
  border: 1px solid #2a2410;
  border-radius: 16px;
  padding: 24px;
  margin-bottom: 16px;
  position: relative;
}

.result-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, #f59e0b, transparent);
  opacity: 0.4;
  border-radius: 16px 16px 0 0;
}

.result-label {
  font-size: 10px;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: #fb923c;
  margin-bottom: 12px;
  padding-bottom: 8px;
  border-bottom: 1px solid #2a2410;
}

.result-text {
  font-size: 13px;
  line-height: 1.8;
  color: #fef3c7;
  white-space: pre-wrap;
  font-weight: 300;
}

/* Footer */
.clariq-footer {
  text-align: center;
  margin-top: 48px;
  padding-top: 24px;
  border-top: 1px solid #2a2410;
  font-size: 11px;
  color: #57534e;
  letter-spacing: 0.06em;
}

.clariq-footer span { color: #f59e0b; }

/* Streamlit widget overrides */
.stTextArea textarea {
  background-color: #0c0a06 !important;
  border: 1px solid #2a2410 !important;
  border-radius: 10px !important;
  color: #fef3c7 !important;
  font-family: 'DM Mono', monospace !important;
  font-size: 13px !important;
}

.stTextArea textarea:focus {
  border-color: #f59e0b !important;
  box-shadow: 0 0 0 2px rgba(245,158,11,0.15) !important;
}

.stButton button {
  background: linear-gradient(135deg, #f59e0b, #fb923c) !important;
  color: #0c0a06 !important;
  border: none !important;
  border-radius: 10px !important;
  font-family: 'Syne', sans-serif !important;
  font-weight: 700 !important;
  font-size: 15px !important;
  letter-spacing: 0.04em !important;
  padding: 12px 24px !important;
  width: 100% !important;
  transition: all 0.2s !important;
}

.stButton button:hover {
  transform: translateY(-1px) !important;
  box-shadow: 0 8px 32px rgba(245,158,11,0.3) !important;
}

.stSelectbox select {
  background-color: #141209 !important;
  color: #fef3c7 !important;
  border: 1px solid #2a2410 !important;
}

div[data-testid="stExpander"] {
  background: #141209 !important;
  border: 1px solid #2a2410 !important;
  border-radius: 10px !important;
}

.streamlit-expanderHeader {
  color: #a8a29e !important;
  font-size: 12px !important;
}
</style>
""", unsafe_allow_html=True)

# ─── Configuration ───────────────────────────────────────────────────────────
ENDPOINT = st.secrets.get("AZURE_ENDPOINT", "https://clariq-s-resource.services.ai.azure.com/api/projects/ClarIQ-S")
API_KEY = st.secrets.get("AZURE_API_KEY", "9KSDaCPPyg7JzHoyBMpXI3HweWPXkGvE7pvGQk9bWjUA0cAwnGfFJQQJ99CEACfhMk5XJ3w3AAAAACOGVuh4")
KNOWLEDGE_AGENT = "ClarIQ-Knowledge-Agent"
ACTION_AGENT = "ClarIQ-Action-Agent"

# ─── Hero Section ────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="badge">⚡ Powered by Microsoft Foundry</div>
  <div class="hero-title">Clar<span class="accent">IQ</span></div>
  <div class="hero-tagline">Know your lane. Own your path.</div>
  <div class="hero-sub">AI-powered career navigation for non-traditional tech talent. Grounded in real role frameworks from Microsoft, Google, AWS, Salesforce, and IBM.</div>
</div>
""", unsafe_allow_html=True)

# ─── Stats ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="stats-grid">
  <div class="stat-card">
    <span class="stat-num">21</span>
    <span class="stat-label">Role Frameworks</span>
  </div>
  <div class="stat-card">
    <span class="stat-num">5</span>
    <span class="stat-label">Top Companies</span>
  </div>
  <div class="stat-card">
    <span class="stat-num">9</span>
    <span class="stat-label">Knowledge Docs</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ─── Example backgrounds ─────────────────────────────────────────────────────
examples = {
    "Marketing + AWS cert": "I have 3 years of digital marketing experience managing campaigns and analytics dashboards. I recently completed my AWS Cloud Practitioner certification. I'm great at data storytelling and stakeholder communication. Which tech role fits me best?",
    "Engineer pivoting to AI": "I have a Chemical Engineering degree, 2 years at Accenture in consulting, and I've been building AI agents for the past year. I have AZ-900, AI-900, and DP-900 certifications. I hate coding but love building and strategy. What role fits me?",
    "Operations + no certs yet": "I've been in operations and project coordination for 4 years. I manage cross-functional teams, vendor relationships, and delivery timelines. I don't have any tech certifications yet but I'm ready to get them. Where do I start in tech?",
    "Healthcare to tech": "I'm a registered nurse with 7 years of ICU experience. I'm comfortable with data, documentation, and high-stakes decision making. I'm interested in healthcare AI and cloud roles. What path makes sense for someone like me?",
    "Write my own": ""
}

# ─── Input Section ───────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Your Background</div>', unsafe_allow_html=True)

selected = st.selectbox(
    "Try an example or write your own",
    options=list(examples.keys()),
    index=4,
    label_visibility="collapsed"
)

default_text = examples[selected]

user_input = st.text_area(
    "Background",
    value=default_text,
    placeholder="Tell ClarIQ about yourself — your background, experience, certifications, and what kind of tech role you're aiming for...",
    height=160,
    label_visibility="collapsed"
)

# ─── Submit ──────────────────────────────────────────────────────────────────
submit = st.button("Find My Path →")

# ─── Agent Call ──────────────────────────────────────────────────────────────
def call_agent(client, agent_name, agent_version, message):
    openai_client = client.get_openai_client()
    response = openai_client.responses.create(
        input=[{"role": "user", "content": message}],
        extra_body={
            "agent_reference": {
                "name": agent_name,
                "version": agent_version,
                "type": "agent_reference"
            }
        }
    )
    return response.output_text

# ─── Results ─────────────────────────────────────────────────────────────────
if submit and user_input.strip():
    if not ENDPOINT or not API_KEY:
        st.error("Missing Azure credentials. Please configure secrets.")
    else:
        try:
            client = AIProjectClient(
                endpoint=ENDPOINT,
                credential=AzureKeyCredential(API_KEY)
            )

            # Step 1 — Knowledge Agent
            with st.status("ClarIQ is analyzing your background...", expanded=True) as status:
                st.write("🔍 Searching knowledge base...")
                time.sleep(0.5)

                knowledge_prompt = f"""The user has the following background: "{user_input}".
Search the knowledge base and retrieve relevant information about:
1) Which tech roles from our role frameworks best match this background
2) What certifications are recommended for those roles
3) Any relevant research about the navigation gap for people with this type of background.
Cite your sources."""

                knowledge_response = call_agent(client, KNOWLEDGE_AGENT, "3", knowledge_prompt)

                st.write("🗺️ Mapping to role frameworks...")
                time.sleep(0.5)

                # Step 2 — Action Agent
                action_prompt = f"""Based on this user background: "{user_input}"

And this knowledge base research: "{knowledge_response}"

Now provide a specific career positioning plan with exactly three sections:
1. BEST ROLE MATCH — the single best fitting role and why
2. YOUR TOP 3 GAPS — the three most important things missing for that role
3. YOUR NEXT STEPS — a concrete 90-day action plan with specific certifications, projects, and milestones"""

                st.write("⚡ Building your action plan...")
                action_response = call_agent(client, ACTION_AGENT, "1", action_prompt)

                status.update(label="Your ClarIQ navigation plan is ready.", state="complete")

            # Show results
            st.markdown(f"""
<div class="result-card">
  <div class="result-label">Knowledge Retrieval</div>
  <div class="result-text">{knowledge_response}</div>
</div>
""", unsafe_allow_html=True)

            st.markdown(f"""
<div class="result-card">
  <div class="result-label">Your ClarIQ Navigation Plan</div>
  <div class="result-text">{action_response}</div>
</div>
""", unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Something went wrong: {str(e)}")

elif submit and not user_input.strip():
    st.warning("Please tell ClarIQ about your background first.")

# ─── Footer ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="clariq-footer">
  Built on <span>Microsoft Foundry</span> · Multi-agent AI · Grounded in enterprise knowledge · <span>ClarIQ 2026</span>
</div>
""", unsafe_allow_html=True)
