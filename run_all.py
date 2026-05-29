import os

FILES = [
    "01_env_setup.py",
    "02_imports.py",
    "03_fetch_transcript.py",
    "04_print_transcript_obj.py",
    "05_detect_and_translate.py",
    "06_split_chunks.py",
    "07_len_chunks.py",
    "08_chunks_60.py",
    "09_faiss_store.py",
    "10_index_to_docstore_id.py",
    "11_get_by_ids.py",
    "12_retriever.py",
    "13_retriever_display.py",
    "14_retriever_invoke.py",
    "15_llm.py",
    "16_prompt.py",
    "17_question.py",
    "18_retrieved_docs.py",
    "19_context_text.py",
    "20_final_prompt.py",
    "21_final_prompt_display.py",
    "22_answer.py",
]

base = os.path.join(os.path.dirname(__file__), "code")
g = {"__name__": "__main__"}

for name in FILES:
    path = os.path.join(base, name)
    with open(path, encoding="utf-8") as f:
        exec(f.read(), g)
