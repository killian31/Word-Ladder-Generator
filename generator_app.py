from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


# Function to find valid neighbors of a word
def find_neighbors(word, french_words):
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
def find_word_ladder(start, target, french_words):
    visited = set()
    queue = [[start]]

    while queue:
        path = queue.pop(0)
        word = path[-1]

        if word == target:
            return path

        if word not in visited:
            visited.add(word)
            neighbors = find_neighbors(word, french_words)
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None


@app.route("/", methods=["GET", "POST"])
def word_ladder():
    if request.method == "POST":
        start_word = request.form["start_word"]
        target_word = request.form["target_word"]

        word_ladder = find_word_ladder(
            start_word.lower(), target_word.lower(), french_words
        )

        if word_ladder:
            return render_template("result.html", word_ladder=word_ladder)
        else:
            return render_template("result.html", error="No word ladder found.")

    return render_template("index.html")


@app.route("/play-again", methods=["POST"])
def play_again():
    return redirect(url_for("word_ladder"))


if __name__ == "__main__":
    # Load the list of French words from the "francais.txt" file
    with open("francais.txt", "r", encoding="utf-8") as file:
        french_words = set(word.strip().lower() for word in file)

    app.run(debug=True)
