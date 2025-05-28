import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text="Hello i am Sahil Mahajan"
tokens = enc.encode(text)

print("Tokens:",tokens )

tokens = [13225, 575, 939, 50610, 311, 18429, 44750]
decoded = enc.decode(tokens)

print("Decoded",decoded)