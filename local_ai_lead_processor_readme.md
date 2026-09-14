# Local AI Lead Processor & Email Generator

An automated Python pipeline that reads scraped business data from a CSV, processes it through a local Large Language Model (LLM) via Ollama, and generates highly personalized marketing copy for each entry at zero API cost.

## 💼 Business Value
Writing customized cold outreach emails is incredibly time-consuming, but generic templates get flagged as spam. Connecting third-party AI APIs (like OpenAI) to process thousands of leads can quickly cost businesses hundreds of dollars. 

This script solves both problems by running the AI generation **locally**.
* **Zero API Costs:** By utilizing local LLMs (like Llama 3 or Mistral), you can process unlimited rows of data for free.
* **Data Privacy:** Sensitive lead data never leaves your local machine.
* **Mass Personalization:** Automatically turns raw scraped data (names, prices, product titles) into personalized, human-sounding outreach emails.

## ✨ Key Features
* **Pandas Integration:** Seamlessly ingests scraped CSV datasets and structures the output.
* **Local LLM Pipeline:** Uses the official Python `ollama` library to ping a background server for generation.
* **Automated Data Appending:** Creates a new column for the AI-generated drafts and exports a ready-to-use enriched `.csv`.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Data Processing:** [Pandas](https://pandas.pydata.org/)
* **Local AI:** [Ollama](https://ollama.com/) (Llama 3 / Mistral)

## 🚀 Installation & Setup

1. **Install Ollama:**
   Download and install Ollama from [their official website](https://ollama.com/). Once installed, open your terminal and pull a lightweight model:
   ```bash
   ollama run llama3
   ```

2. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/local-ai-lead-processor.git
   cd local-ai-lead-processor
   ```

3. **Install dependencies:**
   ```bash
   py -m pip install -r requirements.txt
   ```

## 💻 Usage

1. Ensure your source data (e.g., `scraped_books_complete.csv`) is in the root directory.
2. Ensure Ollama is running in the background.
3. Run the automation agent:

```bash
py ai_agent.py
```

The script will iterate through the data, query the local LLM, and generate an `ai_enriched_leads.csv` file containing the original data alongside the newly drafted AI emails.