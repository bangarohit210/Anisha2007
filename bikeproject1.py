import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
import plotly .express as px
import streamlit as st

st.sidebar.markdown("🚴Bike Sales Data Analysis")
menu = st.sidebar.radio("Navigation",( "🏠 Home","📊 Data Overview", "💰 Sales Analysis", "👥 Customer Analysis", "📈 Charts","📝 Conclusion" ))
if menu=="🏠 Home":
    st.title("🚴Bike Sales Data Analysis")
    st.markdown("The Bike Sales Data Analysis project is a Data Science dashboard that analyzes bike sales data to provide valuable business insights. It helps users understand sales performance, revenue trends, customer behavior, product categories, and regional sales through interactive charts and visualizations. The dashboard is developed using Python, Pandas, Plotly, and Streamlit to make data analysis simple, clear, and interactive.")
    col1,col2=st.columns(2)
    with col1:
        st.image("bike3.jpg",width=300)
    with col2:
        st.image("bike2.jpg",width=280)

st.title("📊 Data Overview")

st.markdown("""
The **Data Overview** section provides a summary of the bike sales dataset.
It helps users understand the dataset's structure, including the number of records,
columns, data types, and missing values before performing detailed analysis.
""")


# Upload CSV file
uploaded_file = st.file_uploader(
    "📁 Upload Bike Sales Dataset (sales_data.csv)",
    type=["csv"]
)

if uploaded_file is not None:
    # Read CSV
    df = pd.read_csv(uploaded_file)

    st.success("✅ Dataset uploaded successfully!")

    # Preview
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # Shape
    st.subheader("Dataset Shape")
    st.write(f"**Rows:** {df.shape[0]}")
    st.write(f"**Columns:** {df.shape[1]}")
