import seaborn as sns
import plotly.graph_objects as go
from featureengineering import feature_engineering

def data_visualization():
    dataset = feature_engineering()
    # Candlestick chart
    fig = go.Figure(data=[go.Candlestick(x=dataset['date_parsed'],
                    open=dataset['Open'],
                    high=dataset['High'],
                    low=dataset['Low'],
                    close=dataset['Close'])])
    fig.show()
    
    # KDE plot for Volume
    sns.kdeplot(dataset['Volume'])
    
    # Scatter plot of Gold Price and Euro Price
    fig_scatter = go.Figure(data=go.Scatter(x=dataset['EU_Price'],
                                        y=dataset['Close'],
                                        mode='markers',
                                        marker=dict(color='blue')))
    fig_scatter.update_layout(title='Gold Price vs. Euro Price', xaxis_title='Euro Price', yaxis_title='Gold Price')
    fig_scatter.show()
    
    return dataset
data_visualization()
