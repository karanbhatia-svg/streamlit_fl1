
import streamlit as st
from pathlib import Path
import base64

st.set_page_config(
    page_title="Karan Bhatia — Backend Engineer",
    page_icon="💻",
    layout="wide",
)

# ---------- Utilities ----------
def badge(label: str):
    st.markdown(f"<span class='badge'>{label}</span>", unsafe_allow_html=True)

def badges(items):
    st.markdown(
        "<div class='badge-wrap'>" + "".join([f"<span class='badge'>{i}</span>" for i in items]) + "</div>",
        unsafe_allow_html=True
    )

def section_title(title, emoji=''):
    st.markdown(f"<h2 class='section'>{emoji} {title}</h2>", unsafe_allow_html=True)

def load_resume_bytes():
    # Try to load a local PDF named 'Karan-Bhatia-Backend-Developer.pdf' if present
    # Otherwise, skip the download button gracefully.
    for p in [Path('Karan-Bhatia-Backend-Developer.pdf'), Path('resume.pdf'), Path('assets/resume.pdf')]:
        if p.exists():
            return p.read_bytes(), p.name
    return None, None

# ---------- Styles ----------
st.markdown(
    """
    <style>
        :root {
        --card-bg: #1F2937;   /* dark gray-blue cards */
        --muted: #94a3b8;     /* muted light gray text */
        --accent: #38bdf8;    /* cyan accent */
        }
        body, .stApp {
        background-color: #0f172a !important;  /* dark navy page */
        color: #e2e8f0 !important;            /* light text */
        }
        /* Sidebar background */
        [data-testid="stSidebar"] {
            background-color: #87cefa !important;
        }
        /* Sidebar text (radio, headers, etc.) */
        [data-testid="stSidebar"] * {
            color: #f8fafc !important;
        }
        /* Style for download button */
        .stDownloadButton > button {
            background-color: #2563eb;   /* blue background */
            color: white;                /* white text */
            border-radius: 8px;
            padding: 0.6rem 1rem;
            border: none;
            font-weight: 600;
        }
        
        .title h1 { margin-bottom: 0.2rem; }
        .subtitle { color: var(--muted); font-size: 0.95rem; }
        .links a { text-decoration: none; margin-right: 0.6rem; }
        .section { margin-top: 2.2rem; padding-top: 0.6rem; border-top: 1px solid #222; }
        .badge-wrap { display: flex; flex-wrap: wrap; gap: 0.5rem; }
        .badge {
            display: inline-block;
            padding: 0.28rem 0.55rem;
            border-radius: 999px;
            border: 1px solid #333;
            background: rgba(255,255,255,0.03);
            font-size: 0.85rem;
            margin-right: 0.25rem;
        }
        .pill {
            display:inline-flex; align-items:center; gap:.35rem;
            border:1px solid #333; padding:.3rem .6rem; border-radius:999px;
            font-size:.85rem;
        }
        .muted { color: var(--muted); }
        .kpi {
            display:grid; grid-template-columns: repeat(3, minmax(0,1fr)); gap: .6rem;
        }
        .kpi .card {
            border:1px solid #222; border-radius: 14px; padding: .9rem;
            background: rgba(255,255,255,0.02);
        }
        .card h4 { margin: 0 0 .4rem 0; }
        .point { margin-bottom: .45rem; }
        .project-card {
            border:1px solid #222; border-radius: 14px; padding: 1rem; margin-bottom: 1rem;
            background: rgba(255,255,255,0.02);
        }
        /* Hide Streamlit default menu, footer, and header */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        [data-testid="collapsedControl"] {
            display: block;  /* force show the sidebar toggle button */
        }

    </style>
    """
    , unsafe_allow_html=True
)

# ---------- Header ----------
left, right = st.columns([3, 1])

with left:
    st.markdown("<div class='title'><h1>Karan Bhatia</h1></div>", unsafe_allow_html=True)
    st.markdown(
    """
    <div class='subtitle'>Python Backend Developer · Django · FastAPI · REST APIs · Data Engineering & ML integration</div><br>
    <div class='muted'>Passionate about building robust, scalable backend systems, Open to backend-focused roles (Django / FastAPI / DRF).</div>
    """,
    unsafe_allow_html=True
)
    st.markdown(
        "<div class='links'>"
        "<a href='mailto:karanb1902@gmail.com'>karanb1902@gmail.com</a>"
        " · <a href='tel:+919306884400'>+91 93068 84400</a>"
        " · <a href='https://github.com/karanbhatia-svg' target='_blank'>GitHub</a>"
        " · <a href='https://www.linkedin.com/in/karan-bhatia-ai/' target='_blank'>LinkedIn</a>"
        " · <span class='muted'>Delhi NCR, India</span>"
        "</div>",
        unsafe_allow_html=True
    )

with right:
    # Quick stats
    st.markdown("<div class='kpi'>", unsafe_allow_html=True)
    st.markdown("<div class='card'><h4>Experience</h4><div>~2+ years</div></div>", unsafe_allow_html=True)
    st.markdown("<div class='card'><h4>APIs built</h4><div>50+ endpoints</div></div>", unsafe_allow_html=True)
    st.markdown("<div class='card'><h4>Focus</h4><div>Scalable SaaS</div></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Resume download
resume_bytes, resume_name = load_resume_bytes()
if resume_bytes:
    st.download_button("⬇️ Download Resume (PDF)", data=resume_bytes, file_name=resume_name, mime="application/pdf")

# ---------- Sidebar Navigation ----------
st.sidebar.title("Navigate")
page = st.sidebar.radio("Go to", ["About", "Experience", "Skills", "Projects", "Certificates", "Education"])

# ---------- About ----------
if page == "About":
    section_title("About", "👋")
    st.write(
        "Backend Python Developer with 2+ years of experience building scalable SaaS solutions. "
        "Skilled in Django, FastAPI, and REST API design. Comfortable with data-heavy systems, "
        "asynchronous processing (Celery), and integrating ML models into production backends."
    )
    badges(["Django", "FastAPI", "DRF", "Celery", "SQL", "PostgreSQL", "MySQL", "MongoDB", "Redis", "Docker", "AWS", "GCP Looker"])

# ---------- Experience ----------
if page == "Experience":
    section_title("Experience", "💼")

    st.subheader("Junior Engineer · PhysioAI")
    st.caption("Jan 2025 — Present · Delhi NCR (Remote/Hybrid)")
    st.markdown("""
    - Built & maintained **50+ REST endpoints** with Django REST Framework; improved response times by **up to 40%** via caching and query optimization.
    - Owned database work across **MySQL/MS SQL**: CRUD, bulk inserts, migrations, indexing, encryption; removed API load bottlenecks and added async tasks for faster processing.
    - Collaborated closely with frontend on GitHub-based workflows to improve API–UI integration and reduce bugs.
    - Integrated **image & chat generation ML models** into Django for real-time posture/health-risk predictions using **Celery**, cron jobs, and REST APIs.
    """)

    st.subheader("Backend Developer Trainee · PhysioAI")
    st.caption("May 2023 — Dec 2024")
    st.markdown("""
    - Learned backend development hands-on across **DRF, databases, and API design**.
    - Helped ship and test core features; contributed to onboarding and documentation for new teammates.
    """)

# ---------- Skills ----------
if page == "Skills":
    section_title("Skills", "🧰")

    st.markdown("**Programming:**")
    badges(["Python", "SQL", "HTML5", "CSS3", "JavaScript", "Bash"])

    st.markdown("**Libraries:**")
    badges(["NumPy", "Pandas", "scikit-learn", "TensorFlow", "Celery", "LangChain", "pdfkit", "PyPDF2", "openpyxl"])

    st.markdown("**Frameworks:**")
    badges(["Django", "Django REST Framework", "FastAPI", "React", "Node.js"])

    st.markdown("**Databases:**")
    badges(["PostgreSQL", "MySQL", "MongoDB", "Django ORM"])

    st.markdown("**WebSockets:**")
    badges(["Django Channels"])

    st.markdown("**Tools & Platforms:**")
    badges(["Git", "GitHub", "Jira", "VS Code", "Linux", "Sentry", "AWS"])

# ---------- Projects ----------
if page == "Projects":
    section_title("Highlighted Projects", "🚀")

    proj = [
        {
            "name": "Clinic Management System",
            "desc": "Role-based access, appointments, bulk data entry, encryption; deployed across hundreds of clinics and sports academies.",
            "stack": ["Django", "MySQL", "DRF"],
            "links": {}
        },
        {
            "name": "ML Model Integration with Django",
            "desc": "Image recognition & posture detection in Django; real-time analysis via REST + Celery; used by hospitals for early diagnosis support.",
            "stack": ["Django", "Celery", "TensorFlow/scikit-learn"],
            "links": {}
        },
        {
            "name": "Data Analysis & Reporting",
            "desc": "APIs for medical/financial/scheduling data, Excel/PDF automation (pdfkit, PyPDF2, openpyxl).",
            "stack": ["DRF", "Excel/PDF automation"],
            "links": {}
        },
        {
            "name": "API Integration Projects",
            "desc": "Designed and integrated APIs across diverse sources with robust error handling and performance tuning.",
            "stack": ["DRF", "FastAPI"],
            "links": {}
        },
        {
            "name": "GCP Looker Dashboards",
            "desc": "Interactive Looker dashboards on BigQuery datasets; custom filters/KPIs for real-time insights.",
            "stack": ["GCP", "Looker", "BigQuery"],
            "links": {}
        },
        {
            "name": "Real-Time Chat App (Django Channels)",
            "desc": "One-on-one & group messaging with auth and message history; Redis-backed routing.",
            "stack": ["Django Channels", "WebSockets", "Redis"],
            "links": {}
        },
        {
            "name": "Django E‑commerce",
            "desc": "Full-featured store with product, cart, checkout; Stripe payments.",
            "stack": ["Django", "PostgreSQL", "Stripe"],
            "links": {"GitHub": "https://github.com/karanbhatia-svg/Ecommerce1/tree/master/Ecommerce"}
        },
        {
            "name": "React + DRF Blog",
            "desc": "Blog front-end in React with DRF backend.",
            "stack": ["React", "DRF"],
            "links": {"GitHub": "https://github.com/karanbhatia-svg/React-django-blog"}
        },
        {
            "name": "Food Calorie Calculator",
            "desc": "FastAPI backend with Chart.js visualizations on the front-end.",
            "stack": ["FastAPI", "Chart.js"],
            "links": {"GitHub": "https://github.com/karanbhatia-svg/Food-calculator/tree/master/foodie"}
        },
    ]

    for p in proj:
        with st.container(border=False):
            st.markdown(f"<div class='project-card'><h3>{p['name']}</h3><p class='muted'>{p['desc']}</p></div>", unsafe_allow_html=True)
            badges(p["stack"])
            if p["links"]:
                link_str = " · ".join([f"[{k}]({v})" for k, v in p["links"].items()])
                st.markdown(link_str)
            st.divider()

# ---------- Certificates ----------
if page == "Certificates":
    section_title("Certificates", "📜")
    st.markdown("- **Python Full-Stack** — 4 months training, DUCAT Gurgaon")
    st.markdown("- **Introduction to Data Analysis** — Simplilearn")

# ---------- Education ----------
if page == "Education":
    section_title("Education", "🎓")
    st.markdown("**B.Sc (Hons) in Computer Data Science** — Guru Jambheshwar University of Science & Technology, Hisar (2019–2022)")
    st.markdown("**12th (PCM)** — CBSE (2018–2019)")

# ---------- Contact ----------
# if page == "Contact":
#     section_title("Contact", "✉️")
#     st.write("Open to backend-focused roles (Django / FastAPI / DRF). For collaboration or opportunities, drop a message below or send an email.")
#     with st.form("contact"):
#         name = st.text_input("Your name")
#         email = st.text_input("Your email")
#         msg = st.text_area("Message")
#         submitted = st.form_submit_button("Create email draft")
#         if submitted:
#             subject = f"Hello Karan — from {name}".strip()
#             body = f"""Hi Karan,%0D%0A%0D%0A{msg}%0D%0A%0D%0A— {name} ({email})"""
#             mailto = f"mailto:karanb1902@gmail.com?subject={subject}&body={body}"
#             st.success("Click below to open your email client with a pre-filled message.")
#             st.markdown(f"[Compose Email]({mailto})")


st.sidebar.markdown("---")
st.sidebar.caption("© Karan Bhatia")
