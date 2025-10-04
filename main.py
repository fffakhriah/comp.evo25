import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Nurul Fakhriah's Resume", page_icon="💼", layout="wide")

# --- Title ---
st.title("💼 Nurul Fakhriah's Resume")

# --- About Me Section ---
st.markdown("""
### 👩‍💻 About Me  
Passionate about technology and digital innovation.  
I love working in teams, solving problems, and exploring new ideas.
""")

# --- Contact Information ---
st.header("📞 Contact Information")
contact_col1, contact_col2 = st.columns(2)
with contact_col1:
    st.write("📧 Email: fakhriahyusoff.com")
    st.write("📱 Phone: 019-9455026")
with contact_col2:
    st.write("🔗 LinkedIn: [linkedin.com/in/nfakhriah](https://linkedin.com/in/nfakhriah)")

# --- Education ---
st.header("🎓 Education")
st.write("📚 **Bachelor of Information Technology**, University Malaysia Kelantan, 2025")

# --- Work Experience ---
st.header("💼 Work Experience")
st.write("👩‍💻 **Internship**, Education State of Kelantan, 2023")
st.write("- 🤝 Helped the Director deal with company issues")

# --- Skills ---
st.header("🛠️ Skills")
skills_col1, skills_col2 = st.columns(2)
with skills_col1:
    st.write("- 👥 Teamwork")
    st.write("- 💬 Communication")
with skills_col2:
    st.write("- 🧠 Critical Thinking")
    st.write("- 💻 Problem Solving")

# --- Projects ---
st.header("🚀 Projects")
st.write("💻 **Computer Evolution Project** – Project for this semester")

# --- Footer ---
st.markdown("---")
st.markdown("🌟 *Thank you for visiting my digital resume!*")
