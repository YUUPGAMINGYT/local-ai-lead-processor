import pandas as pd
import ollama

def generate_ai_pitches():
    print("Reading scraped data...")
    # Load the CSV we made in Project 1
    df = pd.read_csv("scraped_books_complete.csv")
    
    # We will only do the first 5 rows so it doesn't take hours on a laptop
    sample_df = df.head(5).copy()
    
    # Create a new column to store the AI's responses
    sample_df['AI_Email_Draft'] = ""

    print("Starting AI generation...")
    
    # Loop through each row and ask Ollama to write something
    for index, row in sample_df.iterrows():
        title = row['Title']
        price = row['Price']
        
        # The prompt we are sending to the AI
        prompt = f"Write a very short, 2-sentence marketing email convincing someone to buy the book '{title}' for {price}."
        
        print(f"Drafting email for: {title}...")
        
        # Call your local Ollama model
        response = ollama.chat(model='llama3', messages=[
            {
                'role': 'user',
                'content': prompt,
            },
        ])
        
        # Save the AI's answer back into the dataframe
        ai_text = response['message']['content']
        sample_df.at[index, 'AI_Email_Draft'] = ai_text

    # Save the new AI-enriched data to a new CSV
    sample_df.to_csv("ai_enriched_leads.csv", index=False)
    print("Done! Check ai_enriched_leads.csv for your AI drafts.")

generate_ai_pitches()