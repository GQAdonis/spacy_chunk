import spacy
from fastapi import FastAPI

# Load the spaCy model
nlp = spacy.load("en_core_web_trf")

# Example text
text = "Your long text goes here. It will be split into sentences or chunks."

# Define FastAPI app
app = FastAPI()

# Process the text
doc = nlp(text)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=7677)