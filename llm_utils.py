import os
from dotenv import load_dotenv
import google.generativeai as genai
import configparser

# Load environment variables
load_dotenv()

# Load configuration from config.ini
config = configparser.ConfigParser()
config.read("config.ini")

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Read config values
MODEL_NAME = config["DEFAULT"]["gemini_model"]
TRUNCATE_CHARS = int(config["DEFAULT"]["truncate_chars"])


def format_user_data(user_data):
    def format_posts(posts):
        formatted = ""
        for post in posts:
            formatted += f"[Post] Title: {post['title']}\nText: {post['selftext']}\nLink: {post['permalink']}\n\n"
        return formatted.strip()

    def format_comments(comments):
        formatted = ""
        for comment in comments:
            formatted += f"[Comment] On Post: {comment['submission_title']}\nComment: {comment['body']}\nLink: {comment['permalink']}\n\n"
        return formatted.strip()

    return f"""
--- Reddit Posts ---
{format_posts(user_data['posts'])}

--- Reddit Comments ---
{format_comments(user_data['comments'])}
    """


def generate_persona_from_data(user_data):
    print("[🧠] Calling Gemini to generate persona...")

    formatted_content = format_user_data(user_data)

    if len(formatted_content) > TRUNCATE_CHARS:
        print(f"[⚠️] Truncating Reddit content to {TRUNCATE_CHARS} characters to stay within Gemini token limits.")
        formatted_content = formatted_content[:TRUNCATE_CHARS]

    prompt = f"""
You are a psychological profiling assistant trained to infer accurate user personas from Reddit content.

Below is a Reddit user's content (posts and comments). Your task is to generate a user persona with specific attributes.

For each attribute, provide:
1. A trait or interest
2. A quote that supports your inference (copied exactly from the user's content)
3. A direct Reddit permalink to the post or comment that contains that quote

👉 Format your response in a Markdown table like this:

| Trait/Inference | Supporting Quote | Reddit Link |
|------------------|------------------|-------------|
| Interested in gaming | "Just finished playing the new Elden Ring DLC!" | https://www.reddit.com/r/gaming/comments/xyz123/comment/abcde/ |

---

Reddit Content:
{formatted_content}
    """

    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        print(f"[❌] Gemini Error: {e}")
        return "Error: Could not generate persona."
