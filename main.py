import os, glob
import requests
import cohere
import frontmatter
from tqdm import tqdm
from txtai.embeddings import Embeddings
from txtai.pipeline import Extractor
from txtai.pipeline import Segmentation

co = cohere.Client('LgDUf4xw6b4FUI56YTK1RdIICmr1Y2kI3wHfMKsH')
embeddings = Embeddings({"path": "sentence-transformers/nli-mpnet-base-v2", "content": True, "objects": True})
segment = Segmentation(paragraphs=True)

def generateEmbeddings():
    path = './notes'
    uid = 0;
    for filename in tqdm(glob.glob(os.path.join(path, '*.md'))):
       with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in readonly mode
           note = frontmatter.load(f)

           for uid, text in enumerate(segment(note.content)):
               # Check if it has changed
               result = embeddings.search(f"SELECT id, text FROM txtai WHERE id = '{filename}-{uid}'", 1) 
               if(len(result) != 0):
                   if result[0]["text"] == text:
                       print(f"skipping {filename}-{uid} because no changes")
                       continue
              
               embeddings.upsert([(f"{filename}-{uid}", text, None)])

    embeddings.save("./embeddings")


print("Regenerate Embeddings? (y/n):")
res = input()

embeddings.load("./embeddings")

if(res == "y"):
    generateEmbeddings()

# Submits a series of prompts to the Hugging Face API.
# This call can easily be switched to use the OpenAI API (GPT-3), Cohere API or a library like langchain.
def cohere_api(prompts):
    print(prompts)
    response = co.generate(
      prompt=prompts[0],
    )
    print(response[0].text)
    return [response[0].text]

# Submits a series of prompts to the Hugging Face API.
# This call can easily be switched to use the OpenAI API (GPT-3), Cohere API or a library like langchain.
def hugging_face_api(prompts):
    API_URL = "https://api-inference.huggingface.co/models/google/distilbert-base-cased-distilled-squad"
    headers = {"Authorization": "Bearer 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"}
    response = requests.post(API_URL, headers=headers, json={"inputs": prompts})

    return [x["generated_text"] for x in response.json()]


# Initialize Extractor
# Create extractor instance
extractor = Extractor(embeddings, hugging_face_api, context=30)

def prompt(question):
  return f"""Answer the following question using only the context below. Say 'no answer' when the question can't be answered.
Question: {question}
Context: """

def search(query, question=None):
  # Default question to query if empty
  if not question:
    question = query

  return extractor([("answer", query, prompt(question), False)])[0][1]

while(True):
    print("(search) Enter query (press q to exit):")
    query = input()
    
    if query == "q":
        break

    print("------------------ GENERATIVE ANSWER -------------------")
    result = search(query)
    print(f'{query} : {result}')

    print("------------------ RELATED NOTES (SEMANTIC SEARCH) -------------------")
    for result in embeddings.search(query, 5):
        print(f'{result["id"]}:{result["score"]}')


