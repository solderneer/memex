import os, glob
import requests
import frontmatter
from tqdm import tqdm
from txtai.embeddings import Embeddings
from txtai.pipeline import Extractor
from txtai.pipeline import Segmentation

class Index():
    def __init__(self, embeddingsPath, rootPaths):
        self.embeddings = Embeddings({"path": "sentence-transformers/nli-mpnet-base-v2", "content": True, "objects": True})
        # self.segment = Segmentation(paragraphs=True)
        self.embeddingsPath = embeddingsPath
        self.rootPaths = rootPaths

        # Load in the embeddings
        if os.path.exists(embeddingsPath):
            self.embeddings.load(embeddingsPath)

    def find_markdown_files(self):
        mdFiles = []
        for rootPath in self.rootPaths:
            for dirpath, dirnames, filenames in os.walk(rootPath):
                for filename in filenames:
                    if filename.endswith('.md'):
                        mdFiles.append(os.path.join(dirpath, filename))
        return mdFiles

    def refresh(self):
        mdFiles = self.find_markdown_files()

        # Status
        total = len(mdFiles)
        skipped = 0
        error = []

        for file in tqdm(mdFiles):
           with open(file, 'r') as f: # open in readonly mode
               note = None
               try:
                   note = frontmatter.load(f)
               except:
                   error.append(file)
                   continue

               text = note.content

               result = self.embeddings.search(f"SELECT id, text FROM txtai WHERE id = '{file}'", 1) 
               if len(result) != 0:
                   if result[0]["text"] == text:
                       skipped += 1
                       continue

               self.embeddings.upsert([(f"{file}", text, None)])

               # for uid, text in enumerate(self.segment(note.content)):
               #     # Check if it has changed
               #     result = self.embeddings.search(f"SELECT id, text FROM txtai WHERE id = '{filename}-{uid}'", 1) 
               #     if(len(result) != 0):
               #         if result[0]["text"] == text:
               #             print(f"skipping {filename}-{uid} because no changes")
               #             continue
               #    
               #     self.embeddings.upsert([(f"{filename}-{uid}", text, None)])
               #      
        self.embeddings.save(self.embeddingsPath)

        return (total, skipped, error)

    def search(self, query, limit):
        return self.embeddings.search(query, limit)

# # Submits a series of prompts to the Hugging Face API.
# # This call can easily be switched to use the OpenAI API (GPT-3), Cohere API or a library like langchain.
# def cohere_api(prompts):
#     print(prompts)
#     response = co.generate(
#       prompt=prompts[0],
#     )
#     print(response[0].text)
#     return [response[0].text]
# 
# # Submits a series of prompts to the Hugging Face API.
# # This call can easily be switched to use the OpenAI API (GPT-3), Cohere API or a library like langchain.
# def hugging_face_api(prompts):
#     API_URL = "https://api-inference.huggingface.co/models/google/distilbert-base-cased-distilled-squad"
#     headers = {"Authorization": "Bearer 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"}
#     response = requests.post(API_URL, headers=headers, json={"inputs": prompts})
# 
#     return [x["generated_text"] for x in response.json()]
# 
# 
# # Initialize Extractor
# # Create extractor instance
# extractor = Extractor(embeddings, hugging_face_api, context=30)
# 
# def prompt(question):
#   return f"""Answer the following question using only the context below. Say 'no answer' when the question can't be answered.
# Question: {question}
# Context: """
# 
# def search(query, question=None):
#   # Default question to query if empty
#   if not question:
#     question = query
# 
#   return extractor([("answer", query, prompt(question), False)])[0][1]
# 
# while(True):
#     print("(search) Enter query (press q to exit):")
#     query = input()
#     
#     if query == "q":
#         break
# 
#     print("------------------ GENERATIVE ANSWER -------------------")
#     result = search(query)
#     print(f'{query} : {result}')
# 
#     print("------------------ RELATED NOTES (SEMANTIC SEARCH) -------------------")
#     for result in embeddings.search(query, 5):
#         print(f'{result["id"]}:{result["score"]}')


if __name__ == "__main__":
    index = Index("./embeddings", ["./letters", "./notes", "./_private"])

    print("------------------ INDEXING -------------------")
    total, skipped, error = index.refresh()
    print(f'{total} files indexed | {skipped} files skipped | {len(error)} errors')
    print(f'Error Files: {error}')

    while(True):
        print("(search) Enter query (press q to exit):")
        query = input()
         
        if query == "q":
            break

        print("------------------ RELATED NOTES (SEMANTIC SEARCH) -------------------")
        for result in index.search(query, 5):
            print(f'{result["id"]}:{result["score"]}')


