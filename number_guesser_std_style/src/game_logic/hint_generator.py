def provide_hint(guess, target):
    """Provide a hint based on the guess and target number."""
    if guess < target:
        return "Try a higher number!"
    else:
        return "Try a lower number!"
    