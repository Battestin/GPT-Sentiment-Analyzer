# GPT Sentiment Analyzer

Python tool for performing sentiment analysis on product reviews using OpenAI's GPT-3.5-turbo model. Generates summaries, overall sentiment ratings, and highlights pros and cons.

## 🚀 How to Run

1. Clone the repo  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Set your API key in a `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. Place the review text files in the `data` folder, following this naming convention:
   ```
   reviews-<product_name>.txt
   ```

5. Run the script:
   ```bash
   python gpt_sentiment_analyzer.py
   ```

## 🧠 What it Does

- Loads review texts for a list of products  
- Sends each batch to the GPT-3.5 model  
- Produces a structured output including:
  - A short summary
  - Overall sentiment (Positive, Neutral, Negative)
  - 3 strengths and 3 weaknesses
- Saves the results to `.txt` files

## ⚠️ Notes

- Handles basic API and authentication errors  
- You can customize the product list in the `main()` function  
- Review files must exist or the script will skip that product silently

## 📄 License

MIT
