from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Load GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
model.eval()

# Function to generate output from GPT-2
def run_gpt2(prompt, max_length=100):
    inputs = tokenizer(prompt, return_tensors="pt")
    input_ids = inputs["input_ids"]
    
    with torch.no_grad():
        outputs = model.generate(
            input_ids,
            max_length=max_length + len(input_ids[0]),
            temperature=0.7,
            top_p=0.9,
            repetition_penalty=1.2,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id  # avoid warnings
        )
    
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    # Return only the part after the prompt
    return generated_text[len(prompt):].strip()

# === User input ===
paragraph = input("Enter a paragraph: ")

# === Generate Summary ===
summary_prompt = f"Summarize the following paragraph:\n{paragraph}\nSummary:"
summary = run_gpt2(summary_prompt, max_length=60)

# === Generate Answer ===
question = input("Ask a question based on the paragraph: ")
qa_prompt = f"Paragraph: {paragraph}\nQuestion: {question}\nAnswer:"
answer = run_gpt2(qa_prompt, max_length=60)

# === Output ===
print("\n=== Summary ===")
print(summary)

print("\n=== Question & Answer ===")
print(f"Q: {question}")
print(f"A: {answer}")

# === Count a single word in paragraph ===
count = input("Enter a word to count in the paragraph: ")

words_to_count = paragraph.split()
word_count = words_to_count.count(count)

if word_count == 0:
    print("The word is not present")
print(word_count)
