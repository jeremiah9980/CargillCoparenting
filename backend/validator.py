
def validate_dataset(data):

required=["messages"]

for r in required:
    if r not in data:
        raise ValueError(f"Dataset missing {r}")

for m in data["messages"]:
    if "sender" not in m or "text" not in m:
        raise ValueError("Invalid message structure")

return True
