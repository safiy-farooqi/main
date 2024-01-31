# WORDLE


"""Ex03 wordle program."""

def contains_char(string_to_search: str, char_to_search: str) -> bool:
    """Searches at all indexes of a word for a given char."""
    assert len(char_to_search) == 1

    i = 0
    while i < len(string_to_search):
        if string_to_search[i] == char_to_search:
            return True
        i += 1
    return False


def emojified(guess_string: str, secret_string: str) -> str:
    """String of emojis of yellow or white box."""
    assert len(guess_string) == len(secret_string)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index = 0
    emoji = ""
    while index < len(guess_string):
        if guess_string[index] == secret_string[index]:
            emoji += GREEN_BOX
        elif contains_char(secret_string, guess_string[index]): 
            emoji += YELLOW_BOX
        else: 
            emoji += WHITE_BOX
        index += 1
    return emoji


def input_guess(expected_length: int) -> str:
    """Asks user for x-character word."""
    user_input: str = input(f"Enter a {(expected_length)} character word: ")

    while len(user_input) != expected_length:
        user_input = input(f"That wasn't {(expected_length)} chars! Try again: ")
    return user_input


def main() -> None:
    """Wordle EX03."""
    max_turns = 6
    turn_number = 0
    secret_word = "codes"
    guess = ""
    while turn_number < max_turns and guess != secret_word:
        turn_number += 1 
        print(f"=== Turn {turn_number}/{max_turns} ===")
        guess = input_guess(len(secret_word))
        result_emoji = emojified(guess, secret_word)
        print(result_emoji)

    if guess == secret_word:
        print(f"You won in {turn_number}/{max_turns} turns!")
    else:
        print(f"X/{max_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
