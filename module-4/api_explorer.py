import requests

# GET all users and print each user's name and email
print("=== All Users ===")
users = requests.get("https://jsonplaceholder.typicode.com/users")
users = users.json()
for user in users:
    print(f"User Name: {user['name']}")
    print(f"Username: {user['username']}")
    print(f"Email: {user['email']}")
    print()



# GET all posts by user #3 (use query parameters)
print("=== Posts by User #3 ===")
posts_by_user_3 = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 3}
)
posts_by_user_3 = posts_by_user_3.json()
for post in posts_by_user_3:
    print(f"Post Title: {post['title']}")
    print(f"Post Body: {post['body'][:80]}...")
    print()

# GET all comments on post #1 (endpoint: /posts/1/comments)
print("=== Comments on Post #1 ===")
comments_on_post_1 = requests.get("https://jsonplaceholder.typicode.com/posts/1/comments")
comments_on_post_1 = comments_on_post_1.json()
for comment in comments_on_post_1:
    print(f"Comment Name: {comment['name']}")
    print(f"Comment Email: {comment['email']}")
    print(f"Comment Body: {comment['body'][:80]}...")
    print()

# POST a new post and print the response
print("=== Creating a New Post ===")
new_post = {
    "title": "My New Post",
    "body": "This is the body of my new post.",
    "userId": 1
}
response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post
)
created_post = response.json()
print(f"Created Post ID: {created_post['id']}")
print(f"Created Post Title: {created_post['title']}")
print(f"Created Post Body: {created_post['body'][:80]}...")
print(f"Author (userId): {created_post['userId']}")