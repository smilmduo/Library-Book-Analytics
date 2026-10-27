import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="Library Book Analytics",
    page_icon="📚",
    layout="wide"
)

DATA_FILE = Path(__file__).resolve().parent.parent / "library_data.csv"

st.title("📚 Library Book Analytics")
st.caption("Big Data Analytics using Hadoop, HDFS, Apache Hive and Python")

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_FILE)
    df["issue_date"] = pd.to_datetime(df["issue_date"], errors="coerce")
    df["book_title"] = df["book_title"].fillna("Unknown")
    df["category"] = df["category"].fillna("Unknown")
    df["student_id"] = df["student_id"].fillna("Unknown")
    return df.dropna(subset=["issue_date"])

try:
    df = load_data()
except Exception as e:
    st.error(f"Could not load the dataset: {e}")
    st.stop()

st.sidebar.header("Filters")

categories = sorted(df["category"].unique().tolist())
selected_categories = st.sidebar.multiselect(
    "Select book categories",
    categories,
    default=categories
)

filtered = df[df["category"].isin(selected_categories)].copy()

if filtered.empty:
    st.warning("No records match the selected filters.")
    st.stop()

total_issues = len(filtered)
unique_books = filtered["book_id"].nunique()
unique_students = filtered["student_id"].nunique()
unique_categories = filtered["category"].nunique()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Book Issues", total_issues)
c2.metric("Unique Books", unique_books)
c3.metric("Borrowers", unique_students)
c4.metric("Categories", unique_categories)

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("📈 Most-Issued Books")
    top_books = (
        filtered.groupby("book_title")
        .size()
        .reset_index(name="Total Issues")
        .sort_values("Total Issues", ascending=False)
        .head(10)
    )
    fig = px.bar(
        top_books.sort_values("Total Issues"),
        x="Total Issues",
        y="book_title",
        orientation="h",
        labels={"book_title": "Book", "Total Issues": "Issues"},
        color="Total Issues",
        color_continuous_scale="Blues"
    )
    fig.update_layout(showlegend=False, coloraxis_showscale=False)
    st.plotly_chart(fig, width='stretch')

with right:
    st.subheader("📚 Category Popularity")
    category_data = (
        filtered.groupby("category")
        .size()
        .reset_index(name="Total Issues")
        .sort_values("Total Issues", ascending=False)
    )
    fig = px.pie(
        category_data,
        names="category",
        values="Total Issues",
        hole=0.4
    )
    st.plotly_chart(fig, width='stretch')

left, right = st.columns(2)

with left:
    st.subheader("📅 Monthly Borrowing Trend")
    monthly = (
        filtered.assign(month=filtered["issue_date"].dt.to_period("M").astype(str))
        .groupby("month")
        .size()
        .reset_index(name="Total Issues")
        .sort_values("month")
    )
    fig = px.line(
        monthly,
        x="month",
        y="Total Issues",
        markers=True,
        labels={"month": "Month", "Total Issues": "Issues"}
    )
    st.plotly_chart(fig, width='stretch')

with right:
    st.subheader("🎓 Frequent Borrowers")
    borrowers = (
        filtered.groupby("student_id")
        .size()
        .reset_index(name="Books Borrowed")
        .sort_values("Books Borrowed", ascending=False)
    )
    fig = px.bar(
        borrowers,
        x="student_id",
        y="Books Borrowed",
        labels={"student_id": "Student ID"}
    )
    st.plotly_chart(fig, width='stretch')

st.subheader("📋 Library Issue Records")
st.dataframe(
    filtered.sort_values("issue_date", ascending=False),
    width='stretch',
    hide_index=True
)

st.download_button(
    "Download Filtered Data as CSV",
    data=filtered.to_csv(index=False).encode("utf-8"),
    file_name="library_analytics.csv",
    mime="text/csv"
)

st.caption(
    "Academic demonstration using sample data. "
    "Hadoop/HDFS stores the dataset and Hive provides SQL analytics; "
    "this dashboard currently reads the project CSV directly."
)
