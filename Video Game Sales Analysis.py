
# Import the modules required.
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset.
df = pd.read_csv("https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/video-games-sales/video-game-sales.csv")

# Get the dataset information.
df.info()

# 2. Treat Null Values

# Check for the null values in all the columns.
df.isnull().sum()

# Remove the rows/columns containing the null values.
df = df.dropna()

# Convert the data-type of the year values into integer values.
df["Year"] = df["Year"].astype(int)

# Find out the total number of units sold yearly across different regions and the world.
df_sales_yearly = df.groupby(by="Year").sum().iloc[:,1:]
df_sales_yearly

# Create the line plots for the total number of units sold yearly across different regions and the world.
for col in df_sales_yearly.columns:
  plt.figure(figsize=(30 ,10))
  plt.plot(df_sales_yearly.index, df_sales_yearly[col])
  plt.title(f"{col}")
  plt.show()

# In which year, the most number of games were sold globally and how many?
print(f"The max golbal sale is {df['Global_Sales'].max()} in year {df[df['Global_Sales'] == df['Global_Sales'].max()]['Year'][0]}")

# Find out the genre-wise total number of units sold across different regions and the world.
df_sales_genre = df.groupby(by="Genre").sum().iloc[:,2:]

# Create line plots for genre-wise total number of units sold across different regions and the world.
for col in df_sales_genre.columns:
  plt.figure(figsize=(30 ,10))
  plt.plot(df_sales_genre.index, df_sales_genre[col])
  plt.title(f"{col}")
  plt.show()


# What genre of video game is most popular in Japan in terms of the total number of units sold?
print(f"The genre of video game is most popular in Japan is {df[df['JP_Sales'] == df['JP_Sales'].max()]['Genre'][4]}")

# Genre-wise total number of units sold across different regions and the world in descending order.
df_sales_genre.sort_values(by=['Global_Sales'], ascending=False)

# Find out the publisher-wise total number of units sold across different regions and the world in the descending order.
df_sales_publisher = df.groupby(by="Publisher").sum().iloc[:,2:]
df_sales_publisher.sort_values(by=['Global_Sales'], ascending=False)

# Find out the platform-wise the total number of units sold across different regions and the world in the descending order.
df_sales_platform = df.groupby(by="Platform").sum().iloc[:,2:]
df_sales_platform.sort_values(by=['Global_Sales'], ascending=False)
