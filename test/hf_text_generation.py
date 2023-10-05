from transformers import pipeline, set_seed
generator = pipeline('text-generation', model='gpt2')
set_seed(42)
print(generator("Hello, I'm a language model,", max_length=30, num_return_sequences=5))
