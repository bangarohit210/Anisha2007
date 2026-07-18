import pandas as pd
# import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns


st.sidebar.markdown("🚴Bike Sales Data Analysis")
menu = st.sidebar.radio("Navigation",( "🏠 Home","📊 Data Overview","📈 Revenue Analysis" , "📉 Data Visualizations", ))
try:
    df=pd.read_csv("sales_data.csv")
except:
    st.error("Dataset file not found")
    st.stop()

if menu=="🏠 Home":
    st.title("🚴Bike Sales Data Analysis")
    st.markdown("The Bike Sales Data Analysis project is a Data Science dashboard that analyzes bike sales data to provide valuable business insights. It helps users understand sales performance, revenue trends, customer behavior, product categories, and regional sales through interactive charts and visualizations. The dashboard is developed using Python, Pandas, Plotly, and Streamlit to make data analysis simple, clear, and interactive.")
    col1,col2=st.columns(2)
    with col1:
        st.image("bike3.jpg",width=300)
    with col2:
        st.image("bike2.jpg",width=280)
elif menu=="📊 Data Overview":
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

    st.subheader("Data Cleaning")
    col1,col2=st.columns(2)
    with col1:
        st.subheader("Missing values")
        missing=df.isnull().sum()
        st.dataframe(missing[missing > 0], width="stretch")

elif menu == "📈 Revenue Analysis":

    st.title("📈 Revenue Analysis")

    st.write("""
    Welcome to the Revenue Analysis section.
    Here you can explore bike sales performance, revenue trends,
    product-wise sales, and customer insights.
    """)
# graph1
    # st.subheader("Monthly Revenue Analysis")
    # monthly_revenue = df.groupby("Month")["Revenue"].sum()

    # plt.figure(figsize=(8,5))
    # plt.plot(monthly_revenue.index,
    #          monthly_revenue.values,
    #          marker="o")

    # plt.title("Monthly Revenue")
    # plt.xlabel("Month")
    # plt.ylabel("Revenue")
    # plt.grid(True)
    # plt.xticks(rotation=45)

    # st.pyplot(plt)
    st.subheader("📈 Monthly Revenue Analysis")

    monthly_revenue = df.groupby("Month")["Revenue"].sum()

    plt.figure(figsize=(8,5), facecolor="black")
    ax = plt.gca()
    ax.set_facecolor("black")

    plt.plot(
    monthly_revenue.index,
    monthly_revenue.values,
    color="cyan",
    marker="o",
    markersize=8,
    linewidth=3
)

    plt.title("Monthly Revenue", color="white", fontsize=15)
    plt.xlabel("Month", color="white")
    plt.ylabel("Revenue", color="white")

    plt.xticks(rotation=45, color="white")
    plt.yticks(color="white")

    plt.grid(color="gray", linestyle="--", alpha=0.4)

# White border
    for spine in ax.spines.values():
        spine.set_color("white")

    st.pyplot(plt)



#graph2
#
    st.subheader("Revenue by Product Category")

    category_revenue = df.groupby("Product_Category")["Revenue"].sum()

    colors = ["red", "blue", "green", "orange", "purple", "cyan", "yellow"]

    plt.figure(figsize=(8,6), facecolor="black")
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
  
#  graph3
    st.subheader("📅 Yearly Revenue Analysis")

    data = df.groupby("Year")["Revenue"].sum()

    plt.figure(figsize=(6,4))

    plt.bar(
    data.index.astype(str),
    data.values,
    color="royalblue",
    edgecolor="black",
    linewidth=1,
    width=0.5
)

    plt.title("Yearly Revenue", fontsize=14, fontweight="bold")
    plt.xlabel("Year")
    plt.ylabel("Revenue")
    plt.grid(axis="y", linestyle="--", alpha=0.4)

    plt.tight_layout()

    st.pyplot(plt)
    # graph4
    st.subheader("🌍 Revenue by Country")

    data = df.groupby("Country")["Revenue"].sum()

    plt.figure(figsize=(7,4))
    plt.bar(data.index, data.values,
            color="orange", edgecolor="black")

    plt.title("Revenue by Country")
    plt.xticks(rotation=45)

    st.pyplot(plt)

# elif menu=="📉 Data Visualizations":
#     st.title("📉 Data Visualizations")
#     st.write("This page displays charts and graphs for visual analysis of the Bike Sales dataset.")

# # graph1
#     # plt.figure(figsize=(8,5))

#     # plt.hist(df["Customer_Age"], bins=10,rwidth=0.8)

#     # plt.title("Customer Age Distribution", pad=15)
#     # plt.xlabel("Customer Age", labelpad=10)
#     # plt.ylabel("Count", labelpad=10)

#     # plt.tight_layout()   # Graph ke around space adjust karega
#     # st.pyplot(plt)
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
#     # garph2

#     data = df.groupby("Product_Category")["Revenue"].sum()

#     colors = ["#00C853", "#2979FF", "#FFD600"]   # Green, Blue, Yellow

#     plt.figure(figsize=(8,6), facecolor="black")

#     plt.pie(
#     data.values,
#     labels=data.index,
#     autopct="%1.1f%%",
#     startangle=90,
#     colors=colors,
#     textprops={"color": "white", "fontsize": 12},
#     wedgeprops={"edgecolor": "white", "linewidth": 2}
# )

#     plt.title(
#     "Revenue by Product Category",
#     fontsize=14,
#     color="white",
#     fontweight="bold",
#     pad=15
# )

#     plt.gca().set_facecolor("black")   # Pie chart background black
#     plt.axis("equal")                  # Perfect circle

#     st.pyplot(plt)
#     # graph3
   

# fig = px.sunburst(
#     df,
#     path=["Product_Category", "Sub_Category", "Product"],
#     values="Revenue",
#     color="Revenue",
#     color_continuous_scale="Turbo",
#     title="Revenue by Category, Sub-Category and Product"
# )

# fig.update_layout(
#     width=900,          # Width increase
#     height=700, 
#     paper_bgcolor="black",
#     plot_bgcolor="black",
#     font=dict(color="white", size=14),
#     title_font=dict(size=18),
    
# )

# st.plotly_chart(fig, use_container_width=True)


# # graph4
# # corr = df[["Quantity", "Price", "Revenue"]].corr()

# # fig = px.imshow(
# #     corr,
# #     text_auto=True,
# #     title="Correlation Heatmap"
# # )
# # st.plotly_chart(fig, use_container_width=True)

# corr = df[
#     [
#         "Customer_Age",
#         "Order_Quantity",
#         "Unit_Cost",
#         "Unit_Price",
#         "Profit",
#         "Cost",
#         "Revenue"
#     ]
# ].corr()

# # Heatmap
# fig = px.imshow(
#     corr,
#     text_auto=".2f",
#     color_continuous_scale="Blues",
#     title="Correlation Heatmap"
# )

# fig.update_layout(
#     title_x=0.3,
#     height=600
# )

# st.plotly_chart(fig, use_container_width=True)  

