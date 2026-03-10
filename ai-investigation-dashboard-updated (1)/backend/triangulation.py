
def detect_triangulation(messages):

triads=[]

for m in messages:
    text=m["text"].lower()

    if "said that" in text or "told me" in text:
        triads.append(m)

return triads
