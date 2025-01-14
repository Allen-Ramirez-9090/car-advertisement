import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset into a DataFrame
cars_df = pd.read_csv('vehicles_us.csv')

# Add a header
st.header("Car Advertisement Analysis Dashboard")

# Create and display the histogram of car prices (adjusted layout)
fig_hist = px.histogram(cars_df, x='price', nbins=40, title='Car Price Distribution', 
                         range_x=[0, cars_df['price'].max() * 0.95])  # Adjusted price range

# Update layout to remove slider and ensure the plot appears solid
fig_hist.update_layout(
    height=700,  # Make the plot taller by increasing height
    xaxis_title="Price",  # Add x-axis label for clarity
    margin=dict(t=50, b=150, l=50, r=50)  # Adjust margins to prevent overlap
)

# Display the histogram
st.plotly_chart(fig_hist)

# Create and display the scatter plot for price vs odometer (adjusted layout)
fig_scatter = px.scatter(cars_df, x='odometer', y='price', color='condition', 
                         title='Price vs Odometer (Mileage)', 
                         labels={'odometer': 'Odometer (miles)', 'price': 'Price'})

# Update layout to make the plot taller and adjust the x-axis labels
fig_scatter.update_layout(
    height=800,  # Make the plot taller by increasing height
    margin={"l": 50, "r": 50, "b": 100, "t": 50},  # Adjust margins to avoid label overlap
    xaxis_tickangle=-45  # Rotate the x-axis labels to avoid overlap
)

# Update the x and y axis labels to include commas for readability
fig_scatter.update_layout(
    xaxis=dict(
        tickformat=',',  # Use commas as thousand separators
        title='Odometer (miles)'
    ),
    yaxis=dict(
        tickformat=',',  # Use commas as thousand separators
        title='Price'
    )
)

# Display the scatter plot
st.plotly_chart(fig_scatter)
