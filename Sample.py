import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

# Sample Pie Chart Data
df = pd.DataFrame({"Category": ["Our Action", "Our Results"], "Percentage": [20, 80]})

# Unemployment Data
years = [2018, 2019, 2020, 2021, 2022, 2023]
unemployment_rate = [14.0, 13.5, 17.1, 16.4, 15.9, 16.7]

# Generate Matplotlib Plot as Image
def create_unemployment_plot():
    fig, ax = plt.subplots(figsize=(4, 3))
    sns.lineplot(x=years, y=unemployment_rate, marker="o", color="red", ax=ax)
    ax.set(title="Unemployment Rate in Rwanda (2018-2023)", xlabel="Year", ylabel="Rate (%)", ylim=(10, 20))
    ax.grid(True)
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png", bbox_inches="tight")
    buffer.seek(0)
    return f"data:image/png;base64,{base64.b64encode(buffer.getvalue()).decode()}"

# Create Dash application
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Do You Need Assistance?", style={'text-align': 'center'}),
    html.H3("We do it Right Now", style={'text-align': 'center'}),

    # All Three Outputs in One Line
    html.Div([
        # "Reach Out for Help" (Left)
        html.Div([
            html.H3("Reach Out for Help", style={'text-align': 'center'}),
            html.Ul([
                html.Li("📧 Email: faustin@tuta.io"),
                html.Li("📞 WhatsApp: +250784885925")
            ], style={'text-align': 'center', 'list-style-type': 'none', 'padding': 0}),

            html.H3("Services", style={'text-align': 'center', 'text-decoration': 'underline'}),
            html.Ul([
                html.Li("📊 Survey Design & Demographic Research"),
                html.Li("📈 Data Analysis & Visualization"),
                html.Li("🤖 Training & Consulting Services")
            ], style={'text-align': 'center', 'list-style-type': 'none', 'padding': 0})
        ], style={'flex': '1', 'border': '2px solid black', 'padding': '4px', 'margin': '4px', 'box-sizing': 'border-box'}),

        # Pie Chart (Middle)
        html.Div([
            dcc.Graph(
                id='pie-chart',
                figure=px.pie(df, names="Category", values="Percentage", title="Our Actions Impact Results"),
                style={"height": "100%", "width": "100%"}
            )
        ], style={'flex': '1', 'border': '2px solid black', 'padding': '4px', 'margin': '4px', 'box-sizing': 'border-box', 'text-align': 'center'}),

        # Unemployment Rate Chart (Right)
        html.Div([
            html.H2("Rwanda Unemployment Rate (2018-2023)", style={'text-align': 'center'}),
            html.Img(src=create_unemployment_plot(), style={"width": "100%", "border": "2px solid black"})
        ], style={'flex': '1', 'text-align': 'center', 'box-sizing': 'border-box'}),
    
    ], style={'display': 'flex', 'flex-wrap': 'wrap', 'justify-content': 'space-between', 'width': '100%', 'box-sizing': 'border-box'}),  
])

if __name__ == '__main__':
    app.run_server(debug=True)
