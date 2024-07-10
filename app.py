text = "The quick brown fox jumps over the lazy dog."
taken = []
word = ""

for c in text:
    if c != " ":
        word += c
    else:
        taken.append(word)
        word = ""

if word:
    taken.append(word)

tokenss = ", ".join([f'"{tokens}"' for tokens in taken])
print(f"[{tokenss}]")
