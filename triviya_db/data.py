import requests as rq

parameters = {
    "amount": "10",
    "type": "boolean"
}

# response = rq.get(url="https://opentdb.com/api.php", params=parameters)
# response.raise_for_status()
# data = response.json()
question_data = [
    {
      "category": "Entertainment: Video Games",
      "type": "boolean",
      "difficulty": "easy",
      "question": "The name of the main character of the video game &quot;The Legend of Zelda&quot;, is Zelda.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "Entertainment: Film",
      "type": "boolean",
      "difficulty": "easy",
      "question": "The film &quot;2001: A Space Odyssey&quot; was released on December 31st, 2000.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "Politics",
      "type": "boolean",
      "difficulty": "easy",
      "question": "In 2016, the United Kingdom voted to stay in the EU.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "History",
      "type": "boolean",
      "difficulty": "medium",
      "question": "Abraham Lincoln was the first U.S. President to be born outside the borders of the thirteen original states. ",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Entertainment: Comics",
      "type": "boolean",
      "difficulty": "easy",
      "question": "The &quot;Pepe&quot; meme originated from a comic drawn by Matt Furie called &quot;Boy&#039;s Club&quot;?",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "medium",
      "question": "Albert Einstein had trouble with mathematics when he was in school.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "Mythology",
      "type": "boolean",
      "difficulty": "easy",
      "question": "According to Greek Mythology, Atlas was an Olympian God.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "Science & Nature",
      "type": "boolean",
      "difficulty": "hard",
      "question": "The chemical element Lithium is named after the country of Lithuania.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "Entertainment: Cartoon & Animations",
      "type": "boolean",
      "difficulty": "medium",
      "question": "Snagglepuss was part of the Yogi Yahooies in the 1977 show Scooby&#039;s All-Star Laff-a-Lympics.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "medium",
      "question": "&quot;Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo.&quot; is a grammatically correct sentence.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    }
  ]
