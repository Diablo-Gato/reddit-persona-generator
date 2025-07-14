```markdown
# Reddit Persona Generator

This project scrapes Reddit activity from a given public user profile and generates a psychological persona based on their posts and comments. Each inferred trait is supported with a direct quote and a citation link to the original Reddit content.

The persona generation is performed using Gemini (Google Generative AI), and the tool is designed to be modular, extensible, and production-ready.

## Features

-   Reddit user scraping using the PRAW API (posts and comments)
-   Trait extraction using prompt-engineered Gemini LLM calls
-   Citation support: each trait includes a quote and direct Reddit link
-   Output saved as structured Markdown tables
-   Built with environment security and API token management in mind

## Project Structure

```

reddit-persona-generator/
├── main.py              \# CLI entry point
├── scrapper.py          \# Reddit data collection
├── llm\_utils.py         \# LLM prompt and response handling
├── config.ini           \# Configurable parameters (model, limits)
├── .env.example         \# Environment variable template
├── .gitignore           \# Files/directories excluded from version control
├── requirements.txt     \# Python dependencies
├── README.md            \# Project overview and documentation
└── output/              \# Generated persona outputs

````

## Setup Instructions

### 1. Clone the repository

```bash
git clone [https://github.com/Diablo-Gato/reddit-persona-generator.git](https://github.com/Diablo-Gato/reddit-persona-generator.git)
cd reddit-persona-generator
````

### 2\. Create a virtual environment and activate it

```bash
python -m venv venv
```

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 3\. Install dependencies

```bash
pip install -r requirements.txt
```

### 4\. Set up environment variables

Create a `.env` file using the provided `.env.example` as a template:

```
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
GEMINI_API_KEY=your_gemini_api_key
```

You can obtain these from:

  * **Reddit API**: `https://www.reddit.com/prefs/apps`
  * **Gemini API**: `https://aistudio.google.com/app/apikey`

### 5\. Configure model and limits (optional)

Edit `config.ini` to adjust:

```ini
[DEFAULT]
gemini_model = models/gemini-1.5-flash-002 # Updated to reflect your chosen model
truncate_chars = 5000
output_folder = output
```

## Usage

To generate a persona:

```bash
python main.py [https://www.reddit.com/user/USERNAME/](https://www.reddit.com/user/USERNAME/)
```

Replace `USERNAME` with any public Reddit username. The script will:

  * Scrape the user’s posts and comments
  * Pass them to Gemini for analysis
  * Generate a Markdown table of inferred traits
  * Save the output to `output/USERNAME_persona.txt`

## Example Output

The persona is generated in this format:

| Trait/Inference | Supporting Quote | Reddit Link |
|---|---|---|
| Interested in gaming | "Just finished playing the new Elden Ring DLC\!" | `https://www.reddit.com/r/gaming/comments/...` |
| Uses formal tone | "In conclusion, I believe the hypothesis stands." | `https://www.reddit.com/r/science/comments/...` |

## Notes

  * Only public Reddit profiles can be analyzed.
  * The Gemini LLM has token limits; long histories are truncated.
  * Quotes and links are programmatically validated when possible.
  * This tool is for educational and evaluative purposes only.

## License

MIT License

## Author

Priya

GitHub: `https://github.com/Diablo-Gato`

```
```