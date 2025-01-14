import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset into a DataFrame
cars_df = pd.read_csv('vehicles_us.csv')

# Add a header
st.header("Car Advertisement Analysis Dashboard")

# Add a title and display the histogram of car prices (adjusted layout)
st.title("Car Price Distribution")
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

# Add the explanation text under the histogram
st.write("""
The car price distribution histogram reveals the frequency of car listings across different price ranges in the dataset. 
With the majority of prices concentrated in lower ranges, this indicates that most cars are listed at more affordable prices, 
while higher price ranges show fewer listings. This suggests a skewed distribution, where most cars are priced lower, 
and only a small portion of listings are in the higher price bracket. The plot provides valuable insights into the overall 
pricing trends within the dataset.
""")

# Add a title and display the scatter plot for price vs odometer (adjusted layout)
st.title("Price vs Odometer (Mileage) Scatter Plot")
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

# Add the explanation text under the scatter plot
st.write("""
The scatter plot of price versus odometer (mileage) with color coding based on car condition highlights the relationship 
between a vehicle's mileage and its price. Generally, higher-mileage cars tend to have lower prices, though exceptions exist, 
particularly with cars in better condition. This visualization provides insight into how both mileage and condition influence 
the pricing of cars in the dataset.
""")
