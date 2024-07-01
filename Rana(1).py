import streamlit as st
import pandas as pd
import plotly.express as px

# Create a DataFrame
df = pd.read_excel('https://github.com/HeshamTay/Datasets/raw/main/List.xlsx')  # Check if the file path is correct

# Streamlit app
st.title('Shop Profit Visualization')

# Plot the map

def assign_category(sales):
    if sales == 0:
        return 'Not Active'
    elif int(sales) > 0 and int(sales) <= 1500:
        return 'Very Low'
    elif int(sales) > 1500 and int(sales) <= 3000:
        return 'Low'
    elif int(sales) > 3000 and int(sales) <= 5000:
        return 'Medium-Low'
    elif int(sales) > 5000 and int(sales) <= 10000:
        return 'Medium'
    elif int(sales) > 10000 and int(sales) <= 25000:
        return 'Medium-High'
    elif int(sales) > 25000 and int(sales) <= 50000:
        return 'High'
    else:
        return 'Very High'
 

df['Color'] = df['Sales'].apply(assign_category)

emirate = df['Emirate'].unique().tolist()
selected_emirate = st.multiselect('Select an Emirate', emirate)

# Filter the DataFrame based on the user's region selection
filtered_df = df[df['Emirate'].isin(selected_emirate)]

import plotly.express as px

fig = px.scatter_mapbox(
    filtered_df,
    lat="Latitude",
    lon="Longitude",
    color="Color",
    color_discrete_map={
        'Not Active': 'black',
        'Very Low': 'purple',
        'Low': 'navy',
        'Medium-Low': 'yellow',
        'Medium': 'grey',
        'Medium-High': 'green',
        'High': 'red',
        'Very High': 'pink'
    },
    hover_name="Name",
    hover_data={"Sales": True, "Phone": True},
    zoom=5,
    height=500,
    width=500
)


# Update layout with mapbox style
fig.update_layout(mapbox_style="carto-positron")

# Display the plot
st.plotly_chart(fig, use_container_width=True)
