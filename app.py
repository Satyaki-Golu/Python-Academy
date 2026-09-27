"""
app.py
Responsive Streamlit Python Academy - Optimized for Mobile and Desktop.
"""

import io
import sys
import streamlit as st
from curriculum import CURRICULUM

# 1. Page Configuration: Centered layout is cleaner on mobile screens
st.set_page_config(
    page_title="Python Academy",
    page_icon="🐍",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom mobile CSS tweaks for buttons, text areas, and padding
st.markdown(
    """
    <style>
    /* Improve touch targets and reduce excess padding on mobile */
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 3rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }
    button[kind="primary"], button[kind="secondary"] {
        width: 100% !important;
        min-height: 48px !important;
        font-size: 16px !important;
    }
    textarea {
        font-size: 15px !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def run_code(code_str: str) -> str:
    """Executes Python code in memory and captures console output."""
    buffer = io.StringIO()
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    sys.stdout = buffer
    sys.stderr = buffer
    try:
        scope = {}
        exec(code_str, scope)
        output = buffer.getvalue()
        return output if output else "[Code ran successfully with no console output]"
    except Exception as exc:
        return f"{type(exc).__name__}: {exc}"
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr


# Initialize session state for lesson completion
if "completed_topics" not in st.session_state:
    st.session_state.completed_topics = set()

# Total progress metrics
all_lesson_keys = [
    f"{sec}::{topic}"
    for sec, topics in CURRICULUM.items()
    for topic in topics.keys()
]
total_lessons = len(all_lesson_keys)
completed_lessons = len(st.session_state.completed_topics)
progress_ratio = completed_lessons / total_lessons if total_lessons > 0 else 0.0

# ----------------- TOP BANNER & PROGRESS -----------------
st.title("🐍 Python Academy")
st.caption("Mobile-friendly interactive learning platform")

st.progress(progress_ratio)
st.write(f"📊 **Progress:** {completed_lessons}/{total_lessons} lessons completed ({int(progress_ratio * 100)}%)")

st.divider()

# ----------------- IN-PAGE SELECTORS (Mobile First) -----------------
# Learners on phones don't need to open the hamburger sidebar to navigate
selected_section = st.selectbox(
    "📁 Step 1: Select Module",
    list(CURRICULUM.keys()),
    key="mobile_sec_select",
)

topics_in_section = list(CURRICULUM[selected_section].keys())


def topic_label(topic_name: str) -> str:
    key = f"{selected_section}::{topic_name}"
    return f"✅ {topic_name}" if key in st.session_state.completed_topics else f"⚪ {topic_name}"


selected_topic = st.selectbox(
    "📖 Step 2: Select Lesson",
    topics_in_section,
    format_func=topic_label,
    key="mobile_topic_select",
)

current_key = f"{selected_section}::{selected_topic}"
lesson = CURRICULUM[selected_section][selected_topic]

# Checkbox toggle for lesson status
is_done = current_key in st.session_state.completed_topics
mark_done = st.checkbox(
    "Mark lesson as completed",
    value=is_done,
    key=f"chk_{current_key}",
)

if mark_done:
    st.session_state.completed_topics.add(current_key)
else:
    st.session_state.completed_topics.discard(current_key)

st.divider()

# ----------------- INTERACTIVE TABS -----------------
tab_learn, tab_run, tab_challenge = st.tabs(["📖 Lecture", "💻 Code Sandbox", "🎯 Challenge"])

with tab_learn:
    st.markdown(lesson["theory"])
    st.subheader("Reference Code")
    st.code(lesson["demo_code"], language="python")

with tab_run:
    st.markdown("### Interactive Runner")
    st.caption("Tap below to edit and run code on your device:")

    sandbox_input = st.text_area(
        "Python Code:",
        value=lesson["demo_code"],
        height=200,
        key=f"mobile_sandbox_{current_key}",
    )

    if st.button("▶ Run Code", type="primary", use_container_width=True, key=f"btn_run_{current_key}"):
        with st.spinner("Executing..."):
            out = run_code(sandbox_input)
            st.markdown("**Console Output:**")
            st.code(out, language="text")

with tab_challenge:
    st.markdown("### Practical Challenge")
    st.info(lesson["challenge"])

    challenge_input = st.text_area(
        "Write your solution:",
        height=150,
        placeholder="# Type your Python code here...",
        key=f"mobile_chal_{current_key}",
    )

    if st.button("Test My Solution", type="primary", use_container_width=True, key=f"btn_test_{current_key}"):
        if not challenge_input.strip():
            st.warning("Please write some code before testing!")
        else:
            test_out = run_code(challenge_input)
            st.markdown("**Your Output:**")
            st.code(test_out, language="text")

    with st.expander("👀 Show Reference Solution"):
        st.code(lesson["solution"], language="python")