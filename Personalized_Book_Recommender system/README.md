## Recommender system 

Recommender systems or recommendation systems, are software engines designed to suggest items to users depending on previous likes, dislikes, interests, product engagement and interaction,etc.
Recommender systems keep users interested in the sites.

**Why Recommender Systems?**
 1. It increases sales
 2. To increase load on the system
 3. Increasing engagement and satisfaction

**Types of Recommender systems**
 1. **Popularity based recommender system**
      Concept: Recommends items that are most popular among users — typically those with the highest ratings, most purchases, or most views.
      Example: A streaming platform showing “Top 10 trending movies.
      Pros: Simple to implement, no need for user history.
      Cons: Lacks personalization — every user sees the same recommendations.
 3. **Content based recommender system**
      Concept: Recommends items similar to those the user has liked in the past, based on item features (keywords, genres, descriptions, etc.).
      Example: If a user watches several sci-fi movies, the system recommends other sci-fi titles.
      Pros: Personalized; works even for new users (if they’ve rated a few items).
      Cons: Limited to known preferences; can’t easily suggest items outside the user’s typical interests (“serendipity problem”).
 4. **Collaborative filtering system**
      Concept: Uses the behavior and preferences of many users to recommend items.
            User-based: Finds users with similar tastes and recommends what they liked.
            Item-based: Finds items that are liked by similar users.
      Example: “People who liked this also liked...” on e-commerce sites.
      Pros: Doesn’t require item features; captures collective trends.
      Cons: Suffers from the cold start problem (new users or items with no data).
 5. **Hybrid recommender system**
      Concept: Combines two or more recommendation techniques (e.g., collaborative + content-based) to improve accuracy.
      Example: Netflix uses both content features (movie genres, cast) and user behavior (ratings, watch history).
      Pros: Balances strengths and weaknesses of different methods; reduces cold start and bias issues.
      Cons: More complex to design and tune.

**How are these used in the project?** -

**Popularity Based Recommender system**-

Using the avg rating a book got from a user we will find the best book rank using that rank we will suggest that list of books to all universally.

**Collaborative filtering system** -

Based on the ratings given by different users we will try to find the similar books and recommend them based on the choice they make
Here, the cosine similarity algorithm is used to find similarity between books.

<img width="766" height="231" alt="image" src="https://github.com/user-attachments/assets/f23e5de5-1b4b-4530-bd35-feac5c6266e8" />


- For each book different user ratings are written as a vector and similarity between each books user vector is calculated using cosine similarity which is the cos value between the each vector. 

<img width="912" height="317" alt="image" src="https://github.com/user-attachments/assets/13ebdf5a-a4c8-4bed-b168-f812423a9df6" />



**Dataset Used:** 

Using Book Recomendation Dataset from kaggle. This dataset has 3 main Files: 1. Ratings 2. Books 3. Users

![WhatsApp Image 2025-10-17 at 17 14 51_78f99550](https://github.com/user-attachments/assets/256023df-2b8a-4b51-8fb6-f788926d0a0a)


Deployement:

The deployment consists of :
1. Data used section
2. Top 50 recommendations
3. 5 similar Book Recomendations
