import numpy as np

def get_user_preferences(num_users, num_items):
    """ Prompt user to input preferences for each item """
    user_preferences = []
    print("Enter ratings for each item (from 1 to 5, or 0 if not rated):")
    for i in range(num_users):
        ratings = []
        for j in range(num_items):
            rating = int(input(f"Enter rating for Item {j + 1} for User {i + 1}: "))
            while rating < 0 or rating > 5:
                print("Please enter a rating between 0 and 5.")
                rating = int(input(f"Enter rating for Item {j + 1} for User {i + 1}: "))
            ratings.append(rating)
        user_preferences.append(ratings)
    return np.array(user_preferences)

def recommend_items(user_id, user_preferences, num_recommendations=3):
    """ Recommend items to a user based on collaborative filtering """
    # Calculate similarity with other users using cosine similarity
    similarities = []
    for i in range(user_preferences.shape[0]):
        if i != user_id:
            similarity = np.dot(user_preferences[user_id], user_preferences[i]) / (
                np.linalg.norm(user_preferences[user_id]) * np.linalg.norm(user_preferences[i])
            )
            similarities.append((i, similarity))
    
    # Sort by similarity and recommend items from most similar users
    similarities.sort(key=lambda x: x[1], reverse=True)
    
    # Gather recommended items
    recommendations = []
    for similar_user, similarity in similarities[:num_recommendations]:
        for item in range(user_preferences.shape[1]):
            if user_preferences[user_id][item] == 0 and user_preferences[similar_user][item] > 0:
                recommendations.append((item, user_preferences[similar_user][item]))
    
    # Sort recommendations by rating and return top recommendations
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations[:num_recommendations]

def main():
    # Get number of users and items from the user
    num_users = int(input("Enter number of users: "))
    num_items = int(input("Enter number of items: "))
    
    # Get user preferences matrix from user input
    user_preferences = get_user_preferences(num_users, num_items)
    
    # Example: Recommend items for a specified user
    user_id = int(input(f"Enter user ID (from 1 to {num_users}): ")) - 1
    recommendations = recommend_items(user_id, user_preferences)
    
    # Print recommendations
    print(f"\nRecommendations for User {user_id + 1}:")
    for item, rating in recommendations:
        print(f"Item {item + 1} with rating {rating}")

if __name__ == "__main__":
    main()
