import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from langchain.prompts import PromptTemplate

def generate_answer(query, chunks, model_name="vinai/bartpho-syllable"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    context = "\n".join([chunk for chunk, _ in chunks])
    prompt_template = PromptTemplate(
        input_variables=["context", "question"],
        template="Dựa trên thông tin sau:\n{context}\nTrả lời câu hỏi: {question}"
    )
    prompt = prompt_template.format(context=context, question=query)
    inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(
        inputs["input_ids"],
        max_length=100,
        num_beams=5,
        early_stopping=True
    )
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer

if __name__ == "__main__":
    from retriever.retrieve import retrieve
    query = "Hồ Chí Minh sinh ngày nào?"
    chunks = retrieve(query)
    answer = generate_answer(query, chunks)
    print(f"Câu hỏi: {query}\nTrả lời: {answer}")