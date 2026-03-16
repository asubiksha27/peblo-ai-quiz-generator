def adjust_difficulty(current, correct):

    if correct:
        if current == "easy":
            return "medium"
        if current == "medium":
            return "hard"
    else:
        if current == "hard":
            return "medium"
        if current == "medium":
            return "easy"

    return current