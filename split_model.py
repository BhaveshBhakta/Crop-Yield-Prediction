import pickle

# Load the original model (run this only once to create the split files)
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Split and save the model into two parts
model_bytes = pickle.dumps(model)
halfway = len(model_bytes) // 2
part1, part2 = model_bytes[:halfway], model_bytes[halfway:]

with open("model_part1.pkl", "wb") as file1:
    file1.write(part1)

with open("model_part2.pkl", "wb") as file2:
    file2.write(part2)

print("Model split successfully into model_part1.pkl and model_part2.pkl.")
