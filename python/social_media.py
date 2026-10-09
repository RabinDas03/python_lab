def analyze_likes():
  raw_input = input("Enter likes for 5 posts separated by spaces: ")
  likes = [int(x) for x in raw_input.split()]
  if not likes:
    print("No likes entered.\n")
    return

  highest_likes = max(likes)
  total_likes = sum(likes)
  popular_posts = [l for l in likes if l >= 100]
  print(
      f"Highest Likes: {highest_likes}\nTotal Likes: {total_likes}\nPosts with >="
      f" 100 likes: {popular_posts}\n"
  )

if __name__ == "__main__":
  analyze_likes()
