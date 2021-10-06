# Import the required modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the csv file into dataframe 'df'
df = pd.read_csv(filepath_or_buffer = "https://github.com/whjr2021/DV-with-Python/blob/main/SA1_covid_vaccinations.csv?raw=true")

# Print the dataset and observe the values
print(df)

# Extract the columns 'Country' and 'Fully_Vaccinated' from dataframe 'df' 
country_name = df['Country']
fully_vaccinated = df['Fully_Vaccinated']
# Extract the column 'Partly_Vaccinated' from  dataframe 'df' and store in 'partly_vaccianated' 
partly_vaccianated = df['Partly_Vaccinated']

# Set values for x-axis
bar_1 = np.arange(len(country_name))

# Set the figsize
plt.figure(figsize = (16, 9))

# Plot the bar graphs for share of people fully vaccinated against COVID-19
plt.barh(y = country_name, width = fully_vaccinated, label = 'Fully Vaccinated (Both doses administered)')

# Plot the bar graphs for share of people only partly vaccinated against COVID-19
plt.barh(y = country_name, width = partly_vaccianated, label = 'Partly Vaccianated (One dose administered)')

# Set the title of the graph
plt.title("Share of people vaccinated against COVID-19 in top 10 countries with highest population")

# Set the labels for x and y-axes
plt.xlabel("Share of vaccinated population in %")
plt.ylabel("Country")

# Show labels with legend
plt.legend()

# Display the graph
plt.show()