# utils/ui_style.py
import streamlit as st

def apply_premium_light_theme():
    st.markdown(
        """
<style>
:root{
  --bg:#f6f7fb;
  --card:#ffffff;
  --muted:#5b6475;
  --text:#111827;
  --border:rgba(17,24,39,0.10);
  --shadow: 0 14px 35px rgba(17,24,39,0.08);
  --shadow2: 0 8px 20px rgba(17,24,39,0.06);
  --accent:#5b6cff;
  --accent2:#8b5cf6;
}

.stApp{
  background:
    radial-gradient(900px 600px at 15% 10%, rgba(91,108,255,0.16), transparent 60%),
    radial-gradient(800px 520px at 85% 18%, rgba(139,92,246,0.12), transparent 55%),
    radial-gradient(700px 500px at 50% 95%, rgba(15,118,110,0.06), transparent 55%),
    var(--bg);
  color: var(--text);
}

html, body, [class*="css"]{
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial;
}
h1,h2,h3{
  letter-spacing:-0.03em;
  color: var(--text);
}
p, li, span, label{
  color: var(--muted);
}

.block-container{
  padding-top: 2.2rem;
  padding-bottom: 2.2rem;
  max-width: 1200px;
}

section[data-testid="stSidebar"]{
  background: rgba(255,255,255,0.7);
  backdrop-filter: blur(10px);
  border-right: 1px solid var(--border);
}

.panel{
  background: rgba(255,255,255,0.72);
  backdrop-filter: blur(10px);
  border: 1px solid var(--border);
  border-radius: 22px;
  padding: 1.3rem 1.3rem;
  box-shadow: var(--shadow2);
}

.card{
  background: rgba(255,255,255,0.82);
  backdrop-filter: blur(10px);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 1.15rem 1.15rem;
  box-shadow: var(--shadow2);
  transition: transform .18s ease, box-shadow .18s ease;
}
.card:hover{
  transform: translateY(-4px);
  box-shadow: var(--shadow);
}

.kicker{
  color: var(--muted);
  font-size: 0.95rem;
  margin-bottom: 0.35rem;
}

.hr{
  height: 1px;
  background: rgba(17,24,39,0.08);
  margin: 1.2rem 0 1.6rem 0;
}

.stButton > button{
  border-radius: 14px;
  border: 1px solid rgba(17,24,39,0.14);
  padding: 0.65rem 1rem;
  background: rgba(255,255,255,0.9);
}
.stButton > button:hover{
  border: 1px solid rgba(91,108,255,0.35);
}

header[data-testid="stHeader"]{
  background: transparent;
}
</style>
""",
        unsafe_allow_html=True
    )

def notice(title: str, body: str):
    st.markdown(
        f"""
<div class="panel">
  <div class="kicker">{title}</div>
  <p style="margin:0; line-height:1.75;">{body}</p>
</div>
""",
        unsafe_allow_html=True
    )

def soft_status(title: str, body: str):
    # Same as notice, just a naming convenience
    notice(title, body)
