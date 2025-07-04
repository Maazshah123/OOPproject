from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load FLAN-T5 model and tokenizer
tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-base")
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-base")
model.eval()

# Function to run FLAN-T5 on any task
def run_flan_t5(prompt, max_length=100):
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
    outputs = model.generate(
        **inputs,
        max_length=max_length,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.2,
        do_sample=True
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# === User input ===
paragraph = input("Enter a paragraph: ")

# === Summarize the paragraph ===
summary_prompt = f"Summarize: {paragraph}"
summary = run_flan_t5(summary_prompt)

# === User input for question ===
question = input("Ask a question based on the paragraph: ")
qa_prompt = f"Answer the question based on the paragraph: {paragraph} Question: {question}"
answer = run_flan_t5(qa_prompt)

# === Output ===
print("\n=== Summary ===")
print(summary)

print("\n=== Question & Answer ===")
print(f"Q: {question}")
print(f"A: {answer}")

#count a single word in paragrap
count = input("Enter a word to count in the paragraph: ")

wordsToCount= paragraph.split()  
#print(wordsToCount[0])
word_count = 0  
for word in wordsToCount:
    if word == count: 
        word_count = word_count + 1 
else:
    print ("the word is not present")
print(word_count)
    
