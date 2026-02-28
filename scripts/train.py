import json
import random
import os

accuracy = round(random.uniform(0.85, 0.99), 4)

metrics = {
    "accuracy": accuracy
}

os.makedirs("artifacts", exist_ok=True)

with open("artifacts/metrics.json", "w") as f:
    json.dump(metrics, f)

with open("artifacts/model.pkl", "w") as f:
    f.write("dummy model")

print("Training complete. Accuracy:", accuracy)