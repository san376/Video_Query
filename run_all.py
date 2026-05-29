import os

FILES = [
    "01_env_setup.py",
    "02_imports.py",
    "03_fetch_transcript.py",
    "04_detect_and_translate.py",
    "05_split_chunks.py",
    "06_faiss_store.py",
    "07_index_to_docstore_id.py",
    "08_retriever.py",
    "09_retriever_invoke.py",
    "10_llm.py",
    "11_prompt.py",
    "12_question.py",
    "13_context_text.py",
    "14_final_prompt.py",
    "15_answer.py",
]

base = os.path.join(os.path.dirname(__file__), "code")
g = {"__name__": "__main__"}

for name in FILES:
    path = os.path.join(base, name)
    with open(path, encoding="utf-8") as f:
        exec(f.read(), g)
