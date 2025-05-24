from openai import OpenAI
from dotenv import load_dotenv
import os
import openai

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

model = "gpt-3.5-turbo"

def load_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return content
    except IOError as e:
        print(f"Error loading file: {e}")

def save_file(file_name, content):
    try:
        with open(file_name, 'w', encoding="utf-8") as file:
            file.write(content)
    except IOError as e:
        print(f"Error saving file: {e}")

def sentiment_analysis(product_name):
    system_prompt = """
    You are a sentiment analyzer of product reviews.
    Write a paragraph of up to 50 words summarizing the reviews and
    then assign the overall sentiment to the product.
    Also identify 3 strengths and 3 weaknesses identified from the reviews.

    # Output Format

    Product Name:
    Review Summary:
    Overall Sentiment: [use only Positive, Negative or Neutral here]
    Strengths: 3 bullet list
    Weaknesses: 3 bullet list
    """

    user_prompt = load_file(f"Alura\GPT Python criando ferramentas com API\GPT - Sentiment analyzer\\data\\reviews-{product_name}.txt")
    print(f"Starting sentiment analysis for the product: {product_name}")

    messages_list = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    try:
        response = client.chat.completions.create(messages=messages_list, model=model)

        response_text = response.choices[0].message.content
        save_file(f"Alura\GPT Python criando ferramentas com API\GPT - Sentiment analyzer\\data\\sentiment analysis-{product_name}.txt", response_text)
    except openai.AuthenticationError as e:
        print(f"Authentication error: {e}")
    except openai.APIError as e:
        print(f"API error: {e}")

sentiment_analysis("Mineral makeup")
