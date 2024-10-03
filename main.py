import json
from difflib import get_close_matches


def load_intents(file_path: str) -> dict:
    with open(file_path, "r") as file:
        data: dict = json.load(file)
    return data


def save_intents(file_path: str, data: dict):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)


def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=2, cutoff=0.8)
    return matches[0] if matches else None


def get_answer_for_question(question: str, intents: dict) -> str | None:
    for q in intents["questions"]:
        if q["question"] == question:
            return q["answer"]


def chat_bot():
    intents: dict = load_intents("intents.json")

    while True:
        user_input: str = input("You:")

        if user_input.lower() == "quit":
            break

        best_match: str | None = find_best_match(
            user_input, [q["question"] for q in intents["questions"]]
        )

        if best_match:
            answer: str = get_answer_for_question(best_match, intents)
            print(f"Bot: {answer}")
        else:
            print("Bot: I don't know the answer. Can you teach me?")
            new_answer: str = input(
                "What should the bot answer to this (or you can type skip): "
            )

            if new_answer.lower() != "skip":
                intents["questions"].append(
                    {"question": user_input, "answer": new_answer}
                )

                save_intents("intents.json", intents)
                print("Bot: Thank you! I will keep this in mind")


if __name__ == "__main__":
    chat_bot()
