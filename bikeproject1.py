import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly .express as px
import streamlit as st
import base64

from streamlit_option_menu import option_menu
st.sidebar.title("🚴Bike Sales Data Analysis")
st.set_page_config("Bike Sales Analysis","🚵" , layout= "wide")
with st.sidebar:
    menu = option_menu(
        "Navigation",
        [ "Dashboard", "Data Overview", "Revenue Analysis", "Data Visualizations","Insights"],
        icons=["house", "speedometer2", "table", "graph-up", "bar-chart","lightbulb"   ],
        default_index=0,
        styles={
            "container": {"padding": "5px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "5px",
                "--hover-color": "#E5E7EB",
            },
            "nav-link-selected": {
                "background-color": "#2563EB",
                "color": "white",
            },
        },
    )

# Read image
with open("image4.jpg", "rb") as img:
    encoded = base64.b64encode(img.read()).decode()

# HTML + CSS
st.markdown(f"""
<style>

.stApp {{
    background: url("data:image/jpg;base64,{encoded}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

</style>
""", unsafe_allow_html=True)



# st.sidebar.markdown("🚴Bike Sales Data Analysis")
# menu = st.sidebar.radio("Navigation",[ "🏠 Home","📋 Dashboard","📊 Data Overview","📈 Revenue Analysis" , "📉 Data Visualizations"])
try:
    df=pd.read_csv("sales_data.csv")
except:
    st.error("Dataset file not found")
    st.stop()

# if menu=="Home":
#     st.title("🚴Bike Sales Data Analysis")
#     st.markdown("The Bike Sales Data Analysis project is a Data Science dashboard that analyzes bike sales data to provide valuable business insights. It helps users understand sales performance, revenue trends, customer behavior, product categories, and regional sales through interactive charts and visualizations. The dashboard is developed using Python, Pandas, Plotly, and Streamlit to make data analysis simple, clear, and interactive.")
#     col1,col2=st.columns(2)
#     with col1:
#         st.image("bike3.jpg",width=300)
#     with col2:
#         st.image("bike2.jpg",width=280)
#         # Project Objectives
#     st.header("🎯 Project Objectives")

#     st.write(" Analyze bike sales performance.")
#     st.write(" Identify revenue and profit trends.")
#     st.write(" Compare product categories.")
#     st.write(" Understand customer purchasing behavior.")
#     st.write("Support better business decisions")

if menu == "Dashboard":

    st.title("📋 Bike Sales Dashboard")
    st.markdown("---")
    # st.image("image4.jpg")

    # ================= KPI =================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("💰 Revenue", f"${df['Revenue'].sum():,.0f}")

    with col2:
        st.metric("📈 Profit", f"${df['Profit'].sum():,.0f}")

    with col3:
        st.metric("📦 Orders", int(df["Order_Quantity"].sum()))

    with col4:
        st.metric("👥 Customers", len(df))

    st.markdown("---")

    # ================= Charts =================

    col1, col2 = st.columns(2)

    with col1:

        category = df.groupby("Product_Category")["Revenue"].sum().reset_index()

        fig = px.pie(
            category,
            names="Product_Category",
            values="Revenue",
            hole=0.5,
            color_discrete_sequence=px.colors.qualitative.Set3,
            title="Revenue by Category"
        )

        fig.update_layout(template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)

    with col2:

        country = (
            df.groupby("Country")["Order_Quantity"]
            .sum()
            .nlargest(5)
            .reset_index()
        )

        fig = px.bar(
            country,
            x="Country",
            y="Order_Quantity",
            color="Country",
            color_discrete_sequence=px.colors.qualitative.Bold,
            title="Top 5 Countries"
        )
        st.plotly_chart(fig, use_container_width=True)


    col3, col4 = st.columns(2)
    with col3:

        age = df.groupby("Age_Group")["Revenue"].sum().reset_index()

        fig = px.bar(
        age,
        x="Age_Group",
        y="Revenue",
        color="Age_Group",
        title="Age Group"
    )

        fig.update_layout(
        template="plotly_dark",
        height=300
    )

        # st.plotly_chart(fig, use_container_width=True)

        fig.update_layout(template="plotly_dark")

        st.plotly_chart(fig, use_container_width=True)
    with col4:

        gender = df.groupby("Customer_Gender")["Order_Quantity"].sum().reset_index()

        fig = px.pie(
            gender,
            names="Customer_Gender",
            values="Order_Quantity",
            hole=0.5,
            title="Gender"
        )

        fig.update_layout(
            template="plotly_dark",
            height=300
        )

        st.plotly_chart(fig, use_container_width=True)
    col5, col6 = st.columns(2)
    with col5:

        sub_cat = (
            df.groupby("Sub_Category")["Revenue"]
            .sum()
            .sort_values(ascending=False)
            .reset_index()
        )

        fig = px.bar(
            sub_cat,
            x="Revenue",
            y="Sub_Category",
            orientation="h",
            color="Revenue",
            title="Revenue by Sub Category",
            color_continuous_scale="Blues"
        )

        fig.update_layout(
            template="plotly_dark",
            height=350
        )

        st.plotly_chart(fig, use_container_width=True)
    with col6:
        fig = px.histogram(
            df,
            x="Profit",
            nbins=25,
            title="Profit Distribution",
            color_discrete_sequence=["orange"]
        )

        fig.update_layout(
            template="plotly_dark",
            height=350
        )

        st.plotly_chart(fig, use_container_width=True)


    


    
   
    
elif menu=="Data Overview":
    st.title("📊 Data Overview")
    st.markdown("""
The **Data Overview** section provides a summary of the bike sales dataset.
It helps users understand the dataset's structure, including the number of records,
columns, data types, and missing values before performing detailed analysis.
""")
    st.dataframe(df,width="stretch")
    df=pd.read_csv("sales_data.csv")
    st.subheader("First 10 Records")
    st.dataframe(df.head(10), width="stretch")

        

elif menu == "Revenue Analysis":

    st.title("📈 Revenue Analysis")

    st.write("""
    Welcome to the Revenue Analysis section.
    Here you can explore bike sales performance, revenue trends,
    product-wise sales, and customer insights.
    """)
    
# graph1
#      st.subheader("📈 Monthly Revenue Analysis")

#     monthly_revenue = df.groupby("Month")["Revenue"].sum()

#     plt.figure(figsize=(), facecolor="black")
#     ax = plt.gca()
#     ax.set_facecolor("black")

#     plt.plot(
#     monthly_revenue.index,
#     monthly_revenue.values,
#     color="cyan",
#     marker="o",
#     markersize=8,
#     linewidth=3
# )

#     plt.title("Monthly Revenue", color="white", fontsize=15)
#     plt.xlabel("Month", color="white")
#     plt.ylabel("Revenue", color="white")

#     plt.xticks(rotation=45, color="white")
#     plt.yticks(color="white")

#     plt.grid(color="gray", linestyle="--", alpha=0.4)

# # White border
#     for spine in ax.spines.values():
#         spine.set_color("white")

#     st.pyplot(plt)
    st.subheader("📈 Monthly Revenue Analysis")

    monthly_revenue = df.groupby("Month")["Revenue"].sum()

    fig, ax = plt.subplots(figsize=(10,6))

    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")

    ax.plot(
    monthly_revenue.index,
    monthly_revenue.values,
    color="cyan",
    marker="o",
    markersize=5,
    linewidth=2
)

    ax.set_title("Monthly Revenue", color="white", fontsize=10)
    ax.set_xlabel("Month", color="white", fontsize=8)
    ax.set_ylabel("Revenue", color="white", fontsize=8)

    ax.tick_params(axis="x", colors="white", labelsize=6, rotation=45)
    ax.tick_params(axis="y", colors="white", labelsize=6)

    ax.grid(color="gray", linestyle="--", alpha=0.3)

    for spine in ax.spines.values():
       spine.set_color("white")

    plt.tight_layout()

    st.pyplot(fig)
    plt.close(fig)



#graph2
#
    st.subheader("Revenue by Product Category")

    category_revenue = df.groupby("Product_Category")["Revenue"].sum()

    colors = ["red", "blue", "green", "orange", "purple", "cyan", "yellow"]

    plt.figure(figsize=(10,6), facecolor="black")
    ax = plt.gca()
    ax.set_facecolor("black")

    plt.bar(
    category_revenue.index,
    category_revenue.values,
    color=colors,
    edgecolor="white",
    width=0.5
)

    plt.title("Revenue by Product Category", color="white")
    plt.xlabel("Product Category", color="white")
    plt.ylabel("Revenue", color="white")
    plt.xticks(rotation=30, color="white")
    plt.yticks(color="white")
    plt.grid(axis="y", linestyle="--", alpha=0.3)

    st.pyplot(plt)
    col3, col4, = st.columns(2)  
#  graph3
    st.subheader("📅 Yearly Revenue Analysis")

    data = df.groupby("Year")["Revenue"].sum()

    plt.style.use("dark_background")   # Dark palette

    plt.figure(figsize=(6,4))

    plt.bar(
    data.index.astype(str),
    data.values,
    color=["#00BFFF", "#FF6F61", "#FFD700", "#32CD32", "#BA55D3"],
    edgecolor="white",
    width=0.5
)

    plt.title("Yearly Revenue", color="white")
    plt.xlabel("Year", color="white")
    plt.ylabel("Revenue", color="white")
    plt.grid(axis="y", color="gray", linestyle="--", alpha=0.4)

    st.pyplot(plt)
#     # graph4
#     st.subheader("🌍 Revenue by Country")

#     country_revenue = (
#     df.groupby("Country")["Revenue"]
#       .sum()
#       .sort_values(ascending=False)
# )

#     fig, ax = plt.subplots(figsize=(5,3), facecolor="black")
#     ax.set_facecolor("black")

#     colors = ["#00E5FF", "#00B8D4", "#0097A7", "#4DD0E1", "#80DEEA"]

#     ax.bar(
#     country_revenue.index,
#     country_revenue.values,
#     color=colors[:len(country_revenue)]
# )

#     ax.set_title("Revenue by Country", color="white")
#     ax.set_xlabel("Country", color="white")
#     ax.set_ylabel("Revenue", color="white")

#     ax.tick_params(colors="white")

#     for spine in ax.spines.values():
#        spine.set_color("white")

#     plt.xticks(rotation=45)
#     plt.grid(axis="y", linestyle="--", alpha=0.3)

#     st.pyplot(fig)

    import plotly.express as px

    st.subheader("🗺️ Revenue by State")

# Revenue by State
    state_revenue = (
    df.groupby("State", as_index=False)["Revenue"]
    .sum()
    .sort_values(by="Revenue", ascending=False)
)

# Plotly Bar Chart
    fig = px.bar(
    state_revenue,
    x="State",
    y="Revenue",
    color="Revenue",
    color_continuous_scale="Turbo",
    title="Revenue by State"
)

# Layout
    fig.update_layout(
    template="plotly_dark",
    height=550,          # Graph height
    width=850,           # Graph width
    title_x=0.5,
    xaxis_title="State",
    yaxis_title="Revenue",
    xaxis_tickangle=-45,
    font=dict(size=14)
)

# Show Graph
    st.plotly_chart(fig, use_container_width=False)

    
     


elif menu=="Data Visualizations":
    st.title("📉 Data Visualizations")
    st.write("This page displays charts and graphs for visual analysis of the Bike Sales dataset.")

# graph1
    # plt.figure(figsize=(8,5))

    # plt.hist(df["Customer_Age"], bins=10,rwidth=0.8)

    # plt.title("Customer Age Distribution", pad=15)
    # plt.xlabel("Customer Age", labelpad=10)
    # plt.ylabel("Count", labelpad=10)

    # plt.tight_layout()   # Graph ke around space adjust karega
    # st.pyplot(plt)
#     plt.figure(figsize=(8,5), facecolor="black")

#     ax = plt.gca()
#     ax.set_facecolor("black")   # Graph background black

#     plt.hist(
#     df["Customer_Age"],
#     bins=10,
#     rwidth=0.8,
#     color="skyblue",
#     edgecolor="white"
# )

#     plt.title("Customer Age Distribution", color="white", fontsize=14, pad=15)
#     plt.xlabel("Customer Age", color="white", labelpad=10)
#     plt.ylabel("Count", color="white", labelpad=10)

#     plt.xticks(color="white")
#     plt.yticks(color="white")

# # White border
#     for spine in ax.spines.values():
#         spine.set_color("white")

#     plt.tight_layout()
#     st.pyplot(plt)


    st.subheader(" Customer Age Distribution")

    plt.figure(figsize=(8,5), facecolor="black")

    ax = plt.gca()
    ax.set_facecolor("black")

# Different colors for each bar
    colors = [
    "#FF4B4B", "#FFA500", "#FFFF00", "#32CD32",
    "#00CED1", "#1E90FF", "#8A2BE2", "#FF1493",
    "#00FF7F", "#FF69B4"
]

    n, bins, patches = plt.hist(
    df["Customer_Age"],
    bins=10,
    rwidth=0.85,
    edgecolor="white"
)

# Apply different color to each bar
    for patch, color in zip(patches, colors):
        patch.set_facecolor(color)

    plt.title("Customer Age Distribution", color="white", fontsize=15, pad=15)
    plt.xlabel("Customer Age", color="white", fontsize=12)
    plt.ylabel("Count", color="white", fontsize=12)

    plt.xticks(color="white")
    plt.yticks(color="white")

# White Border
    for spine in ax.spines.values():
        spine.set_color("white")

    plt.grid(axis="y", linestyle="--", alpha=0.3, color="white")

    plt.tight_layout()
    st.pyplot(plt)
    # garph2

    data = df.groupby("Product_Category")["Revenue"].sum()

    colors = ["#00C853", "#2979FF", "#FFD600"]   # Green, Blue, Yellow

    plt.figure(plt.figure(figsize=(8,5)), facecolor="black")

    plt.pie(
    data.values,
    labels=data.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=colors,
    textprops={"color": "white", "fontsize": 12},
    wedgeprops={"edgecolor": "white", "linewidth": 2}
)

    plt.title(
    "Revenue by Product Category",
    fontsize=14,
    color="white",
    fontweight="bold",
    pad=15
)

    plt.gca().set_facecolor("black")   # Pie chart background black
    plt.axis("equal")                  # Perfect circle

    st.pyplot(plt)
    # graph3
   

    fig = px.sunburst(
    df,
    path=["Product_Category", "Sub_Category", "Product"],
    values="Revenue",
    color="Revenue",
    color_continuous_scale="Turbo",
    title="Revenue by Category, Sub-Category and Product"
)

    fig.update_layout(
    width=900,          # Width increase
    height=700, 
    paper_bgcolor="black",
    plot_bgcolor="black",
    font=dict(color="white", size=14),
    title_font=dict(size=18),
    
)

    st.plotly_chart(fig, use_container_width=True)


# graph4
# corr = df[["Quantity", "Price", "Revenue"]].corr()

# fig = px.imshow(
#     corr,
#     text_auto=True,
#     title="Correlation Heatmap"
# )
# st.plotly_chart(fig, use_container_width=True)
    corr = df[
    [
        "Customer_Age",
        "Order_Quantity",
        "Unit_Cost",
        "Unit_Price",
        "Profit",
        "Cost",
        "Revenue"
    ]
]   .corr()

# Heatmap
    fig = px.imshow(
    corr,
    text_auto=".2f",
    color_continuous_scale="Blues",
    title="Correlation Heatmap"
)

    fig.update_layout(
    title_x=0.3,
    height=600
)

    st.plotly_chart(fig, use_container_width=True)   
# graph 5

    st.subheader("🏆 Top 10 Products by Order Quantity")

    top_products = (
    df.groupby("Product")["Order_Quantity"]
    .sum()
    .nlargest(10)
    .reset_index()
)

    colors = [
    "#00E5FF",  # Cyan
    "#FF6B6B",  # Red
    "#FFD93D",  # Yellow
    "#6BCB77",  # Green
    "#4D96FF",  # Blue
    "#C77DFF",  # Purple
    "#FF9F1C",  # Orange
    "#F72585",  # Pink
    "#2EC4B6",  # Teal
    "#A0E426"   # Lime
]

    fig = px.bar(
    top_products,
    x="Product",
    y="Order_Quantity",
    text="Order_Quantity",
    title="🏆 Top 10 Selling Products",
    color="Product",                 # Every bar gets a different color
    color_discrete_sequence=colors
)

    fig.update_traces(
    textposition="outside",
    marker_line_color="white",
    marker_line_width=1.5
)

    fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="black",
    plot_bgcolor="black",
    height=500,
    title_x=0.5,
    xaxis_tickangle=-30,
    showlegend=False,
    font=dict(color="white", size=12)
)

    st.plotly_chart(fig, use_container_width=True)
# garph6
    country = df.groupby("Country")["Order_Quantity"].sum().reset_index()

    fig = px.bar(
    country,
    x="Country",
    y="Order_Quantity",
    color="Country",
    color_discrete_sequence=px.colors.qualitative.Dark24,
    title="Orders by Country"
)

    fig.update_layout(template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)


elif menu == "Insights":

    st.title(" Insights")

    st.markdown("---")

    # ================= Top Performers =================

    st.subheader("🏆 Top Performers")

    best_product = df.groupby("Product")["Order_Quantity"].sum().idxmax()
    top_country = df.groupby("Country")["Revenue"].sum().idxmax()
    top_category = df.groupby("Product_Category")["Revenue"].sum().idxmax()

    st.success(f"🏆 Best Selling Product : {best_product}")
    st.info(f"🌍 Top Revenue Country : {top_country}")
    st.warning(f"🚴 Top Product Category : {top_category}")
    # ================= Key Insights =================
    st.markdown("---")
    st.markdown("---")
    st.subheader("📌 Key Insights")

    with st.expander("💰 Revenue Performance"):
        st.write("Total revenue indicates strong business growth and healthy sales performance.")

    with st.expander("🚴 Best Selling Category"):
        st.write("The Bikes category contributes the highest share of total revenue.")

    with st.expander("🌍 Top Performing Country"):
        st.write("The leading country generates the maximum number of orders and revenue.")

    with st.expander("📦 Customer Orders"):
        st.write("Orders are well distributed across multiple product categories.")

    with st.expander("📊 Business Overview"):
        st.write("The dashboard provides a quick overview of revenue, profit, orders, and customer trends.")





    st.markdown("---")

    st.subheader("🚀 Future Scope")

    st.markdown("""
    - Add real-time bike sales data for live monitoring.
    - Build sales forecasting using historical data.
    - Create an interactive dashboard with more filters.
    - Analyze customer buying behavior in greater detail.
    - Compare sales performance across different regions and bike categories.
    - Add inventory and profit analysis for better business decisions.
    """)

    st.markdown("---")

    st.subheader("📖 Conclusion")

    st.write("""
    The Bike Sales Data Analysis project provides a clear understanding of sales performance through data visualization and analysis.
    It identifies the best-selling bike categories, top-performing regions, customer purchasing patterns, and revenue trends.
    The dashboard helps businesses make informed decisions, improve sales strategies, and enhance overall business performance.
    This project demonstrates how data analysis can transform raw sales data into meaningful insights for better decision-making.
    """)
    st.markdown("---")




    

    