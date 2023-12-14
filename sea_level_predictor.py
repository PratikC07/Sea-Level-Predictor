import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Load the data from epa-sea-level.csv
    df = pd.read_csv('epa-sea-level.csv')
  
    # Create a scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Sea Level Data')
  
    # Perform linear regression for the entire dataset
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
  
    # Create a line of best fit for the entire dataset
    line_x = range(df['Year'].min(), 2051)
    line_y = slope * line_x + intercept
    plt.plot(line_x, line_y, color='red', label='Best Fit Line (1880-2050)')
  
    # Filter data for the years 2000 and beyond
    recent_data = df[df['Year'] >= 2000]
  
    # Perform linear regression for the recent data
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
  
    # Create a line of best fit for the recent data
    line_x_recent = range(recent_data['Year'].min(), 2051)
    line_y_recent = slope_recent * line_x_recent + intercept_recent
    plt.plot(line_x_recent, line_y_recent, color='green', label='Best Fit Line (2000-2050)')
  
    # Set labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
  
    # Add legend
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
