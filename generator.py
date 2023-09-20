from tqdm import tqdm


# Function to find valid neighbors of a word
def find_neighbors(word):
    neighbors = set()
    for i in range(len(word)):
        for char in "abcdefghijklmnopqrstuvwxyz":
            new_word = word[:i] + char + word[i + 1 :]
            if new_word != word and new_word in french_words:
                neighbors.add(new_word)
    for i in range(len(word) + 1):
        for char in "abcdefghijklmnopqrstuvwxyz":
            new_word = word[:i] + char + word[i:]
            if new_word in french_words:
                neighbors.add(new_word)
    for i in range(len(word)):
        new_word = word[:i] + word[i + 1 :]
        if new_word in french_words:
            neighbors.add(new_word)
    return neighbors


# Function to find the shortest word ladder using BFS
def find_word_ladder(start, target):
    visited = set()
    queue = [[start]]

    while queue:
        path = queue.pop(0)
        word = path[-1]

        print(f"Checking {word}")
        if word == target:
            return path

        if word not in visited:
            visited.add(word)
            neighbors = find_neighbors(word)
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None


if __name__ == "__main__":
    with open("francais.txt", "r", encoding="utf-8") as file:
        french_words = set(word.strip().lower() for word in file)

    # Input from the user
    start_word = input("Enter the starting word (not too long): ").strip().lower()
    target_word = input("Enter the target word: ").strip().lower()

    word_ladder = find_word_ladder(start_word, target_word)

    if word_ladder:
        print("Shortest Word Ladder:")
        print(" -> ".join(word_ladder))
    else:
        print("No word ladder found.")
