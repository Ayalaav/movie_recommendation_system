import pandas as pd # For data manipulation and analysis.
import numpy as np # For numerical operations.
import matplotlib.pyplot as plt # For  visualization.
import seaborn as sns # For  visualization.
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
ratings_df = pd.read_csv('movies.csv')

#########################
# # Display the first few rows of the dataset
# print("First 5 rows of the dataset:")
# print(ratings_df.head())
#
# # Check the shape of the dataset
# print("\nShape of the dataset:")
# print(ratings_df.shape)
#
# # Check basic info about the dataset
# print("\nDataset Info:")
# ratings_df.info()
#
# # Check for missing values
# print("\nMissing Values:")
# print(ratings_df.isnull().sum())
#
# print("\nNumber of unique users:", ratings_df['User_ID'].nunique())
# print("Number of unique movies:", ratings_df['Movie_ID'].nunique())
#
# print("\nDataset Statistics:")
# print(ratings_df.describe())

#########################

# Create a User-Item Matrix
user_item_matrix = ratings_df.pivot_table(index='User_ID', columns='Movie_Title', values='Rating')
# print(user_item_matrix.head())

user_item_matrix.fillna(0, inplace=True)  # Filling missing values with 0 (no rating)

#########################
# # Set pandas options to display the full DataFrame
# pd.set_option('display.max_rows', None)  # Show all rows
# pd.set_option('display.max_columns', None)  # Show all columns
# pd.set_option('display.width', None)  # Ensure the output fits the console width
# pd.set_option('display.max_colwidth', None)  # Ensure columns are not truncated
#
# # Now print the full user_item_matrix
# print(user_item_matrix)
#########################

# Compute the similarity matrix
cosine_sim = cosine_similarity(user_item_matrix.T)  # .T to transpose and compute similarity between movies

# Creates another table only with a similarity score between the movies, for example the similarity between movie A and movie B is 0.8 following the preference result
cosine_sim_df = pd.DataFrame(cosine_sim, index=user_item_matrix.columns, columns=user_item_matrix.columns)
# print(cosine_sim_df.head())


# Make Recommendations
def get_movie_recommendations(movie_name, cosine_sim_df, top_n=5):
    # Get the pairwise similarity scores for the given movie
    sim_scores = cosine_sim_df[movie_name]

    # Sort the movies based on similarity scores (in descending order)
    sim_scores = sim_scores.sort_values(ascending=False)

    # Get the top N movie recommendations (excluding the movie itself)
    sim_scores = sim_scores.drop(movie_name)

    # Return the top N similar movies
    return sim_scores.head(top_n)


# Example: Get top 3 similar movies to "Movie A"
recommended_movies = get_movie_recommendations('To Kill a Mockingbird', cosine_sim_df, top_n=3)
print(recommended_movies)


